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
import random
import pygame
from pygamegame import PygameGame

class Game(PygameGame):
    def init(self):
        self.bgColor = (255, 180, 180)
        self.player = "To be determined by server"
        Dino.init()
        # going to want to do "if player == GC: initialize GC stuff" later
        Puzzle1GC.init()
        self.solution = "Z"
        self.puzzle1 = None
        self.dinos = pygame.sprite.Group()
        self.gameStart = False
        

    def keyPressed(self, code, mod):
        pass
        
    def mousePressed(self, x, y):
        if self.gameStart == True:
            msg = "dinoMade %d %d\n" % (x, y)
            self.dinos.add(Dino(x, y))
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
            
            elif (command == "dinoMade"):
                x = int(msg[2])
                y = int(msg[3])
                self.dinos.add(Dino(x, y))
    
            elif (command == "newPlayer"):
                self.gameStart = True
                print("There's another player!")
              
            #except:
              #  print("failed")
            serverMsg.task_done()

    def redrawAll(self, screen):
        self.dinos.draw(screen)
        if self.player == "GC":
            if self.puzzle1 != None:
                self.puzzle1.draw(screen)
        
serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

Game(800, 500).run(server)
'''
####################################
# customize these functions
####################################

def init(data):
    data.me = Dot("Lonely", data.width/2, data.height/2)
    data.otherStrangers = dict()
    data.squares = []

def mousePressed(event, data):
    x = event.x
    y = event.y
    msg = "squareMade %d %d\n" % (x, y)
    data.squares += [Square(x, y)]
    print ("sending: ", msg,)
    data.server.send(msg.encode())

def keyPressed(event, data):
    dx, dy = 0, 0
    msg = ""

    # moving
    if event.keysym in ["Up", "Down", "Left", "Right"]:
      speed = 5
      if event.keysym == "Up":
        dy = -speed
      elif event.keysym == "Down":
        dy = speed
      elif event.keysym == "Left":
        dx = -speed
      elif event.keysym == "Right":
        dx = speed
      # move myself
      data.me.move(dx, dy)
      # update message to send
      msg = "playerMoved %d %d\n" % (dx, dy)

    # teleporting
    elif event.keysym == "space":
      # get a random coordinate
      x = random.randint(0, data.width)
      y = random.randint(0, data.height)
      # teleport myself
      data.me.teleport(x, y)
      # update the message
      msg = "playerTeleported %d %d\n" % (x, y)

    # send the message to other players!
    if (msg != ""):
      print ("sending: ", msg,)
      data.server.send(msg.encode())

def timerFired(data):
    # timerFired receives instructions and executes them
    while (serverMsg.qsize() > 0):
      msg = serverMsg.get(False)
      try:
        print("received: ", msg, "\n")
        msg = msg.split()
        command = msg[0]

        if (command == "myIDis"):
          myPID = msg[1]
          data.me.changePID(myPID)

        elif (command == "newPlayer"):
          newPID = msg[1]
          x = data.width/2
          y = data.height/2
          data.otherStrangers[newPID] = Dot(newPID, x, y)

        elif (command == "playerMoved"):
          PID = msg[1]
          dx = int(msg[2])
          dy = int(msg[3])
          data.otherStrangers[PID].move(dx, dy)

        elif (command == "playerTeleported"):
          PID = msg[1]
          x = int(msg[2])
          y = int(msg[3])
          data.otherStrangers[PID].teleport(x, y)

        elif (command == "squareMade"):
          x = int(msg[2])
          y = int(msg[3])
          data.squares += [Square(x, y)]
        
        elif (command == "givePosition"):
          x = data.me.x
          y = data.me.y
          msg = "takePosition %d %d\n" % (x, y)
          data.server.send(msg.encode())
        
        elif (command == "takePosition"):
          PID = msg[1]
          x = int(msg[2])
          y = int(msg[3])
          if not PID in data.otherStrangers:
            data.otherStrangers[PID] = Dot(PID, x, y)

      except:
        print("failed")
      serverMsg.task_done()

def redrawAll(canvas, data):
    # draw squares
    for square in data.squares:
      square.drawSquare(canvas)
    # draw other players
    for playerName in data.otherStrangers:
      data.otherStrangers[playerName].drawDot(canvas, "blue")
    # draw me
    data.me.drawDot(canvas, "red")

####################################
# use the run function as-is
####################################

def run(width, height, serverMsg=None, server=None):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.server = server
    data.serverMsg = serverMsg
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

run(200, 200, serverMsg, server)
'''