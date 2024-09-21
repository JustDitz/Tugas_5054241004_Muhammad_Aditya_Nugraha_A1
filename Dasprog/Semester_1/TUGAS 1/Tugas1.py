import math
Soal = int(input("Soal no: "))

match Soal: 
    case 2:
        # No 2
    
        Flow, Gravity, Height = float(input("Enter the Flow: ")) * 1000, 9.80, float(input("Enter the Height ")) 
        print(f"{'{0:.5f}'.format(Flow*Gravity*Height*0.9/1000000)} MW")    

    case 4:
        # No 4

        USD = float(input("Currency in US Dollar: "))
        print("Currency in Pound", USD * 0.65) # 1 USD = 0.65 Pound

    case 6:
        # No 6

        Grade = (input("Enter desired grade > "))
        MinAvg = float(input("Enter Minimum Average Required > "))
        CurAvg = float(input("Enter Current Average in Course > "))
        Poin = float(input("Enter How much the final counts as a percentage of the course grade > "))/100

        Answer = (MinAvg-(CurAvg*(1-Poin))) * (1/Poin)
        print(f"You need a score of {Answer:.2f} on the final to get a {Grade}")

    case 8:
        # No 8

        Population = int(input("Enter the Community's Population: "))
        print(f"Magnitude: {((math.ceil(Population/3))*2*14)}L/Day\nCost of Water Saved: {((math.ceil(Population/3))*150)}$")

    case 10:
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
        Midpoint = (x_mid, y_mid)

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
     
    case 12:
        # No 12
        
        # Input
        Speed = float(input("Jet's takeoff speed: ")) * (1000 / 3600) 
        Distance = float(input("Distance of an aircraft-carrier: "))
        
        # Main
        Acceleration = (pow(Speed, 2) / (2*Distance))
        Time = Speed / Acceleration
    
        # Output
        print(f"Acceleration: {Acceleration:.2f} m/s^2")
        print(f"Time: {Time:.2f} seconds")
    case _:
        print("Invalid!")