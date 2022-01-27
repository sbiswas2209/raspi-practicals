def show(limit):
    for i in range(0, limit+1):
        if(i % 2 == 0):
            print(str(i)+" EVEN")
        else:
            print(str(i)+" ODD")
show(int(input("Enter Limit : ")))