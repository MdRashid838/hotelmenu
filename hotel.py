menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80
}
print("Welcome to my Fast Food Restorent")
print("pizza:40 \npasta:50 \nburger:60 \nsalad:70 \ncoffee:80")

order_total = 0

item_1 = input("Enter your first order :")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} is ordered ")
else:
    print("Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":

    item_2 = input("Enter Your another item :")
    if item_2 in menu :
       order_total += menu[item_2]
       print(f"your second item {item_2} is ordered ")
    else:
       print(f"Ordered Item {item_2} is not available yet")

print (f"Total amount of your order is {order_total}")
    