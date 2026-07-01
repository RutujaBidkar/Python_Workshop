text = input("Enter a string: ")

reverse = ""
i = len(text) - 1

while i >= 0:
    reverse = reverse + text[i]
    i -= 1

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")