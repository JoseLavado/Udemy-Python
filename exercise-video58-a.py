print("####################################################")
def sphere_vol(radius):
    return (4/3)*3.14159*(radius**3)

result = sphere_vol(2)
print(f'The volume of the sphere with radius 2 is {result}')

print("####################################################")
def num_chk(num,low,high):
    if num>low and num <high:
        return True

result = num_chk(2,1,3)
print(f'the number 2 is between 1 and 3 is {result}')

print("####################################################")
def up_low(word):
    d = {"upper":0, "lower":0} # a dictionary to hold the values
    for char in word:
        if char.isupper():
            d["upper"]+=1
        elif char.islower():
            d["lower"]+=1
        else:
            pass
    print(f'orginal sentence is {word}')
    print(f'number of upper letters is: {d["upper"]}')
    print(f'number of lower letter is: {d["lower"]}')

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

print("####################################################")
my_list = [1,1,1,1,1,3,3,4,4,4,4,4,5,5,5,5,5]
#print(list(set(my_list)))
uniq = []
for item in my_list:
    if not(item in uniq):
        uniq.append(item)
    else:
        pass
print(f'the original is {my_list}')
print(f'the uniq list is {uniq}')

print("####################################################")
my_list=[1,2,3,-4]
def mult(my_list):
    result=1
    for i in my_list:
        result=result*i
    return result

answer= mult(my_list)    
print(f'answer is {answer}')





    