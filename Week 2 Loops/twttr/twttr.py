input = input("Input :").strip()

for i in input:
    match i.lower():
        case "a" | "e" | "i" | "o" | "u":
            print("", end="")
        case _:
            print(i, end="")
print()