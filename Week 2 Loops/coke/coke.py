coin = 0
while coin < 50:
    user_input = int(input("Insert Coin: "))
    if user_input == 5 or user_input == 10 or user_input == 25:
        coin += user_input
        if coin == 50:
            print("Change Owed:", 0)
        else:
            print("Amount Due:", 50 - coin)
    else:
        print("Amount Due: 50")

if coin > 50:
    print("Change Owed:", coin - 50)