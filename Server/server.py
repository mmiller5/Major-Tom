'''
created by Rohan Varma, adapted by Kyle Chin
https://drive.google.com/drive/folders/0B3Jab-H-9UIiZ2pXMExjdDV1dW8
modified by me
'''

import socket
import threading
from queue import Queue

from puzzle1Generate import *
from puzzle2Logic import *

HOST = "" # put your IP address here if playing on multiple computers
PORT = 50005
BACKLOG = 2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST,PORT))
server.listen(BACKLOG)
print("looking for connection")

def handleClient(client, serverChannel, cID, clientele):
    client.setblocking(1)
    msg = ""
    while True:
        try:
            msg += client.recv(10).decode("UTF-8")
            command = msg.split("\n")
            while (len(command) > 1):
                readyMsg = command[0]
                msg = "\n".join(command[1:])
                serverChannel.put(str(cID) + " " + readyMsg)
                command = msg.split("\n")
        except:
            # we failed
            return

def serverThread(clientele, serverChannel):
    while True:
        msg = serverChannel.get(True, None)
        print("msg recv: ", msg)
        msgList = msg.split(" ")
        senderID = msgList[0]
        instruction = msgList[1]
        forServer = msgList[2]
        details = " ".join(msgList[3:])
        # pass message along to clients if not meant for server
        if forServer == "False":
            for cID in clientele:
                sendMsg = instruction + " " + details + "\n"
                clientele[cID].send(sendMsg.encode())
                print("> sent to %s:" % cID, sendMsg[:-1])
        else:
            print("for server only")
            serverMessage(msgList)
        print()
        serverChannel.task_done()

# update and compare to server side info depending on message
def serverMessage(msg):
    command = msg[1]
    print(command)
    if (command == "puzzle1Response"):
        correct = msg[3]
        instruction = "puzzle1Reception"
        if correct == "True":
            newSolution = puzzle1Generate()
            for cID in clientele:
                sendMsg = instruction + " " + correct + " " + newSolution + "\n"
                clientele[cID].send(sendMsg.encode())
                print("> sent to %s:" % cID, sendMsg[:-1])
        else:
            for cID in clientele:
                sendMsg = instruction + " " + correct + "\n"
                clientele[cID].send(sendMsg.encode())
                print("> sent to %s:" % cID, sendMsg[:-1])
    
    elif (command == "puzzle2MoveMade"):
        move = msg[3:] 
        instruction = "puzzle2Reception"
        legalMove = gameBoard.isLegalMove(move)
        if legalMove:
            legal = "True"
            gameBoard.makeMove(move, "Maxie")
            moveToMake = "%s" % move
            row = int(move[0])
            col = int(move[1])
            newRow = int(move[2])
            newCol = int(move[3])
            for cID in clientele:
                sendMsg = instruction + " " + legal + " %d %d %d %d\n" % (row, col, newRow, newCol)
                clientele[cID].send(sendMsg.encode())
                print("> sent to %s:" % cID, sendMsg[:-1])
            # Minnie make move
            #moveToMake = 
            '''
            for cID in clientele:
                sendMsg = instruction + " " + legal + " " + moveToMake + "\n"
                clientele[cID].send(sendMsg.encode())
                print("> sent to %s:" % cID, sendMsg[:-1])
            '''
        else:
            legal = "False"
            for cID in clientele:
                sendMsg = instruction + " " + legal + "\n"
                clientele[cID].send(sendMsg.encode())
                print("> sent to %s:" % cID, sendMsg[:-1])

    elif (command == "newPlayer"):
        pass
    
    elif (command == "puzzle1Solution"):
        pass





clientele = dict()
playerNum = 0

serverChannel = Queue(100)
threading.Thread(target = serverThread, args = (clientele, serverChannel)).start()

names = ["MT", "GC"]

while True:
    client, address = server.accept()
    # myID is the key to the client in the clientele dictionary
    myID = names[playerNum]
    print(myID, playerNum)
    for cID in clientele:
        print (repr(cID), repr(playerNum))
        clientele[cID].send(("newPlayer %s\n" % myID).encode())
        client.send(("newPlayer %s\n" % cID).encode())
    clientele[myID] = client
    client.send(("myIDis %s\n" % myID).encode())
    print("connection recieved from %s" % myID)
    threading.Thread(target = handleClient, args = 
                            (client ,serverChannel, myID, clientele)).start()
    playerNum += 1

def serverInit():
    gameBoard = Board()





