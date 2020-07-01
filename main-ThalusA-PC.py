import os
import random
import sys
from math import floor
import re

baseNumber=0

def base36encode(number, boolean=True, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    base36 = ''
    sign = ''
    if 0 <= number < len(alphabet):
        return sign + alphabet[int(number)]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[int(i)] + base36
    if boolean == False:
        while len(base36) <= len(str(baseNumber)):
            base36 = "0"+base36
    print(base36)
    print(boolean)
    print(baseNumber)
    return base36

def generateKey():
    lengthOfKey = input("How many caracters you want to have in your key ?\n")
    keyCache = ""
    for key in range(int(lengthOfKey)): 
        keyCache += random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return keyCache


def KeyParser(EncryptedKey):
    x1 = 0
    x2 = 0
    for value in range(len(EncryptedKey)):
        if value%2 == 0:
            x1 += int(EncryptedKey[value], 36)
        else:
            x2 += int(EncryptedKey[value], 36)
    return x1, x2


def main():
    choice = input(
        'Do you want to decrypt or encrypt ?, choose "1" for decrypt and "2" for encrypt\n')
    if (choice != '1') and (choice != '2'):
        print("You didn't choose between 1 or 2...")
        main()
    else:
        if choice == '1':
            method = 'decrypt'
        if choice == '2':
            method = 'encrypt'
        baseNumber = input('In which base do you want to ' + method + ' ? (default = 6)\n')
        if baseNumber == "":
            baseNumber = 6
    print('What do you want to ' + method + '?')
    textinput = input()
    arrayToProcess = []
    arrayWord = list(textinput)
    if method == 'encrypt':
        while arrayWord:
            randomnessObsfuscate = False
            randomnessLenght = False
            obfuscateCount = 0
            lenCount = 1
            while not randomnessObsfuscate:
                if random.random() > 0.5:
                    obfuscateCount += 1
                else:
                    randomnessObsfuscate = True
            while not randomnessLenght:
                if random.random() > 0.5 and lenCount < len(arrayWord):
                    lenCount += 1
                else:
                    randomnessLenght = True
            charactersToArray = ""
            for i in range(lenCount):
                charactersToArray += arrayWord.pop(0)
            arrayToProcess.append([charactersToArray,obfuscateCount,lenCount])
        EncryptedKey = input("Tell the key you want to use for encrypting, if you want to generate a random key just press ENTER. (Enter Only AlphaNumerical Caracters, Minimum 2 caracters.)\n")
        if EncryptedKey == "":
            EncryptedKey = generateKey()
        x1, x2 = KeyParser(EncryptedKey)
        messageEncrypted = ""
        specificLastHeader = ""
        index = 0
        while arrayToProcess:
            CurrentTask = arrayToProcess.pop(0)
            adder = ""
            for iterationObsfucate in range(CurrentTask[1]):
                StartCodon = (x1 * x2 + pow(index, 2)) / (pow(index, 2)+1) 
                EndCodon = (x1 * x2 + pow(index + CurrentTask[2], 2)) / (pow(index + CurrentTask[2], 2)+1)
                for i in range(int(baseNumber)):
                    adder += random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                if int(adder, 36) == StartCodon or int(adder, 36) == EndCodon:
                    iterationObsfucate = 0
                    adder = ""
                index += 1
            messageEncrypted += adder
            StartCodon = (x1 * x2 + pow(index, 2)) / (pow(index, 2)+1) 
            EndCodon = (x1 * x2 + pow(index + CurrentTask[2], 2)) / (pow(index + CurrentTask[2], 2)+1)
            EndPosition = index + CurrentTask[2]
            lastNumStart = 0
            if(StartCodon/35 > int(baseNumber)):
                lastNumStart = floor(StartCodon / 35)
                specificLastHeader += str(index) + ":" + base36encode(lastNumStart, False) + '/'
            messageEncrypted += base36encode(StartCodon-(lastNumStart*35))
            index += 1
            for iterationToTranslate in range(CurrentTask[2]):
                MessagerAdderFirstPart = (pow((index), 2) / (
                    (pow(EndPosition, 2) + 1) + pow(index, 2)))
                MessagerAdderLastPart = (1 / (1 + pow((index), 2)))
                DecimalValueMessageToAdd = (StartCodon * EndCodon + MessagerAdderFirstPart) * MessagerAdderLastPart * ord(CurrentTask[0][iterationToTranslate])
                lastNumMsg = 0
                if DecimalValueMessageToAdd/35 > int(baseNumber):
                    lastNumMsg = DecimalValueMessageToAdd / 35
                    specificLastHeader += str(index) + ":" + base36encode(lastNumMsg, False) + '/'
                messageEncrypted += base36encode(DecimalValueMessageToAdd - (lastNumMsg*35))
                index += 1
            lastNumEnd = 0
            if(EndCodon/35 > int(baseNumber)):
                lastNumEnd = floor(EndCodon / 35)
                specificLastHeader += str(index) + ":" + base36encode(lastNumEnd, False) + '/'
            messageEncrypted += base36encode(EndCodon-(lastNumEnd*35))
            index += 1
    totalMsg = messageEncrypted + '/' + specificLastHeader
    print("Message encrypted : " + totalMsg)
    print("Key used to encrypt the message : " + EncryptedKey)
    if method == 'decrypt':
        regex = re.search('\/(.+)\/$', textinput)
        textinput = textinput[0:(len(textinput)-len(regex.group(1))-2)]
        arraySlicedPart = [textinput[i:i + baseNumber] for i in range(0, len(textinput), baseNumber)]
        # base à completer avec OPCODE au debut specififier ligne et Nombre de fois du maximum


main()
