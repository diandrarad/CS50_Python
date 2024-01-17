import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        problem = f"{x} + {y} = "
        for _ in range(3):
            answer = input(problem)
            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
                continue
            if answer == result:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {result}")
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()