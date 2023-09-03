#Naming Files Differently
from datetime import datetime

import os




#/////////////////////////////////////Taking the information about the seller /////////////////////////

#NOS = Name of Seller
NOS = input('\n \nHey,please tell your name. \n')
#SOF = Sellers offering
SOF = input('What is the food that you are giving?\n')
#PTG = price they are giving
PTG = input('At what price are you giving this food for? <please tell in ₹> \n')
#SPN = Sellers Phone Number
SPN = input('Please give us your phone number. \n')
#FEC = Food Expiry Checker
FEC = input('Date the food will expire. \n')





###############################Storing Place for food ####################################
import pickle

def storeData():
    # initializing data to be stored in db
    SNOS = {NOS}
    SSOF = {SOF}
    SPTG = {PTG}
    SSPN ={SPN}
    SFEC ={FEC}

    # database
    db = {}
    db['Seller Name'] = SNOS
    db['He or she is providing'] = SSOF
    db['The price'] = SPTG
    db['Phone Number of the Seller'] = SSPN
    db['Food Will Expire On '] = SFEC

    # Its important to use binary mode
    dbfile = open('SellerInformation', 'ab')

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()

def loadData():
    # for reading also binary mode is important
    dbfile = open('SellerInformation' , 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

if __name__ == '__main__':
    storeData()
    loadData()

Conforming = input("Are These correct? \n")
if Conforming.lower() == "yes":
    print ("Great")
    os.system('main.py')

else:
    print("Oh,sad to here that, Try Again")
    os.system('Python_.py')
