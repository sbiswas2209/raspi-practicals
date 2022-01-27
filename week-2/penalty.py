def calc(speed):
    if speed <= 70:
        print("OK")
    else:
        penalty = (speed-70)/5;
        print("Penalty :", int(penalty))
        if(penalty > 12):
            print("License Suspended")
calc(int(input("Enter speed : ")))