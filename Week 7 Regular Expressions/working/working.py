import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    matches = re.search(r"^([0-9][0-2]*):*([0-5][0-9])* ([A-P]M) to ([0-9][0-2]*):*([0-5][0-9])* ([A-P]M)$", s)
    if not matches:
        raise ValueError

    start_hr, start_min, start_ampm, end_hr, end_min, end_ampm = matches.groups()
    start_hr, end_hr = int(start_hr), int(end_hr)
    if start_hr > 12 or end_hr > 12:
        raise ValueError

    if start_ampm == "PM" and start_hr != 12:
        start_hr += 12
    elif start_ampm == "AM" and start_hr == 12:
        start_hr = 0

    if end_ampm == "PM" and end_hr != 12:
        end_hr += 12
    elif end_ampm == "AM" and end_hr == 12:
        end_hr = 0

    start_min = int(start_min) if start_min else 0
    end_min = int(end_min) if end_min else 0

    start_time = f"{start_hr:02}:{start_min:02}"
    end_time = f"{end_hr:02}:{end_min:02}"
    return f"{start_time} to {end_time}"


if __name__ == "__main__":
    main()
