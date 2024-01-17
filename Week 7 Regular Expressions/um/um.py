import re


def main():
    print(count(input("Text: ").strip()))


def count(s):
    return len(re.findall(r"\b[U-u]m\b", s))


if __name__ == "__main__":
    main()