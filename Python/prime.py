#input from the user
n = int(input("Enter the no's :"))
#counter
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if (count == 2):
    print(" Prime NUM")
else:
    print("NOT Prime NUM")
