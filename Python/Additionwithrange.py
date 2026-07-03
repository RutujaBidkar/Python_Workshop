start = int(input('Enter a starting number :'))       #getting input from user
end = int(input('Enter a ending number :'))
sum = 0                                               #sum =0
while start <= end:                                 #writing a condition
    sum = sum + start                                #sum addition start
    start = start + 1
print('Sum = ', sum)
