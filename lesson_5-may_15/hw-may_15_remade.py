#%%
def enter ()-> str:
    return input('Enter the integer: ')

def recieve () -> int:
    while True:
        try:
            a = enter()
            b = int(a) 
            break
        except ValueError:
            print('Try again, it doesn\'t seems like an integer.')
    return b


input_value = recieve()

print("Input is integer: ", input_value)

 # %%
def input_():
    string = str(input("Enter a string: "))
    n = input("Enter an integer: ")
    return string, n


def print_character():
    while True:
        try:
            string, n = input_()
            n = int(n)
            character = string[n]
            print("Character at index", n, "is:", character)
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")
        except IndexError:
            print("Invalid index! The string does not have a character at index", n)


print_character()
# %%
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
            if type_of_transaction == 'd':
                bal = deposit()
                return bal
            elif type_of_transaction == 'w':
                if balance < amount:
                    print(f"Invalid index! You don't have enough money. ({(amount - balance)})")
                else:
                    bal = withdrawal()
                    return bal
        except ValueError:
            print("Invalid input! Please enter correct request.")
    

print(f'Your balance: {transaction()}')
# %%
from random import randint

def roll_the_dice()->int:
    return randint(1,6)

amount_of_ = [0,0,0,0,0,0]
for i in range(1000):
    a = roll_the_dice()
    amount_of_[a-1] += 1
for i in range(1, 7):
    print( f'{i} showed {amount_of_[i-1]} times.')
# %%
from random import randint

def receive_input():
    number_ = int(input('Enter the number of regions: '))
    rating_ = [0] * number_
    for i in range(number_):
        rating_[i] = int(input(f'Enter the rating of candidate in region{i+1}: '))
    return number_, rating_

def simulate_region_election(j):
    first_ = 0
    for i in range (10000):
            a = randint(1, 100)
            if a < rating_first[j]:
                first_ += 1
    print(f'Region {j+1}: {first_} voted for 1st candidate, \
{10000 - first_} voted for 2nd candidate.')
    return first_

def simulate_election ():
    all_first_votes = 0
    for j in range (number_):
        all_first_votes += simulate_region_election(j)
    return all_first_votes

def calculate_result (all_first_votes):
    all_votes = 10000 * number_
    result_ = (all_first_votes * 100) / all_votes
    if result_ > 50:
        first_won = 1
    else:
        result_ = (100 - result_)
        all_first_votes = all_votes - all_first_votes
        first_won = 2
    return result_, all_first_votes, first_won

def announce_result ():
    print(f'Result: {first_won} candidate won with {all_first_votes} \
votes and {round(result_, 1)}% of all votes')

number_, rating_first = receive_input()

all_first_votes = simulate_election()

result_, all_first_votes, first_won = calculate_result(all_first_votes)

announce_result()



# %%
