n = int(input('Enter a number'))           #getting input from user
c =0                                        #counter
while(n>0):
  c=c+1
  n = n // 10
print('Total Number of Digits', c)

