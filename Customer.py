import pickle

print('Hey, can we know your name?')
Name = input()
#CIFIN = Conforming If Food Is NEEDED
CIFIN = input('\nHi, '+Name+' do you want to see the list of people willing to give food?\n')

def loadData():
    # for reading also binary mode is important
    dbfile = open('SellerInformation' , 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

if __name__ == '__main__':
        loadData()

Conforming = input("We hope this is what you wanted. \n")
if Conforming.lower() == "yes":
    print ("Great, Have a great day "+Name)

