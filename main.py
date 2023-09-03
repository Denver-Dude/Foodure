###____________WELCOME PAGE______________###
import os

URS = input("Hey, are you here to buy food or give Food? \n")
if URS.lower() == "buy":
   os.system('Customer.py')


if URS.lower() == "give":
   os.system('Python_.py')
