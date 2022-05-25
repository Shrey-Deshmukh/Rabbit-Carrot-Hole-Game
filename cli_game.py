# code written by Shrey Deshmukh
# please install keyboard module and pynput module
import random
from sys import exit
import sys
import os
import keyboard
from pynput.keyboard import Key, Listener
import msvcrt

def printFinal(pos):
    global X
    randomlist=[]
    for i in range(0,N):
        randomlist.append('-')
    for i in reversed(range(3)):
        randomlist[pos[i]] = X[i]
    final_str = ""
    for ele in randomlist:
        final_str  = final_str + str(ele)
    final_str = "\r"+final_str
    sys.stdout.write(final_str)

# keys are defined here
def show(key):
    global X
    if key == Key.delete:
        return False
    if str(key) == "\'d\'":
        if pos[2] == pos[0] +1:
            pass
        elif pos[1] == pos[0] +1 and X[0] == 'r':
            pass
        elif pos[2] == pos[1]+1:
            pos[0]=pos[0]+3
        else:
            pos[0] = pos[0] + 1
        printFinal(pos)

    elif str(key) == "\'a\'":
        if pos[2] == pos[0] - 1:
            pass
        elif pos[1] == pos[0] - 1 and X[0] == 'r':
            pass
        elif pos[2] == pos[1]-1:
            pos[0]=pos[0]-3
        else:
            pos[0] = pos[0] - 1
        printFinal(pos)


    elif str(key) == "\'j\'":
        if pos[2] == pos[0] +1 :
            pos[0] = pos[0] +2
        elif pos[2] == pos[0] -1 :
            pos[0] = pos[0] -2
        printFinal(pos)


    elif str(key) == "\'p\'":
        if (pos[1] == pos[0] +1 or pos[1] == pos[0] -1):
            X=['R','-','o']

        if (pos[2] == pos[0]+1 or pos[2] == pos[0]-1):
            if(X[0] == 'R'):
                return False
        printFinal(pos)

playAgain = True
while(playAgain):
    print("WELCOME TO THIS GAME!!")
    print("Rules:")
    print("Press 'd' to move the rabbit right, 'a' to move the rabbit left")
    print("Press 'j' to jump over the hole, 'p' to pickup and drop the carrot\n")
    N = 50
    X=['r','c','o']
    # r- rabbit without carrot
    # c- carrot
    # o- hole

    pos = random.sample(range(0,N),3)
    printFinal(pos)

    with Listener(on_press = show) as listener:
        listener.join()


    while(True):

        while msvcrt.kbhit():
            msvcrt.getch()
        c = input("\nDO YOU WANT TO PLAY AGAIN [Y/N]\n")

        if(c == 'Y' or c == 'y'):
            playAgain = True
            break
        elif(c == 'n' or c == 'N'):
            playAgain = False
            break
        else:
            print("Error: Enter only [y/n]")

print("THANK YOU FOR PLAYING!")
