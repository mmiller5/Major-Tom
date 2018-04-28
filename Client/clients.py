# Opens the interface for each client. Sends messages to and receives messages
# from the server
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
PORT = 50004

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

from background import *
from gameScreen import *
import random
import pygame
from pygamegame import PygameGame

class Game(PygameGame):
    def init(self):
        self.bgColor = (180, 180, 180)
        self.player = "To be determined by server"
        Background.init()
        GameMode.init()
        self.background = None
        self.mode = "Game"
        self.game = None
        self.gameStart = False

    def keyPressed(self, code, mod):
        pass
        
    def mousePressed(self, x, y):
        if self.mode == "Game":
            msg = self.game.mousePressed(x, y)
            if msg != None:
                self.server.send(msg.encode())
            # look up mode connections

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
                self.game = GameMode(self.player)#playerInit()
    
            elif (command == "newPlayer"):
                self.gameStart = True
                print("There's another player!")

            elif (command == "puzzle1Reception"):
                correct = msg[1]
                if correct == "True":
                    self.game.solution = msg[2]
                    if self.player == "GC":
                        self.game.puzzle1 = Puzzle1GC(self.game.solution)
                    else:
                        self.game.puzzle1 = Puzzle1MT(self.game.solution)
                else:
                    # impose penalty
                    self.game.puzzle1.timer.sprite.penalty(35)

            elif (command == "puzzle2Reception"):
                legal = msg[1]
                if legal == "True":
                    move = msg[2:]
                    self.game.puzzle2.makeMove(move)
                    self.game.puzzle2.update()
                else:
                    # impose penalty
                    self.game.puzzle2.timer.sprite.penalty(10)

            elif (command == "puzzle2Won"):
                if self.game.player == "GC":
                    self.game.puzzle2 = Puzzle2GC()
                else:
                    self.game.puzzle2 = Puzzle2MT()
            #except:
              #  print("failed")
            serverMsg.task_done()
        if self.mode == "Game":
            self.game.timerFired()
        '''
        if self.gameStart:
            if self.player == "GC":
                pass
            else:
                self.puzzle1.update()
            self.puzzle1.timer.update()
            self.puzzle2.timer.update()
            # check if puzzle failed
            if self.puzzle1.timer.timerDone() or \
               self.puzzle2.timer.timerDone():
                pass
        '''

    def redrawAll(self, screen):
        if self.mode == "Game":
            self.game.draw(screen)
        
serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

Game(800, 600).run(server)