from random import randint

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def main():
    number = randint(1, get_level())
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == number:
                print("Just right!")
                sys.exit()
            elif guess > number:
                print("Too large!")
            else:
                print("Too small!")
        except ValueError:
            pass

main()