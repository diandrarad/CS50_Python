def main():
    time = input("What time is it? ")
    decimal_time = convert(time)

    if decimal_time <= 8 and decimal_time >= 7:
        return print("breakfast time")
    elif decimal_time <= 13 and decimal_time >= 12:
        return print("lunch time")
    elif decimal_time <= 19 and decimal_time >= 18:
        return print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)

    minute = minute / 60
    return hour + minute;


if __name__ == "__main__":
    main()