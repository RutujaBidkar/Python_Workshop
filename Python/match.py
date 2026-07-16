x = int(input('Enter a day no '))
if (x ==0) :
    print('Sunday')
elif(x ==1) :
    print('Monday')
elif(x ==2) :
    print('Tuesday')
elif(x ==3) :
    print('Wednesday')
elif(x ==4) :
    print('Thursday')
elif(x ==5) :
    print('Friday')
elif(x ==6) :
    print('Saturday')
else:
    print('Invaild number ')



dayno = int(input('Enter a day no '))
match dayno:
    case 0:
        print('Sunday')
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    break:
print ("Invalid input")
