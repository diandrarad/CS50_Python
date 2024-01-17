import emoji

def emojize(s):
    """
    Converts any codes (or aliases) in s to their corresponding emoji.
    """
    return emoji.emojize(s)

def main():
    """
    Prompts the user for a str in English and outputs the emojized version.
    """
    s = input("Input: ")
    print("Output:", emojize(s))

if __name__ == '__main__':
    main()