import os
import random
import sys

def main():
    print('Do you want to decrypt or encrypt, choose "1" for decrypt and "2" for encrypt')
    choice = input()
    if (choice != '1') and (choice != '2'):
        print("You didn't choose between 1 or 2...")
        main()
    else:
        if choice == '1':
            method = 'decrypt'
        if choice == '2':
            method = 'encrypt'
    print('What do you want to '+method)
    textinput = input()
    if method == 'decrypt':
        array = list(textinput)
        removecount2 = False
        stop = False
        count = 0
        stop2 = False
        count2 = 1
        characterstowrite = ""
        actuallength = 0
        for characters in array:
            encodedpattern = []
            if removecount2 == True:
                stop = False
                count = 0
                stop2 = False
                while count2 != 0:
                    characterstowrite = characterstowrite + characters
                    encodedpattern.append([count, count2, characterstowrite])
                    count2 = count2 - 1
                    continue
            else:
                characterstowrite = characterstowrite + characters
            while stop == False:
                if random.random() >= 0.5:
                    stop = True 
                else:
                    count = count + 1   
            while stop2 == False:
                if random.random() >= 0.5 or actuallength >= len(array):
                    stop2 = True
                else:
                    count2 = count2 + 1
                    actuallength = actuallength + 1
                    removecount2 = True
            print(encodedpattern)    
    if method == 'encrypt':
        textinput.split()

main()

