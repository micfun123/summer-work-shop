from receipt import maker
import json
import csv
from emailsend import send_mail

with open("shop.json", "r") as readfile:
    data = json.load(readfile)

basket = []



def categories(type):
    match type:
        case 1:
            for i in data:
                model = i["model"]
                price = i["price"]
                pricewithtax = price * 1.20
                type = i["type"]
                id = i["id"]
                if i["quantity"] < 0:
                    pass
                else:
                    print(f"{id}: \n")
                    print(f"The {type} is a {model} at the price of {price}. price with tax {pricewithtax}\n")

            print("\n========================================================\n")

            print("press 0 to go back or type a id to add to basket")
            choice = input()
            
            if choice == "0":
                main()
            else:
                basket.append(choice)
                print(f"in your basket is \n {basket} ")
                main()
        case 2:
            for i in data:
                model = i["model"]
                price = i["price"]
                pricewithtax = price * 1.20
                type = i["type"]
                id = i["id"]
                if type == "CPU":
                    if i["quantity"] < 0:
                        pass
                    else:
                        print(f"{id}: \n")
                        print(f"The {type} is a {model} at the price of {price}. price with tax {pricewithtax}\n") 
            print("\n========================================================\n")
            print("press 0 to go back or type a id to add to basket")
            choice = input()
            
            if choice == "0":
                main()
            else:
                basket.append(choice)
                print(f"in your basket is \n {basket} ")
                main()
            
        case 3:
            for i in data:
                model = i["model"]
                price = i["price"]
                pricewithtax = price * 1.20
                type = i["type"]
                id = i["id"]
                if type == "RAM":
                    if i["quantity"] < 0:
                        pass
                    else:
                        print(f"{id}: \n")
                        print(f"The {type} is a {model} at the price of {price}. price with tax {pricewithtax}\n")  
            print("\n========================================================\n")
            print("press 0 to go back or type a id to add to basket")
            choice = input()
            
            if choice == "0":
                main()
            else:
                basket.append(choice)
                print(f"in your basket is \n {basket} ")
                main()

        case 4:
            for i in data:
                model = i["model"]
                price = i["price"]
                pricewithtax = price * 1.20
                type = i["type"]
                id = i["id"]
                if type == "STORAGE":
                    if i["quantity"] < 0:
                        pass
                    else:
                        print(f"{id}: \n")
                        print(f"The {type} is a {model} at the price of {price}. price with tax {pricewithtax}\n")  
            print("\n========================================================\n")
            print("press 0 to go back or type a id to add to basket")
            choice = input()
            
            if choice == "0":
                main()
            else:
                basket.append(choice)
                print(f"in your basket is \n {basket} ")
                main()

        case 5:
                print("adding your basket up")
                total = 0
                for i in basket:
                    for j in data:
                        id = j["id"]
                        if int(i) == int(id):
                            print("ID found")
                            total = total + j["price"]
                print(f"your total is {total}")
                check = input("would you like to return to shopping or pay. please type yes for shopping or pay  : ")
                if check == "yes":
                    main()
                else:
                    name = input("Please ender your name: ")
                    email = input("Please enter your email: ")
                    receiptlist = []
                    for i in basket:
                         for j in data:
                            id = j["id"]
                            if int(i) == int(id):
                                item = j["model"]
                                price = j["price"]
                                receiptlist.append({"item": item ,"price" : price})
                    buissnessname = "Michaels part shop"
                    clientname = name
                    maker(receiptlist,buissnessname,clientname)
                    print("\n your pdf receipt has been made.")
                    print("\n We will attempt to email you the pdf")
                    try:
                        send_mail(email)
                    except Exception as e:
                        print("No email adress was set up")
                        print(e)
                    for j in basket:
                        for i in data:
                            if j == i[id]:
                                quantity = i["quantity"]
                                data.append({"id": id, "quantity": int(quantity)})
                                with open("shop.json", "w") as writefile:
                                    json.dump(data, writefile)
                    print("Thank you for shopping with us")
                                

                    



                        



        
                    
             
def main():
    try:
        print("Welcome to the shop please enter a value to see the selected parts")
        print(" 1. Show all parts \n 2. Shows all CPU \n 3. Shows all RAM \n 4. Shows all Memory\n 5.For checkout")
        choice = int(input("Please enter a value: "))
        categories(choice)
    except Exception as e:
        print(e)
        print("invalid input\n you have been moved to the main menu")
        main()

        



main()