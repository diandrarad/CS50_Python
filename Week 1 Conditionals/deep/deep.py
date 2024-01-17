# Prompts the user for the answer to the Great Question of Life
user_input = input("What? ").lower().strip()

# Output Yes if the user inputs 42 or forty-two or forty two. Otherwise output No.
match user_input:
    case "forty two" | "forty-two" | "42":
        print("Yes")
    case _:
        print("No")