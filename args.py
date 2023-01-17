def func(a,b):
    # return 5% of sum
    return sum((a,b))*0.05

def myargs(*args):
    for n in range(len(args)):
        print(args[n])


a=40
b=60
value=func(a,b)
print(f"the sum of {a} and {b} is {a+b} and its 5% is {value}")
 
myargs(1,3,5,7,9)


