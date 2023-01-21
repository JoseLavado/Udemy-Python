def bond_check(arr):
    bond = [0,0,7]
    agent = [9,9,9]
    arr_len = len(arr)
    x=0
    print (arr) 

    for i in arr:
        if i == 0 or i==7:
            print("i is "+str(i))  
            agent[x]=i
            x=x+1
        
    if agent == bond:
        print(bond)
        print(agent)
        return True
    else:
        print(bond)
        print(agent)
        return False

my_nums = [1,0,0,17,274,8,5,6,8,3,3,3,3,3,8]

result = bond_check(my_nums)

print (result)

print("-----------------")

def spy_game(nums):
    code = [0,0,7,"x"]
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code)==1

print(spy_game(my_nums))


    

