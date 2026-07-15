#input from the user
n = int(input("Enter the no  :"))
#counter
ctr = 1
for i in range(1,n+1):
    if(n%i==0):
        print('Factors Are :' ,i)

