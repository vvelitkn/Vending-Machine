import os
import time
from time import sleep

def vendmach():

    print("Welcome to vending machine!")
    time.sleep(2)
    os.system('cls')
    #Item dictionary
    a = {"item":"1kg banana", "price":2, "stock":5}
    b = {"item":"1kg apple", "price":1.5, "stock":5}
    c = {"item":"1kg pear", "price":1, "stock":5}
    d = {"item":"1kg strawberry", "price":2.5, "stock":5}
    e = {"item":"1 pineapple", "price":3, "stock":5}
    f = {"item":"1kg orange", "price":1, "stock":5}

    #Items conventing to list
    items = [a, b, c, d, e]
    liste=[[],[],[],[],[]]
    for i in range (len(items)):
        liste[i] = [items[i].get("item"),items[i].get("price"),items[i].get("stock")]
    cashamount = float(input("\n\nHow much money you want to put on?\n"))
    os.system('cls')
    
    condition = "y"                                               #checking condition that asks customer wants to keep buying
    while condition=="y":
        print("You got","{0:.2f}".format(cashamount),"dollars\n") #when customer put money on, he/she can see total money
        for i in range (len(items)):                              #printing the items and prices
            print(str(i+1)+"-",items[i].get("item")+":", items[i].get("price"), end="$ | ")

    
        print("\n")
        # asking which item he/she wants to buy
        num= int(input("These are our products, please choose one each time and enter product's number: "))
        # if customer writes a number more then products' number, this code warns
        while (not num<=len(items)):
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
