x1, y1 = map(float, input("First Coordinate: ").split())
x2, y2 = map(float, input("Second Coordinate: ").split())

if x1==x2:
    print("Error")
else:  
    slope1 = (y2-y1)/(x2-x1)
    Perpendicular_slope = -1 / slope1

    # Slope 
    print("Slope: ", slope1)

    # Midpoint
    x_mid = (x1+x2)/2
    y_mid = (y1+y2)/2
    print(f"Midpoint: {x_mid, y_mid}")

    # Slope of Perpendicular
    print("Slope of the Perpendicular Bisector: ", Perpendicular_slope)

    # Y-intecpt
    print("Y-intecept of the Perpendicular Bisector: ", )

    # Equation of Perpendicular
    print(f"The equation of the Perpendicular Bisector: y = {Perpendicular_slope}x + ({y_mid - (Perpendicular_slope*x_mid)})")    

