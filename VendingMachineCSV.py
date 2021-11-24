import os
import time
from time import sleep

def vendmach():

    print("Welcome to vending machine!")
    time.sleep(2)
    os.system('cls')

    file ="file.csv"
    infile= open(file, 'r')
    liste = [line.rstrip() for line in infile]

    for i in range (0, len(liste)):
        liste [i]= liste[i].split(",")
        liste[i][1]= eval(liste [i][1])
        liste[i][2]= eval(liste [i][2])
 
    cashamount = float(input("\n\nHow much money you want to put on?\n"))
    os.system('cls')
    
    condition = "y"                                               #checking condition that asks customer wants to keep buying
    while condition=="y":
        print("You got","{0:.2f}".format(cashamount),"dollars\n") #when customer put money on, he/she can see total money
        for i in range (len(liste)):                              #printing the liste and prices
            print(str(i+1)+"-",liste[i][0]+":", liste[i][1], end="$ | ")

    
        print("\n")
        # asking which item he/she wants to buy
        num= int(input("These are our products, please choose one each time and enter product's number: "))
        # if customer writes a number more then products' number, this code warns
        while (not num<=len(liste)):
            num = int(input("Please just write product's number. --be careful.\n"))
        num= num-1
        selected = liste[num]

        if selected[2]>0:                                           #checking is item avaliable
            if cashamount>=selected[1]:
                cashamount= cashamount- selected[1]                 #total money - item price = total money
                liste[num][2]=liste[num][2]-1                       #total stock-1= total stock
                print("\nCongurilations, you bought", selected[0],".\n")
            else:
                print("You don't have enough money\n")
        else:
            print("Sorry, we got no more",selected[0],".\n")
        
        condition= input("Do you want to continue y/n: ")
        os.system('cls')
        while (condition!="y" and condition!="n"):
            condition = input("Please just write y or n --be careful.\n")
    if condition == "n" :
        print("Here is your change: {0:.2f}".format(cashamount))

vendmach()
