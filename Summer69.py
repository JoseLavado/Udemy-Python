my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

def sum69(thelist):
  ADD=True
  Total=0

  for i in thelist:
    if (i==6):
        ADD=False
    Total = Total+i


  return Total

print(sum69(my_list))

