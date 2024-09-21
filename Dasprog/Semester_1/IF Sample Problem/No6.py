X, Y = map(float,input("X and Y Coordinate: ").split())
Format_X = f'{X:.1f}'
Format_Y = f'{Y:.1f}'

if(X == 0 and Y == 0):
    print(f"({Format_X} , {Format_Y}) is in the middle")
elif(X == 0):
    print(f"({Format_X} , {Format_Y}) is on the Y-axis")
elif(Y == 0):
    print(f"({Format_X} , {Format_Y}) is in the X-axis")
elif(X > 0 and Y > 0):
    print(f"({Format_X} , {Format_Y}) is in quadrant I")
elif(X < 0 and Y > 0):
    print(f"({Format_X} , {Format_Y}) is in quadrant II")
elif(X < 0 and Y < 0):
    print(f"({Format_X} , {Format_Y}) is in quadrant III")
else:
    print(f"({Format_X} , {Format_Y}) is in quadrant IV")
    