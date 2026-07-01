string = input("Enter a string: ")

i = len(string) - 1
reverse = ""

while i >= 0:
    reverse = reverse + string[i]
    i -= 1

print("Reversed string:", reverse)