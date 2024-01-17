def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Plate must contain between 2 and 6 characters
    if not 2 <= len(s) <= 6:
        return 0

    # No periods, spaces, or punctuation marks are allowed
    elif not all(i.isalnum() for i in s):
        return 0

    # Plate must start with at least two letters
    elif not s[0:2].isalpha():
        return 0

    # Numbers cannot be used in the middle of the plate and the first number used cannot be 0
    for i in s:
        if i.isdigit():
            index = s.index(i)
            if s[index:].isdigit() and i != "0":
                return 1
            else:
                return 0

    return 1


main()