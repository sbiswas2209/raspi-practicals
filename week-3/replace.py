list = [1,2,3,4,5,6]
temp = list[0]
list[0] = list[len(list)-1]
list[len(list)-1] = temp
print(list)