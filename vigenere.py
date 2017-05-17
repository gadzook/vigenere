#!/usr/bin/python3
from string import ascii_lowercase, ascii_uppercase, printable
from time import sleep
import configparser

class Vigenere():
    def __init__(self):
        #config
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.PreserveFormatting = int(self.config['Formatting']['PreserveFormatting'])
        self.WordLength = int(self.config['Formatting']['WordLength'])
        self.RowLength = int(self.config['Formatting']['RowLength'])
        self.Caps = int(self.config['Formatting']['Caps'])

        #get text
        self.input_text = open("input_text.txt","r").read()
        self.stripped_text = "".join(char for char in self.input_text if char in printable)

    def get_key(self):
        input_key = input("Enter key: ")
        stripped_key = "".join([char for char in input_key.lower() if char in ascii_lowercase])
        return stripped_key

    def format(self,text):
        result_text = ""
        if self.PreserveFormatting == 1:
            return(text)

        char_list = [char for char in text if char in ascii_lowercase or char in ascii_uppercase]
 
        if self.WordLength > 0:
            for i, char in enumerate(char_list):
                if (i+1) % self.WordLength == 0:
                    result_text = result_text + char + " "
                else:
                    result_text = result_text + char
        else:
            result_text = text

        word_list = result_text.split()

        if self.RowLength >= 0:
            result_list = []
            for i, word in enumerate(word_list):
                if (i+1) % self.RowLength == 0:
                    result_list.append(word+"\n")
                else:
                    result_list.append(word+" ")
            result_text = "".join(result_list)

        if self.Caps == 1:
            result_text = result_text.lower()
        elif self.Caps == 2:
            result_text = result_text.upper()

        return result_text

    def vigenere(self,function):
        text = self.stripped_text
        key = self.get_key()
        result_text = ""
        for i in range(len(text)):
            text_letter = text[i]
            key_letter = key[i%len(key)]
            if text_letter in ascii_lowercase:
                alphabet = ascii_lowercase
            elif text_letter in ascii_uppercase:
                alphabet = ascii_uppercase
            else:
                result_text = result_text + text_letter
                continue
            text_number = alphabet.find(text_letter)
            key_number = alphabet.lower().find(key_letter)

            if function == "e":
                result_number = (text_number + key_number) % len(alphabet)
            else:
                result_number = (text_number - key_number) % len(alphabet)

            result_letter = alphabet[result_number]
            result_text = result_text + result_letter

        if function == "e":
            result_text = self.format(result_text)

        with open("output_text.txt","w") as output:
            output.write(result_text)

        print("Encrypting...\n\n")
        print(result_text+"\n\n")
        return result_text

    def run(self):
        choice = input("Would you like to (e)ncrypt or (d)ecrypt the input text? ")
        if choice == "e" or choice == "d":
            return self.vigenere(choice)
        else:
            print("Invalid choice.")
            self.run()

vigenere = Vigenere()
vigenere.run()