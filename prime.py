num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       print(i)   
       if (num % i) == 0:
           print("******")
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is nota prime number")


print("*******************************************************************")
for n in range(2, 10):
    print("n is = " + str(n)) 
    for x in range(2, n):
        print("n is = " + str(n) + " x is = " + str(x)) 
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')