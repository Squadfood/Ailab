print("Water jug problem")

# Initial capacities of jugs
x = int(input("Enter capacity of X jug: "))
y = int(input("Enter capacity of Y jug: "))

while True:
    rno = int(input("Enter the rule number (1-12): "))
    
    # Rule implementation
    if rno == 1:
        x = 4
    elif rno == 2:
        y = 3
    elif rno == 3:
        d = int(input("Enter how much water from X: "))
        if 0 < d <= x:
            x -= d
    elif rno == 4:
        d = int(input("Enter how much water from Y: "))
        if 0 < d <= y:
            y -= d
    elif rno == 5 or rno == 12:
        x = 0
    elif rno == 6:
        y = 0
    elif rno == 7:
        if x + y >= 4 and y > 0:
            x, y = 4, y - (4 - x)
    elif rno == 8:
        if x + y >= 3 and x > 0:
            x, y = x - (3 - y), 3
    elif rno == 9 or rno == 11:
        if x + y <= 4 and y > 0:
            x, y = x + y, 0
    elif rno == 10:
        if x + y <= 3 and x > 0:
            x, y = 0, x + y
            
    print("X =", x)
    print("Y =", y)
    
    # Check if goal state is reached
    if x == 2:
        print("Reached goal state")
        break
