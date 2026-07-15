#input from the user
n = int(input("Enter the limit of no's :"))
#counter
first = 0
second = 1
for i in range(0,n+1):
    res = first + second
    print(first)
    first = second
    second = res

