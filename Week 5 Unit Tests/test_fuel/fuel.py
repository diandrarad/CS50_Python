def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error:", e)

    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
    except ValueError:
        raise ValueError("Invalid fraction format")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    percentage = round(x / y * 100)

    if not (0 <= percentage <= 100):
        raise ValueError("Percentage must be between 0 and 100")

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
