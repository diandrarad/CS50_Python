list = []
while True:
    try:
        name = input("Name: ").strip().title()
    except EOFError:
        print()
        break
    if name:
        list.append(name)

num_names = len(list)
print("Adieu, adieu, to ", end="")
if num_names == 1:
    print(list[0])
elif num_names == 2:
    print(f"{list[0]} and {list[1]}")
else:
    name_list = ", ".join(list[:-1])
    print(f"{name_list}, and {list[-1]}")
