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

from background import *
from puzzle1GC import *
from puzzle1MT import *
from puzzle2GC import *
from puzzle2MT import *
import random
import pygame
from pygamegame import PygameGame

class Game(PygameGame):
    def init(self):
        self.bgColor = (180, 180, 180)
        self.player = "To be determined by server"
        Puzzle1.init()
        Puzzle2.init()
        Background.init()
        self.background = None
        self.solution = "Z"
        self.puzzle1 = None
        self.puzzle2 = None
        self.gameStart = False
        
    def playerInit(self):
        if self.player == "GC":
            self.background = Background(0, 0, Background.GCimage)
            self.puzzle1 = Puzzle1GC(self.solution)
            self.puzzle2 = Puzzle2GC()
        else:
            self.background = Background(0, 0, Background.MTimage)
            self.puzzle1 = Puzzle1MT(self.solution)
            self.puzzle2 = Puzzle2MT()

    def keyPressed(self, code, mod):
        pass
        
    def mousePressed(self, x, y):
        if self.gameStart == True:
            if self.player == "GC":
                if True: # find dimensions later
                    puzzle1Correct = self.puzzle1.buttonClick(x, y)
                    if puzzle1Correct != None:
                        forServer = True
                        msg = "puzzle1Response %s %s\n" % (forServer, puzzle1Correct)
                        print ("sending: ", msg,)
                        self.server.send(msg.encode())
                if self.puzzle2.x <= x <= self.puzzle2.x + 8 * self.puzzle2.tileSize and \
                   self.puzzle2.y <= y <= self.puzzle2.y + 8 * self.puzzle2.tileSize:
                    move = self.puzzle2.tileClick(x, y)
                    if move != None:
                        forServer = True
                        row = move[0]
                        col = move[1]
                        newRow = move[2]
                        newCol = move[3]
                        msg = "puzzle2MoveMade %s %d %d %d %d\n" % (forServer, row, col, newRow, newCol)
                        print ("sending: ", msg,)
                        self.server.send(msg.encode())
                elif self.puzzle2.highlight.sprite != None:
                    self.puzzle2.clickedTile = None
                    self.puzzle2.highlight.sprite.kill()
            else:
                pass

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
                self.playerInit()
    
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

            elif (command == "puzzle2Reception"):
                legal = msg[1]
                if legal == "True":
                    move = msg[2:]
                    self.puzzle2.makeMove(move)
                    self.puzzle2.update()
                else:
                    # impose penalty
                    pass
            #except:
              #  print("failed")
            serverMsg.task_done()
        if self.gameStart:
            if self.player == "GC":
                pass
            else:
                self.puzzle1.update()

    def redrawAll(self, screen):
        screen.blit(self.background.image, self.background.rect)
        if self.puzzle1 != None:
            self.puzzle1.draw(screen)
        if self.puzzle2 != None:
            self.puzzle2.draw(screen)
        
serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

Game(800, 600).run(server)