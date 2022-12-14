#! /usr/bin/python3

import rsa
import base64
import pyfiglet
import random
from termcolor import colored
import os
import datetime

#FONTS
fonts = ["banner","big","block","bubble","circle","digital","emboss","emboss2","future","ivrit","lean","letter","mini","mnemonic","pagga","script","shadow","slant","small","smblock","smbraille","smscript","smshadow","smslant","standard","term","wideterm"]

#COLORS
colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]

#BANNER
def banner():
	ran_font = random.choice(fonts)
	ran_color = random.choice(colors)
	banner = pyfiglet.figlet_format("TEXT\nENCRYPTION\nDECRYPTION",font = ran_font)
	print (colored(banner,ran_color))

#YOUR CHOICE
def choice():
	print ("\n1.Encryption\n2.Decryption\n3.Back")
	choice = int(input())
	if (choice == 1):
		Encrypter()
	if (choice == 2):
		Decrypter()
	if (choice == 3):
		return()


#KEY LOADING
def getPriKey():
	with open('prikey.pem', 'rb')as f:
		PriKey = rsa.PrivateKey.load_pkcs1(f.read())
	return PriKey

def getPubKey():
	with open('pubkey.pem', 'rb')as f:
		PubKey = rsa.PublicKey.load_pkcs1(f.read())
	return PubKey

#FILE OPENING
def file_open():
	global file
	global locate
	user = os.getlogin()
	locate = "/home/" + user + "/Documents/encrypted_text/"
	if not os.path.exists(locate):
		os.makedirs(locate)
	samay = datetime.datetime.now()
	day = str(samay.day)
	hour = str(samay.hour)
	min = str(samay.minute)
	file = "enc_d" + day + "_h" +  hour + "_m" + min + ".txt"

#ENCRYPTION
def Encrypter():
	global file
	global locate
	text = input("Text: ")
	PubKey = getPubKey()
	file_open()
	try:
		cipher = rsa.encrypt(text.encode('utf-8'), PubKey)
		with open(locate + file, "wb") as en:
			en.write(cipher)
		print (colored("[+]Encryption done", 'green'))
	except:
		print (colored("[!!] Encryption failed", 'red'))
	en.close()
	choice()


#DECRYPTION
def Decrypter():
	fi = input("Path: ")
	PriKey = getPriKey()
	try:
		with open (fi, 'rb') as de:
			cipher = de.read()
		text = rsa.decrypt(cipher, PriKey).decode('utf-8')
		print ("Text: ",text)
	except:
		print (colored("[!!]Decryption failed",'red'))
	de.close()
	choice()
