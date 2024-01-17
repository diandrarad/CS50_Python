import datetime

def main():
    while True:
        # Prompt user for date input
        date_str = input("Date: ").strip()

        try:
            # Parse the date string into a datetime object
            date = parse_date(date_str)
        except ValueError:
            # Invalid date input, try again
            continue

        # Convert datetime object to YYYY-MM-DD string format
        formatted_date = date.strftime("%Y-%m-%d")

        # Output formatted date
        print(formatted_date)
        break

def parse_date(date_str):
    """
    Parses a date string in either "month day, year" or "month/day/year"
    format into a datetime object.
    """
    for format_str in ["%B %d, %Y", "%m/%d/%Y"]:
        try:
            date = datetime.datetime.strptime(date_str, format_str)
            return date
        except ValueError:
            pass

    # If we get here, the input is not a valid date
    raise ValueError("Invalid date format")

if __name__ == '__main__':
    main()
