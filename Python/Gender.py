gender = str(input('Enter Gender :'))
if(gender=='f' or gender=='F'):
    print('Female')
elif gender=='m' or gender=='M':
    print('Male')
else:
    print('Not Applicable')


BillAmount = int(input('Enter Bill Amount :'))
if (BillAmount < 5000):
    print('10% discount')
elif(BillAmount > 5000) or (BillAmount < 10000):
    Print('20% Discount')
elif(BillAmount >= 10000):
    print('25 Discount')
