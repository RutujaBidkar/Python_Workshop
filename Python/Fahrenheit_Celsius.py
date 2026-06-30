
#User input
print("1. Fahrenheit to Celsius")
#print("2. Celsius to Fahrenheit")

choice = int(input("Enter choice: "))

if choice == 1:
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Celsius =", round(c, 2))

elif choice == 2:
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit =", round(f, 2))

else:
    print("Invalid choice")