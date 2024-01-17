from datetime import date
import sys

def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    age = age_in_minutes(birth_date)
    print(age_in_words(age))

def age_in_minutes(birth_date):
    delta = date.today() - birth_date
    return round(delta.total_seconds() / 60)

def number_to_words(num):
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    words = ""

    if num >= 1000000:
        words += number_to_words(num // 1000000) + " million, "
        num %= 1000000

    if num >= 1000:
        words += number_to_words(num // 1000) + " thousand, "
        num %= 1000

    if num >= 100:
        words += ones[num // 100] + " hundred "
        num %= 100

    if num >= 10 and num < 20:
        words += teens[num - 10]
    else:
        if num >= 20:
            words += tens[num // 10] + ("" if num % 10 == 0 else "-")
            num %= 10
        if num > 0:
            words += ones[num]

    return words.strip()


def age_in_words(age_in_minutes):
    return (number_to_words(age_in_minutes)).capitalize() + " minutes"



if __name__ == "__main__":
    main()