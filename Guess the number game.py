import random 

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print('Welcome to guess the number game!')
    print('I have selected a number between 1 to 100. Can you guess it?')
    print('Type "q" or "quit" to quit.')

    while True:
        user_input = input('Enter your guess:  ').strip().lower()
        if user_input in ['q', 'quit']:
            print("Thanks! goodbye.")
            break
        try:
            guess = float(user_input)
            attempts += 1

            if guess < number_to_guess:
                print('Too low..Try again.')
            elif guess > number_to_guess:
                print('Too high. Try again.')
            else:
                print(f'Congrats! You have guessed in {attempts} attempts.' )
                break
        except ValueError:
            print('Invalid input.Please enter an integer.')

if __name__ == "__main__":
    guess_the_number()
         

            
         