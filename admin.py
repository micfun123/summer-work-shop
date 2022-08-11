from calendar import c
import json


with open("shop.json", "r") as readfile:
    data = json.load(readfile)

def main():
    print("Add a new item to the shop")
    print("1. Add a new item")
    print("2. remove an item")
    print("3. show all item amounts")

    choice = int(input())
    

    if choice == 1:  
        print ("Enter the model of the item?")
        model = input()
        price = input("What is the price? please use the format xx.xx\n")
        name = input("What is the type of the item?\n")
        quantity = int(input("How many are there?\n"))
        id = len(data) + 1
        data.append({"id": id, "model": model, "price": float(price), "type": name, "quantity": int(quantity)})
        with open("shop.json", "w") as writefile:
            json.dump(data, writefile)
        print("Item added")
        again = input("Do you want to add another item or remove another item?\n")
        if again == "yes":
            main()
        else:
            exit()
    elif choice == 2:
        for i in data:
            model = i["model"]
            price = i["price"]
            type = i["type"]
            id = i["id"]
            quantity = i["quantity"]
            print(f"{id}: \n")
            print(f"The {type} is a {model} at the price of {price}. you have {quantity} left\n\n")
            
        print ("Enter the model of the item that you want to remove?")
        ID = int(input())
        for i in data:
            if i["id"] == ID:
                data.remove(i)
                with open("shop.json", "w") as writefile:
                    json.dump(data, writefile)
                print("Item removed")
                again = input("Do you want to add another item or remove another item?\n")
                if again == "yes":
                    main()
                else:
                    exit()
    elif choice == 3:
        print("Here is a list of all the items in the shop")
        for i in data:
            model = i["model"]
            price = i["price"]
            type = i["type"]
            id = i["id"]
            quantity = i["quantity"]
            print(f"{id}: \n")
            print(f"The {type} is a {model} at the price of {price}. you have {quantity} left\n")

        
main()