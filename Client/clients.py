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
from startMenu import *
import random
import pygame
from pygamegame import PygameGame

class Game(PygameGame):
    def init(self):
        self.bgColor = (180, 180, 180)
        self.playerNumber = "To be determined by server"
        self.player = "To be determined"
        self.otherPlayer = None
        self.playerReady = False
        self.otherPlayerReady = False
        Background.init()
        StartMode.init()
        GameMode.init()
        self.background = None
        self.mode = "Start"
        self.start = None
        self.game = None
        self.gameStart = False
        self.isWaiting = True

    def keyPressed(self, code, mod):
        pass
        
    def mousePressed(self, x, y):
        if self.mode == "Start":
            if not self.isWaiting:
                result = self.start.mousePressed(x, y)
                if result != None:
                    if result[0] == "Player":
                        self.player = result[1]
                        forServer = False
                        msg = "playerSelection %s %s %s\n" % (forServer, self.playerNumber, self.player)
                        print ("sending: ", msg,)
                        self.server.send(msg.encode())
                    elif result == "Start":
                        forServer = False
                        msg = "gameStart %s %s\n" % (forServer, self.playerNumber)
                        print ("sending: ", msg,)
                        self.server.send(msg.encode())
                
        elif self.mode == "Game":
            msg = self.game.mousePressed(x, y)
            if msg != None:
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
                self.playerNumber = myPID
                print("my ID is:", self.playerNumber)
                self.start = StartMode(self.playerNumber)
                if myPID == "p1":
                    self.player = "GC"
                    self.otherPlayer = "MT"
                else:
                    self.player = "MT"
                    self.otherPlayer = "GC"
    
            elif (command == "newPlayer"):
                self.isWaiting = False
                print("There's another player!")
    
            elif (command == "playerSelection"):
                playerNum = msg[1]
                player = msg[2]
                if playerNum != self.playerNumber:
                    self.otherPlayer = player
                if playerNum == "p1":
                    self.start.p1Tracker.sprite.move(player)
                else:
                    self.start.p2Tracker.sprite.move(player)
                isReady = self.start.startButton.sprite.findIsReady(self.player, self.otherPlayer)
                self.start.readyImage.sprite.changeImage(isReady)

            elif (command == "gameStart"):
                playerNum = msg[1]
                if playerNum != self.playerNumber:
                    self.otherPlayerReady = True
                else:
                    self.playerReady = True
                if self.playerReady and self.otherPlayerReady:
                    self.mode = "Game"
                    self.game = GameMode(self.player)

            elif (command == "puzzle1Reception"):
                correct = msg[1]
                if correct == "True":
                    self.game.solution = msg[2]
                    if self.player == "GC":
                        self.game.puzzle1 = Puzzle1GC(self.game.solution)
                    else:
                        self.game.puzzle1 = Puzzle1MT(self.game.solution)
                else:
                    self.game.puzzle1.timer.sprite.penalty(35)

            elif (command == "puzzle2Reception"):
                legal = msg[1]
                if legal == "True":
                    move = msg[2:]
                    self.game.puzzle2.makeMove(move)
                    self.game.puzzle2.update()
                else:
                    self.game.puzzle2.timer.sprite.penalty(10)

            elif (command == "puzzle2Won"):
                if self.game.player == "GC":
                    self.game.puzzle2 = Puzzle2GC()
                else:
                    self.game.puzzle2 = Puzzle2MT()
            
            elif(command == "puzzle3TumblerMove"):
                if self.player == "MT":
                    number = int(msg[1])
                    self.game.puzzle3.moveTumblers(number)
            #except:
              #  print("failed")
            serverMsg.task_done()
        if self.mode == "Start":
            pass
        elif self.mode == "Game":
            self.game.timerFired()
        

    def redrawAll(self, screen):
        if self.mode == "Start":
            self.start.draw(screen)
            if self.isWaiting:
                self.start.drawWaiting(screen)
        elif self.mode == "Game":
            self.game.draw(screen)
        
serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

Game(800, 600).run(server)