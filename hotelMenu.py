menu = {
    'Coffee' : 30 ,
    "Biriyani" : 90,
    "Pasta" : 40,
    "Momo" : 50,
    "Golgappa" : 20,
    "Soup" : 30
}

print("Welcome to Chira's Restaurant.")
print(" Coffee : 30\n Biriyani : 90\n Pasta : 40\n Momo : 50\n Golgappa : 20\n Veg Soup : 30")

bill = 0

item = input("Enter the item you want to Order : ")
if item in menu :
    bill += menu[item]
    print(f"Your item {item} has been addeed to your order.")
else:
    print(f"Ordered item {item} is not available yet.")

while True :
    ans = input("Do you want to order another item ? (Yes/No)")
    if (ans == 'Yes') :
        item2 = input("Enter the item you want to order : ")
        if item2 in menu :
            bill += menu[item2]
            print(f"Your item {item2} has been added to your order.")
        else : 
            print (f"Ordered item {item2} is not available yet.")
    elif (ans == 'No') :
        break
    else :
        print ("Please write Yes or No.")

print(f"The total amount of item to pay is Rs {bill}")
    
