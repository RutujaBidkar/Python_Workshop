#getting input from user
n = int(input("Enter a number: "))

sum =0   #Acts like a counter
r =0      #Counter as reminder
while (n > 0):
    r = n % 10
    sum = sum + r
    n = n//10
print('Sum of digit is', sum)
