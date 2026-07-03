num = int(input("Enter a number: "))

i = 2
count = 0

while i <= num:
    if num % i == 0:
        count += 1
    i += 1

if count == 1 and num > 1:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")
