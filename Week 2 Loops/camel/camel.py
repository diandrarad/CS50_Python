user_input = input("camelCase: ")

for i in user_input:
    if i.isupper():
        print(f"_{i.lower()}", end="")
    else:
        print(i, end="")
print("")