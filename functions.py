"""
Author: Jose Lavado
Date: Jan 15, 2023
Note: create functions
"""

print("Hello, this is a function exanple")


def hello5x():
    for i in range(5):
        print(f"hello no. {i}")

def sayHello(name="Mike"):
    """
    This function receives name var and says hello back
    """
    print(f"Hello {name} how are you?")

def sumofnums(a,b):
    return a+b

hello5x()
sayHello("Jose")
sayHello("Bella")

a=3
b=5
result=sumofnums(a,b)

print(f"The sum of {a} and {b} is {result}")
sayHello()


def check_even_list(lista):
    elist=[]
    for i in lista:
        if i % 2 ==0:
            elist.append(i)
        else:
            pass
    return elist    

check = check_even_list([1,3,4,6,8,7,9,10])
print(check)





