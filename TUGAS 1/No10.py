# No 10
    
# Input
x1, y1 = map(float, input("First Coordinate: ").split())
x2, y2 = map(float, input("Second Coordinate: ").split())

# Slope and Perpendicular Slope
if x1!=x2 and y1!=y2 : 
    slope1 = (y2-y1)/(x2-x1)
    Perpendicular_slope = -1/slope1

# Midpoint
x_mid = (x1+x2)/2
y_mid = (y1+y2)/2
Midpoint = f"{x_mid, y_mid}"

# Y-Intercept
if x1!=x2 and y1!=y2 :
    y_intercept = y_mid-(Perpendicular_slope*x_mid)

# Output

if x1==x2 :        
    y_intercept = y_mid
    print(f"Original Point = {x1,y1} and {x2,y2}\nY = {y_intercept}")      
elif y1==y2 :
    print(f"Original Point = {x1,y1} and {x2,y2}\nX = {x_mid}")
else :
    print(f"Original Point = {x1,y1} and {x2,y2}\nY = {Perpendicular_slope:.2f}x + ({y_intercept:.2f})")