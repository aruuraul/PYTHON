#conditional if else
num1 = int(input("Enter the first no"))
if num1 % 2 ==0:
   print("the no is even")
else:
    print("the no is odd")

#for
for i in range(1,11):
    print(i)

#elif
num2 = int(input("Enter the second no"))
num3 = int(input("Enter the third no"))

if num1 > num3 & num1 > num2 :
    print('num1 is greater')
elif num2 > num1 & num2 < num3 :
    print('num3 is greater')
else :
    print('num 3 is greater')