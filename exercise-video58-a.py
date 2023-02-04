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



