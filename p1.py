import random

def generate_random_number():
    return random.randint(100,999)

def get_user_guess():
    while True:
        guess=input('enter a three-digit number: ')
        if guess.isdigit() and len(guess)==3:
            return int(guess)
        else:
            print('number is invalid')
def play_game():
    number_to_guess=generate_random_number()
    attempts=6

    print('welcome to play')
    print('i have select 3digit num.you have 6 attemps to guess it')

    for attempt in range(attempts):
        guess=get_user_guess()
        if guess == number_to_guess:
            print('congtatulations you win in {attempt + 1} attempts')
            break
        elif guess < number_to_guess:
            print('is too low')
        else:
            print('is too high.')
 
        remaining_attempts=attempts - (attempt + 1)
        print('you have {remaining_attempts} left')
    else:
    
       print('sorry you are loser')
