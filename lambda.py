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

print ("8888888888888888888888888888888888")

def check_even(nums): return nums%2 == 0




my_num_list=[1,2,3,5,6,7,8,3]

for i in my_num_list:
    print(str(i) + " " + str(check_even(i)))

the_results = filter(check_even, my_num_list)
print(list(the_results))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
a_list =[1,2,3,4]
print(a_list)
print(list(map(lambda i:i**2,a_list)))
print(list(filter(lambda i:i%2==0,a_list)))













