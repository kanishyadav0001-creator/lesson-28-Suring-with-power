def powerof4(number):
    count = 0

    if (number & (~(number & (number - 1)))):

        while(number > 1):
            number >>= 1
            count += 1

        if(count % 2 ==0):
            return True
        else:
            return False
        
number = int(input("Enter your number :" ))
if(powerof4(number)):
    print(number, "Is a power of 4")
else:
    print(number,"Is not power of 4")    