import os
import random
import sys


def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    base36 = ''
    sign = ''
    if number < 0:
        sign = '-'
        number = -number
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
    return sign + base36

def generateKey():
    lengthOfKey = input("How many caracters you want to have in your key ?")
    keyCache = ""
    for key in range(lengthOfKey): 
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
        'Do you want to decrypt or encrypt, choose "1" for decrypt and "2" for encrypt')
    if (choice != '1') and (choice != '2'):
        print("You didn't choose between 1 or 2...")
        main()
    else:
        if choice == '1':
            method = 'decrypt'
        if choice == '2':
            method = 'encrypt'
        baseNumber = input('In which base do you want to {0} ?', format(method))
    print('What do you want to ' + method)
    textinput = input()
    arrayToProcess = []
    arrayWord = list(textinput)
    if method == 'encrypt':
        for i in range(len(arrayWord)):
            randomnessObsfuscate = False
            randomnessLenght = False
            obfuscateCount = 0
            lenCount = 0
            while(randomnessObsfuscate != True):
                if random.random() > 0.5:
                    obfuscateCount += 1
                else:
                    randomnessObsfuscate = True
            while(randomnessLenght != True):
                if random.random() > 0.5:
                    lenCount += 1
                else:
                    randomnessLenght = True
            charactersToArray = ""
            for ArrayMake in range(lenCount):
                charactersToArray += arrayWord[i]
                i += 1
            arrayToProcess.append([charactersToArray,obfuscateCount,lenCount])
        EncryptedKey = input("Tell the key you want to use for encrypting, if you want to generate a random key just press ENTER. (Enter Only AlphaNumerical Caracters, Minimum 2 caracters.)")
        if EncryptedKey == "":
            EncryptedKey = generateKey()
        x1, x2 = KeyParser(EncryptedKey)
        messageEncrypted = ""
        specificLastHeader = ""
        for index, ArrayInstruction in enumerate(arrayToProcess):
            StartCodon = (x1 * x2 + pow(index, 2)) / pow(index, 2) # check base taille
            EndCodon = (x1 * x2 + pow(index + ArrayInstruction[2], 2)) / pow(index + ArrayInstruction[2], 2) # check base taille
            adder = ""
            for iterationObsfucate in range (ArrayInstruction[1]):
                for i in range(baseNumber):
                    adder += random.choice(
                        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                if adder == StartCodon or adder == EndCodon:
                    iterationObsfucate = 0  # adder = taille base 
                    adder = ""
            messageEncrypted += adder
            messageEncrypted += StartCodon
            for iterationToTranslate in range(ArrayInstruction[2]):
                MessagerAdderFirstPart = (pow((index + iterationToTranslate), 2) / (pow(index + ArrayInstruction[2], 2) + pow(index, 2)))
                MessagerAdderLastPart = (1 / (1 + pow((index + iterationToTranslate), 2)))
                DecimalValueMessageToAdd = (StartCodon * EndCodon + MessagerAdderFirstPart) * MessagerAdderLastPart
                
                messageEncrypted += base36encode(DecimalValueMessageToAdd)
                # check la base
            messageEncrypted += EndCodon
    if method == 'decrypt':
        print("Incomming")
        
        # base à completer avec OPCODE au debut specififier ligne et Nombre de fois du maximum


main()

demainidhqzkdiqzdj'aiojqzodjqzdmangédqdzqzdqzdqzdesdzqdqzdqzdpates


36^n 
36
