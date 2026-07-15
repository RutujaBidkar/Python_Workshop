#input from the user
n = int(input("Enter the limit of no's :"))
#Counter
sum=1
for i in range(1,n+1):
    sum *= i
print('sum is : ',sum )