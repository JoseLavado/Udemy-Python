from random import shuffle

#initial list order
mylist = [" ","O"," "]

#Shuffle list fn
def shuffle_list(list_mod):
    shuffle(list_mod)
    return list_mod
    
#player chooses where ball is
def player_guess():
    guess = "3"
    while guess not in ["0","1","2"]:
        guess = input ("Pick a number: 0, 1 or 2: ")
    return int(guess)

def check_guess(mix_list, index):
    if mix_list[index] == "O":
        print ("Correct")
    else:
        print ("Wrong guess")
    return mix_list
    
#shuffle list before game
mixed_list = shuffle_list(mylist)
#player guesse
player_pick = player_guess()
#check guess
result = check_guess(mixed_list, player_pick)
print (result)

