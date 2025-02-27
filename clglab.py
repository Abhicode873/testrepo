for i in range(1, 5):
    print("#" * i)

for i in range(1,5):
    print("*" * i)


#WAP to calculate factorial of number
num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= num 
    num =  num-1

print("Factorial:", fact)

n = int(input("Enter a number: "))
fact=1
i=1
for i in range (1,n+1):
    fact *= i
print("Factorial:", fact)

#WAP to print num from 1 to 100 which are only divisble by 
for num in range(1, 101):
    if num % 5 == 0:
        if num % 10 == 0:
            pass  
        if num % 3 == 0:
            pass
        else:
            print(num)

for num in range(1, 99):
        if num % 3 == 0:
            pass
        else:
            print(num)

#DESIGN TH EPROGRAM TO TAKE THE USER INPUT AND ADDS THE ELEMENT UNTIL THE USER INPUT IS 999
totalsum = 0

while True:
    num = int(input("Enter a number (999 to stop): "))
    if num == 999 or num== -1:
        break
    totalsum += num

print("Sum of entered numbers:", totalsum)



#DESIGN A PROGRAM FOR A PERSON TRAVELLING THOROUGOUT INDIA MON TO SATURDAY AND GOES HOME ONLY SAT AND SUN
#DESIGN A PROGRAM FOR A CUSTOMER WHO VISIT BANKS AND WITHDRAWS EVERY ONE HOUR IF HE GOES WITHIN withdrwal 
 
 
# DESIGN A PROGRAM IN FIBONACCI FOR 0112358 for first 10 terms     
# Number of terms
  
a, b = 0, 1

print("Fibonacci Sequence:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b




#design to take two user inputs find the product of those until user inputs a value -1  
while True:
    num1 = int(input("\nEnter first number (-1 to stop): "))
    if num1 == -1:
        break
    num2 = int(input("Enter second number (-1 to stop): "))
    if num2 == -1:
        break
    else:
      product = num1 * num2
      print("Product:", product)

a = float(input("enter the first num:"))
b = float(input("enter the second num:"))
print("avg=", (a + b)/2)

a = int(input("enter the first num:"))
b = int(input("enter the second num:"))
print(a >=b) 

    