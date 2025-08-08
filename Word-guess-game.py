import random


def welcome():
    '''
    Display the welcome message.
    '''
    print("Welcome to the game!")
    print("We have one word, and you should guess it letter by letter.")
    print("You have only 6 chances to guess the whole word, or you will lose.")
    print("So be careful!")

def user_letter():
    '''
    Get a single alphabet letter from the user.
    Keep asking until the input is valid.
    '''
    while True:
        letter = input("Enter your letter: ").lower()
        if len(letter) > 1 or not letter.isalpha():
            print("Please enter one alphabet letter.")
            continue
        else:
            return letter
        
def random_word():
    '''
    Pick a random word from a list of fruit names.
    '''
    words = ['apple','banana','lemon','orange','mango','peach','kiwi','avocado']
    pick = random.choice(words)
    return pick

def check(random_word, user_letter, state):
    '''
    Check if the user's letter exists in the word.
    If so, update the state with the correct letter.
    '''
    update = False
    for i in range(len(random_word)):
        if user_letter == random_word[i] and state[i] == '_':
            state[i] = user_letter
            update = True
            print("Correct!")
    return state, update


def update_status(update, chance):
    if not update:
        chance -= 1
        print("Wrong guess!")

    return chance


def win(state):
    '''
    Check if the player has won.
    '''
    if '_' not in state:
        print("You won!")
        return True
    return False

def lose(chance):
    '''
    Check if the player has lost.
    '''
    if chance == 0:
        return True
    return False

# call welcome function.

def main():


    welcome()
    chance = 6
    word = random_word()
    state = ['_'] * len(word)
    print("word is:", " ".join(state))



    # main loop 
    while chance > 0:   
        print(f"You have {chance} chances left to guess the word...")
        
        user = user_letter()
        state , update = check(word, user,state)
        print(' '.join(state))
        chance = update_status(update, chance)
        
        if win(state):
            print(f"The word was: {word}")
            break


        if lose(chance):
            print(f"Game over! You ran out of chances. The word was:{word}")
            break




if __name__ == "__main__":
    main()