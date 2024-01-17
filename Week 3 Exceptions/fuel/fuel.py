def main():
    while True:
        fraction = get_fraction("Fraction: ")
        if fraction <= 100:
            break

    if fraction >= 99:
        print("F")
    elif fraction <= 1:
        print("E")
    else:
        print(f"{fraction}%")


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            return round(int(x)/int(y)*100)
        except (ValueError, ZeroDivisionError):
            pass


main()