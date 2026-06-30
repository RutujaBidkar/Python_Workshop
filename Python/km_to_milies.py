#user input
value = float(input("Enter value: "))

#option to choose user
print("1. KM to Miles")
print("2. Miles to KM")

#After choose option
choice = int(input("Choose 1 or 2: "))


if choice == 1:
    print("Miles =", value / 1.6)

elif choice == 2:
    print("KM =", value * 1.6)

else:
    print("Invalid choice")