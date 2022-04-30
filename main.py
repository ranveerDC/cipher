import string
from colorama import Fore, Style
import webbrowser
#Importing libraries to make my program better and more efficient.

alphabet = string.ascii_lowercase #Defining the alphabet as a variable with the use of the string module.

def validityOfMessage(inputString):
  outputOfFunction = all(x.isalpha() or x.isspace() for x in userMessage)
  return outputOfFunction #Defining the function that I will need later to determine if the user's entered message is valid for the program.

def validityOfShift(inputString):
  outputOfFunction = str(shiftAmount).isdigit()
  return outputOfFunction #Defining the function that I will need later to determine if the user's entered shift is valid for the program.

def atbash(userMessage): #Creating the atbash cipher function.
  alpha = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm,', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
  atbash = ['Z', 'z', 'Y', 'y', 'X', 'x', 'W', 'w', 'V', 'v', 'U', 'u', 'T', 't', 'S', 's', 'R', 'r', 'Q', 'q', 'P', 'p', 'O', 'o', 'N', 'n', 'M', 'm', 'L', 'l', 'K', 'k', 'J', 'j', 'I', 'i', 'H', 'h', 'G', 'g', 'F', 'f', 'E', 'e', 'D', 'd', 'C', 'c', 'B', 'b', 'A', 'a']
  outputAtbash = ""
  for i in range(len(userMessage)):
    if userMessage[i] != ' ':
        for x in range(len(alpha)):
            if userMessage[i] == alpha[x]:
                outputAtbash = outputAtbash + atbash[x]
    elif userMessage[i] == ' ':
        outputAtbash = outputAtbash + " "
  return(outputAtbash)

def encryptCaesar(userMessage, shiftAmount): #Defining the encrypt function of the Caeasr cipher.
  cipherText = ""
  for i in range(0, len(userMessage)):
    letterInOrder = ord(userMessage[i])
    shiftedLetter = letterInOrder + shiftAmount
    if userMessage[i] == " ":
      cipherText = cipherText + " "
    elif shiftedLetter > 122 or shiftedLetter >= 91 and shiftedLetter <= 116 and letterInOrder >= 65 and letterInOrder <= 90:
      shiftedLetter = shiftedLetter - 26 #Wrapping the encrypted text to the alphabet.
    cipherText = cipherText + chr(shiftedLetter)
  return cipherText

def excludeSymbols(encryptedCaesar): #Creating a function to filter out the symbols of the encrypted text.
  refined = ""
  for i in range(0, len(encryptedCaesar)):
    if encryptedCaesar[i].isalpha() == True:
      refined = refined + encryptedCaesar[i]
    elif encryptedCaesar[i] == " ":
      refined = refined + " "
  return refined

def decryptCaesar(userMessage, shiftAmount): #Defining the decrypt function of the Caeasr cipher.
  decrypted = ""
  for i in range(0, len(userMessage)):
    letterInOrder = ord(userMessage[i])
    removeShift = letterInOrder - shiftAmount
    if letterInOrder <= 90 and userMessage[i] != " ":
      if removeShift >= ord("A"):
        shiftAmount = shiftAmount + chr(removeShift)
      else:
        decrypted = decrypted + chr(removeShift + 26)
    elif userMessage[i] == " ":
      decrypted = decrypted + userMessage[i]
    else:
      if removeShift >= ord("a"):
        decrypted = decrypted + chr(removeShift)
      else:
        decrypted = decrypted + chr(removeShift + 26)
  return decrypted

print("Enter your message that you will be using. Please note that this message may only contain letters and spaces.")
userMessage=input() #If the user entered a capital E, it will inform the user that it has selected encryption mode and asks for the message that the user wants to encrypt.

while True: #Using a while true loop to make sure that the user corrects their input correctly if needed to.
  if validityOfMessage(userMessage) is False:
    print(Fore.RED + "You have entered an invalid message.")
    print(Style.RESET_ALL + "Input a new message, only containing letters.")
    userMessage=input()
    continue #Checking the validity of the message that the user has entered, and allowing them to change it if it is invalid.
  elif validityOfMessage(userMessage) is True:
    break

print("Enter capital C for the Caesar cipher or capital A for the Atbash cipher.")
userCipher=input()

while True:
  if userCipher == "C" or userCipher == "A":
    break
  elif str(userCipher) != "C" or str(userCipher) != "A":
    print(Fore.RED + "You have entered an invalid input.")
    print(Style.RESET_ALL + "Input capital C for the Caesar cipher or capital A for the Atbash cipher.")
    userCipher=input() #Making sure the user's input is valid and if it is not valid, allowing them to enter a valid input.

