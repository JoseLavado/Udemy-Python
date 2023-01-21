def bond_check(arr):
    bond = [0,0,7]
    agent = [1,2,3]
    arr_len = len(arr)
    x=0

    for i in arr:
        if i == 0 or i == 0 or i == 7:
            agent[x] == i
            x=x+1
        else:
            pass

    if agent == bond:
        print(agent)
        return True
    else:
        print(agent)
        return False

my_nums = [1,0,2,4,0,5,6,7]

result = bond_check(my_nums)

print (result)

a = [7,2,4]
b = [7,2,4]
if a==b:
    print("a equals b")
else:
    print ("a not equals b")

    

