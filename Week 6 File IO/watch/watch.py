import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r'^<iframe (?:width="\d?\d?\d")? ?(?:height="\d?\d?\d")? ?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)" ?(?:title=".+")? ?(?:frameborder="\d")? ?(?:allow="(?:[^"]+(?:; )?)*")? ?(?:allowfullscreen)?></iframe>$', s):
        return f"https://youtu.be/" + matches.group(1)


if __name__ == "__main__":
    main()