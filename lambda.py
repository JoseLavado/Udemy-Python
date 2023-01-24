def square(n):
    return n*n

my_nums = [1,2,3,4,5]
#result = square(3)
#print(result)

print(my_nums)
for i in map(square, my_nums):
    print (i)

values =[1,2]

print(list(map(square, [1,2,3,4,5,6,7,8])) ) 

print("********************************************")
def splicer(mystring):
    if len(mystring)%2 ==0:
        return "EVEN"
    else:
        return mystring[0]

names=["Joey","Andy","Peter","Jenn"]        
print(names)
values2=list (map(splicer, names))
print(values2)










