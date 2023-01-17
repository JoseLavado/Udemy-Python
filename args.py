#lesson 49

def func(a,b):
    # return 5% of sum
    return sum((a,b))*0.05

def myargs(*args):
    print(args)
    for n in range(len(args)):
        print(args[n])


a=40
b=60
value=func(a,b)
print(f"the sum of {a} and {b} is {a+b} and its 5% is {value}")
 
myargs(1,3,5,7,9)


def pickfruit(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print(f"my fruit is {kwargs['fruit']}")

        
pickfruit(fruit="apples")




