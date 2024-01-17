def convert(text):
    """
    Replaces :) with 🙂 and :( with 🙁 in a string.

    Args:
    text (str): The input string to convert.

    Returns:
    str: The converted string with 🙂 and 🙁 instead of :) and :( respectively.
    """
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    """
    Prompts the user for input, calls the convert function on that input, and prints the result.
    """
    user_input = input("Enter some text: ")
    print(convert(user_input))


# Call the main function to start the program
main()
