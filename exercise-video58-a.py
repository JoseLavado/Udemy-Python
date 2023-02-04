###################################################
def sphere_vol(radius):
    return (4/3)*3.14159*(radius**3)

result = sphere_vol(2)
print(f'The volume of the sphere with radius 2 is {result}')

#################################################
def num_chk(num,low,high):
    if num>low and num <high:
        return True

result = num_chk(2,1,3)
print(f'the number 2 is between 1 and 3 is {result}')

####################################################
def up_low(s):
    up=0
    low=0
    for i in s:
        if i.isupper() == True:
            up=up+1
        elif i.islower() == True:
            low=low+1
        else:
            pass
    print(f'upper letters are = {up}')
    print(f'lower letters are {low}')

up_low("AB A AA bb bbbb")