if userCipher == "C":
    print("Would you like to encrypt or decrypt this message? Input capital E for encrypt or capital D for decrypt.")
    userMode=input() #Asking the user which mode it would like to select.

    while True:
        if userMode == "E" or userMode == "D":
            break
        elif str(userMode) != "E" or str(userMode) != "D":
            print(Fore.RED + "You have entered an invalid input.")
            print(Style.RESET_ALL + "Input capital E for encrypt or capital D for decrypt.")
            userMode=input() #Making sure the user's input is valid and if it is not valid, allowing them to enter a valid input.

    print("Enter the shift you will be using.")
    shiftAmount=input() #Asking the user for the shift it would like to use.

    while True:
        if validityOfShift(shiftAmount) == True:
            shiftAmount = int(shiftAmount) % 26
            break
        elif validityOfShift(shiftAmount) == False:
            print(Fore.RED+"You have entered an invalid input.")
            print(Style.RESET_ALL+"Enter the shift that you will be using.")
            shiftAmount =input()
            continue #Making sure that the user entered a valid input when asked for the shift.

    if userMode == "E":
            encryptedCaesar = encryptCaesar(userMessage, shiftAmount)
            encryptedCaesar = excludeSymbols(encryptedCaesar)
            print("Your encrypyed message is", encryptedCaesar + ".") #Using the function I previously created to get the encrypted text.
            print("Would you like to export your result to a txt file? Enter capital Y for yes or capital N for no.")
            userExport=input()
            while True:
              if userExport == "Y" or userExport == "N":
                if userExport =="N":
                  print("Thank you for using my program!")
                  quit()
                if userExport=="Y":
                  with open('cipherExport.txt', 'w') as exportReadFile:
                      exportReadFile.write(encryptedCaesar)
                print("Would you like to open the file you just exported to? Enter capital Y for yes or capital N for no.")
                userOpen=input()
                if userOpen=="Y":
                    webbrowser.open("cipherExport.txt")
                    print("Thank you for using my program!")
                    quit()
              elif userExport != "Y" or userExport != "N":
                              print(Fore.RED+"You have entered an invalid input.")
                              print(Style.RESET_ALL + "Enter capital Y for Yes and capital N for no.")
                              userExport=input()
                              continue

    if userMode == "D":
            decryptedCaesar = decryptCaesar(userMessage, shiftAmount)
            decryptedCaesar = excludeSymbols(decryptedCaesar)
            print("Your encrypyed message is", decryptedCaesar + ".") #Using the function I previously created to get the decrypted text.
            print("Would you like to export your result to a txt file? Enter capital Y for yes or capital N for no.")
            userExport=input()
            while True:
              if userExport == "Y" or userExport == "N":
                if userExport =="N":
                  print("Thank you for using my program!")
                  quit()
                if userExport=="Y":
                  with open('cipherExport.txt', 'w') as exportReadFile:
                      exportReadFile.write(decryptedCaesar)
                print("Would you like to open the file you just exported to? Enter capital Y for yes or capital N for no.")
                userOpen=input()
                if userOpen=="Y":
                    webbrowser.open("cipherExport.txt")
                    print("Thank you for using my program!")
                    quit()
              elif userExport != "Y" or userExport != "N":
                              print(Fore.RED+"You have entered an invalid input.")
                              print(Style.RESET_ALL + "Enter capital Y for Yes and capital N for no.")
                              userExport=input()
                              continue
              

if userCipher == "A":
            print("The atbash of this message is", atbash(userMessage) + ".") #Calling the atbash function.
            print("Would you like to export your result to a txt file? Enter capital Y for yes or capital N for no.")
            userExport=input()
            while True:
              if userExport == "Y" or userExport == "N":
                if userExport =="N":
                  print("Thank you for using my program!")
                  quit()
                if userExport=="Y":
                  with open('cipherExport.txt', 'w') as exportReadFile:
                      exportReadFile.write(atbash(userMessage))
                print("Would you like to open the file you just exported to? Enter capital Y for yes or capital N for no.")
                userOpen=input()
                if userOpen=="Y":
                    webbrowser.open("cipherExport.txt")
                    print("Thank you for using my program!")
                    quit()
              elif userExport != "Y" or userExport != "N":
                              print(Fore.RED+"You have entered an invalid input.")
                              print(Style.RESET_ALL + "Enter capital Y for Yes and capital N for no.")
                              userExport=input()
                              continue