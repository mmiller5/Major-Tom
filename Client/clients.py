'''
Sockets part created by Rohan Varma, adapted by Kyle Chin
https://drive.google.com/drive/folders/0B3Jab-H-9UIiZ2pXMExjdDV1dW8
Pygame part created by Lukas Peraza
https://github.com/LBPeraza/Pygame-Asteroids
combined and modified by me
'''

import socket
import threading
from queue import Queue

HOST = "" # put your IP address here if playing on multiple computers
PORT = 50005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")

def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")

from Dino import *
from puzzle1GC import *
from puzzle1MT import *
import random
import pygame
from pygamegame import PygameGame

class Game(PygameGame):
    def init(self):
        self.bgColor = (180, 180, 180)
        self.player = "To be determined by server"
        Dino.init()
        # going to want to do "if player == GC: initialize GC stuff" later
        Puzzle1.init()
        self.solution = "Z"
        self.puzzle1 = None
        self.dinos = pygame.sprite.Group()
        self.gameStart = False
        

    def keyPressed(self, code, mod):
        pass
        
    def mousePressed(self, x, y):
        if self.gameStart == True:
            if self.player == "GC":
                puzzle1Correct = self.puzzle1.buttonClick(x, y)
                if puzzle1Correct != None:
                    forServer = True
                    msg = "puzzle1Response %s %s\n" % (forServer, puzzle1Correct)
                    print ("sending: ", msg,)
                    self.server.send(msg.encode())
            else:
                forServer = False
                msg = "dinoMade %s %d %d\n" % (forServer, x, y)
                print ("sending: ", msg,)
                self.server.send(msg.encode())
            
        
    def timerFired(self):
        while (serverMsg.qsize() > 0):
            msg = serverMsg.get(False)
            #try:
            print("received: ", msg, "\n")
            msg = msg.split()
            command = msg[0]
            print(command)
            
            if (command == "myIDis"):
                myPID = msg[1]
                self.player = myPID
                print("my ID is:", self.player)
                if self.player == "GC":
                    print("player is Ground Control")
                    self.puzzle1 = Puzzle1GC(self.solution)
                else:
                    print("player is Major Tom")
                    self.puzzle1 = Puzzle1MT(self.solution)
            
            elif (command == "dinoMade"):
                x = int(msg[1])
                y = int(msg[2])
                self.dinos.add(Dino(x, y))
    
            elif (command == "newPlayer"):
                self.gameStart = True
                print("There's another player!")
            
            elif (command == "puzzle1Reception"):
                correct = msg[1]
                if correct == "True":
                    self.solution = msg[2]
                    if self.player == "GC":
                        self.puzzle1 = Puzzle1GC(self.solution)
                    else:
                        self.puzzle1 = Puzzle1MT(self.solution)
                else:
                    # impose penalty
                    pass

            #except:
              #  print("failed")
            serverMsg.task_done()

    def redrawAll(self, screen):
        self.dinos.draw(screen)
        #if self.player == "GC":
        if self.puzzle1 != None:
            self.puzzle1.draw(screen)
        
serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

Game(800, 500).run(server)