a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)
#
#
#
#
a = int(input())
b = int(input())
c = int(input())
if a > b:
    print(a)
else:
    print(b)
    if c > b:
        print(c)
    else:
        print(b)
        #
        #
        #
        #
        num1 = input()
num2 = input()
num3 = input()
if num1 == num2 and num1 == num3 and num3 == num2:
    print(0)
elif num1 == num2 or num1 == num3 or num3 == num2:
    print(1)
elif num1 != num2 and num2!=num3 and num1!=num3:
    print(3)
    