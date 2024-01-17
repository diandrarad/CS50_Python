def main():
    # Ask user for their name, remove whitespace from str, and capitalize user's name
    name = input("What's your name? ").strip().title()
    print(hello(name))

def hello(to="world"):
    return "hello, {to}"


if __name__ == "__main__":
    main()