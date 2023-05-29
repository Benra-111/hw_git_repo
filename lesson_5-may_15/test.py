balance = int(1000)

def transaction()->int:

    def deposit ()-> int:
        balance_1 = balance + amount
        return balance_1
    
    def withdrawal ()->int:
        balance_1 = balance - amount
        return balance_1
    
    while True:
        try:
            amount = int(input("Enter an amount you whant to operate with: "))
            type_of_transaction = input("Enter what type of operation\
 you would like to do, either 'd' for deposit or a 'w' for withdrawal: ")
            global balance
            if type_of_transaction == 'w':
                if balance < amount:
                    print(f"Invalid index! You don't have enough money. ({(amount - balance)})")
                else:
                    balance = withdrawal()
                break
            elif type_of_transaction == 'd':
                balance = deposit()
                break
        except ValueError:
            print("Invalid input! Please enter correct request.")
    print ( balance )
    

#print(f'Your balance: {transaction()}')
while True:
    print(balance)
    transaction()