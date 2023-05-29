import random
capitals = {
    'Ukraine': 'Kyiv',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'USA': 'Washington',
    'Canada': 'Ottawa',
    'Switzerland': 'Bern',
    'Austria': 'Vienna',
    'Belgium': 'Brussels',
    'Sweden': 'Stockholm',
    'Norway': 'Oslo',
    'Denmark': 'Copenhagen',
    'Finland': 'Helsinki',
    'Poland': 'Warsaw',
    'Romania': 'Bucharest',
    'Bulgaria': 'Sofia',
    'Greece': 'Athens'
}


def game_country(counter):
    key = random.choice(list(capitals))
    print(f'What is the capital of {key}?')
    guess = str(input(''))
    if guess == capitals[key]:
        print('Correct')
        counter += 1
    else:
        print(f'You are wrong, correct answer is {capitals[key]}')
    print(f'Your points: {counter}')
    return counter


ingame = True
counter = 0


while ingame == True:
    counter = game_country(counter)
    if input('Would you like to try again? Type exit to leave ') == 'exit':
        ingame = False
        print(f"Final score: {counter}")
    else:
        ingame = True
