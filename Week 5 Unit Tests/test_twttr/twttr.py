def main():
    word = input("Input :").strip()
    print(shorten(word))


def shorten(word):
    shorten_word = []
    for i in word:
        match i.lower():
            case "a" | "e" | "i" | "o" | "u":
                shorten_word.append("")
            case _:
                shorten_word.append(i)
    return "".join(shorten_word)


if __name__ == "__main__":
    main()