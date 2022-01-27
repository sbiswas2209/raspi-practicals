def divisible(a):
    if a % 3 == 0 and a % 5 == 0:
        print("Three Five")
    elif a % 3 == 0:
        print("Three")
    elif a % 5 == 0:
        print("Five")
    else:
        print(a)


divisible(int(input("Enter Number : ")))
