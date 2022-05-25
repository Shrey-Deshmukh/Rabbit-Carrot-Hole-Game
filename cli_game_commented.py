import random
from sys import exit # to exit from the code that is running
# import time
import sys
import os
import keyboard # module for reading inputs
from pynput.keyboard import Key, Listener # used for keyboard
import msvcrt

def printFinal(pos):
    global X # You are changing the value of x, the change should be reflected across all functions
    randomlist=[]
    for i in range(0,N):
        randomlist.append('-')
# when r picks up c to become R and c becomes -, the change reflected in x was always r,c,o (first r used to change, then c then o)
# we reversed the for loop (2,1,0) and first change the o to o, c to - , r to R
    for i in reversed(range(3)):
        randomlist[pos[i]] = X[i] # now replace the positions in the randomlist with r, c, o
    final_str = "" # to convert list to string
    for ele in randomlist: # each element in the random list
        final_str  = final_str + str(ele) # this helps remove the , and '' and [] in the list
    final_str = "\r"+final_str # replacing small r with R. We want to replace r with R and also remove the c
#Carriage return- the rest of the content after the \r will come at the front of your line and will keep replacing
#your characters one by one until it takes all the contents left after the \r in that string.
#So whatever content is there after the \r will come at the beginning of our whole string
    sys.stdout.write(final_str) # you are not spawning a new line everytime a key is pressed or a change is made

# keys are defined here
def show(key):
    global X
    if key == Key.delete: #Key.delete is predefined. Press delete to exit from the cli
        return False
    # pos = [r,c,o]
    if str(key) == "\'d\'": # d is always to go right
        if pos[2] == pos[0] +1: # if o is right of r
            pass # d should not work
        elif pos[1] == pos[0] +1 and X[0] == 'r': # if c is right of r (it has to be small r not big R)
            pass # d should not work
        elif pos[2] == pos[1]+1: #if o is right of c (if c and o are right next to each other, jump across both)
            pos[0]=pos[0]+3 #r is jumping
        else:
            pos[0] = pos[0] + 1 # just continue moving to the right
        printFinal(pos) #shows the output

    if str(key) == "\'a\'": # a is always to go left
        if pos[2] == pos[0] - 1: #if o is left of r
            pass # a should not work
        elif pos[1] == pos[0] - 1 and X[0] == 'r': #if c is left of r and it is small r
            pass #a should not work
        elif pos[2] == pos[1]-1: #if o is left of c (basically o and c are together, jump across both)
            pos[0]=pos[0]-3 #r is jumping
        else:
            pos[0] = pos[0] - 1 #just continue moving left
        printFinal(pos)


    if str(key) == "\'j\'":
        if pos[2] == pos[0] +1 :# if o is right of r, you need to move it forward twice (basically jump once)
            pos[0] = pos[0] +2
        elif pos[2] == pos[0] -1 :# if o is left of r, you need to move backward twice
            pos[0] = pos[0] -2
        printFinal(pos)


    if str(key) == "\'p\'":# to pickup c and put c in the hole
        if (pos[1] == pos[0] +1 or pos[1] == pos[0] -1):# if c is right of r OR c is left of r
            X=['R','-','o'] # you change r to R, c to - and o to o

        if (pos[2] == pos[0]+1 or pos[2] == pos[0]-1):# if o is right of R or o is left of R
            if(X[0] == 'R'): # if R is next to o, and you press p, the cli should terminate
                return False
            #this should be capital R, if it is small r means it hasnt picked up
        printFinal(pos)

playAgain = True
while(playAgain):
    print("WELCOME!!!") #Every time you want to play again (and press Y), then new game should run
    N = 50
    X=['r','c','o']
    # r- rabbit without carrot
    # c- carrot
    # o- hole
    pos = random.sample(range(0,N),3) #generate 3 random nos from 1-50 (which will later hold the position of r,c and o)
    printFinal(pos) #function

    # with is like an endless while loop
    # every keypress calls the function show()
    with Listener(on_press = show) as listener:
        listener.join() # threading. Allows different parts of the program to run concurrently


    #print()
    while(True):

        while msvcrt.kbhit():# used to flush out the input queue (if you enter aaadddddaaaa it used to output this. we dont want to output this, hence use this line)
            msvcrt.getch()
        c = input("\nDO YOU WANT TO PLAY AGAIN [Y/N]")

        if(c == 'Y' or c == 'y'):
            playAgain = True
            break # comes out of this while loop and eneter while(playAgin) loop
        elif(c == 'n' or c == 'N'):
            playAgain = False
            break #it wont enter while(playAgain) and will directly print("BYEEE!")
        else:
            print("error: enter only [y/n]")# if you enter anything else

print("BYEEEE!")
