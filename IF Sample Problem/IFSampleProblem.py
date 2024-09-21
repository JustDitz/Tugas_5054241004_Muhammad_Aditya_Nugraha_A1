Soal = input("Soal: ")
match Soal:
    case 1:
        # Soal no 1
        
        Purchase = float(input("Total Purchase: "))
        Status = input("Are you a student? [Y/N] ")
        Total = 0

        if(Status == "Y"):
            Total = ((Purchase-(Purchase*0.2)) + (Purchase-(Purchase*0.2))*0.05)
            print('{0:.2f}'.format(Total))
        else :
            Total = (Purchase+(Purchase*0.05))
            print('{0:.2f}'.format(Total))
    case 2:
        # Soal no 2
        
        wt_lb = float(input("Weight in Pound: "))
        ht_in = float(input("Height in Inches: "))
        BMI = round((703 * wt_lb) / (pow(ht_in, 2)), 1)

        if BMI < 18.5 :
            print("Underweight")
        elif BMI >= 18.5 and BMI < 25 :
            print("Normal")
        elif BMI >= 25 and BMI < 30 :
            print("Overweight")
        else:
            print("Obese")
    case 3:
        # Soal no 3
        
        def fun1 ():
            x = input("[T/F] : ")
            if x == "T" : return 1
            else : return 0

        def fun2 () :
            print("fun2 executed")
            return 1

        print("Testing &&")
        if fun1() and fun2():
            print("Test of && complete") 

        print("Testing ||")    
        if fun1() or fun2():
            print("Test of || complete")            
    case 4:
        # Soal no 4
        
        Fl_CyColor = str(input("First letter of Clylider Color: ")).lower()
        Fl_CyColor = Fl_CyColor[0]

        match Fl_CyColor:
            case "o":
                print("ammonia")
            case "b":
                print("carbon monoxide")
            case "y":
                print("hydrogen")
            case "g":
                print("oxygen")
            case _ :
                print("Contents unknown")
    case 5:
        # Soal no 5
        
        def Usage(n):
            if(0.0 < n <= 1.0): print("250")
            elif(1.0 < n <= 2.0): print("500")
            elif(2.0 < n <= 5.0): print("1000")
            elif(5.0 < n <= 10.0): print("1500")
            elif(n > 10.0): print("2000")
            else: print("Bad data")
        
        D_Usage = float(input("Data usage in Gbs: "))
        Usage(D_Usage)
    case 6:
        # Soal no 6
        
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
    case 7:
        # Soal no 7
        
        def leap_year(x):
            if((x%4 == 0 and x%100 != 0) or (x%100 == 0 and x%400 == 0)):
                return 1
            else:
                return 0

        def Day_Count(D, M, Y):
            Day_each_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if(leap_year(Y)):
                Day_each_Month[1] = 29

            Day_Num = D
            for i in range(M-1):
                Day_Num += Day_each_Month[i]

            return Day_Num

        def Month_Name(M):
            Name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            return(Name[M-1])

        Day = int(input("Day [1-31]: "))
        Month = int(input("Month [1-12]: "))
        Year = int(input("Year: "))

        print(f"{Day} {Month_Name(Month)} {Year} is day {Day_Count(Day, Month, Year)}") 
    case 8:
        # Soal no 8
        
        print("(1) First Free Service")
        print("(2) Second Free Service")
        Service = int(input("Enter the Free Service number>> "))
        Miles = int(input("Enter number of Miles>> "))

        if(Service == 1):
            if(1500<Miles<=3000):
                print("Vehicle must be serviced")
            else:
                print("Vehicle does not need to be serviced yet")
        else:
            if(3001<Miles<=4500):
                print("Vehicle must be serviced")
            else:
                print("Vehicle does not need to be serviced yet")
    case 9:
        # Soal no 9
        
        WM = int(input("Weekday Minute: "))
        NM = int(input("Night Minute: "))
        WNM = int(input("Weekend Minute: "))
        
        Cost = 3999
        if(WM > 600): Cost+=((WM-600)*40)
        
        print(f"Weekday Minute: {WM}")
        print(f"Night Minute: {NM}")
        print(f"Weekend Minute: {WNM}")
        print(f"Pretax Bill: {round(Cost/100)}$")
        print(f"Average Minute Cost: {round((WM+NM+WNM/Cost)/100)}$")
        Taxes = round((Cost*5.25)/10000)
        print(f"Taxes: {Taxes}$")
        print(f"Total Bill: {round(Cost/100)+Taxes}$")
    case 10:
        # Soal no 10
        
        def Baking_Time(Bread_Type, Double, Manual):
            if Bread_Type == "W":
                Time = [15, 60, 18, 20, 2, 75, 45, 30]
            else :
                Time = [20, 60, 33, 30, 2, 75, 35, 30]
                
            if Double:
                for i in range (len(Time)):
                    Time[i] *= 1.5
            
            Step = ["Primary kneading: ", "Primary rising: ", "Secondary kneading: ", "Secondary rising: ", 
                    "Loaf shaping: ", "Final rising: ", "Baking: ", "Cooling: "]
            for i in range (len(Step)):
                print(f"{Step[i]} {Time[i]} Minute" if i != 4 else f"{Step[i]} {Time[i]} Seconds")
                
                if (Manual and i == 4):
                    print("Remove the dough for manual baking")    
                    break        
                
        Bread_Type = input("Bread type [W for white S for sweet]: ").upper()
        Double = input("Is the loaf size double [T/F]: ").upper() == "T"
        Manual = input("Is the baking manual [T/F]: ").upper() == "T"
        
        Baking_Time(Bread_Type, Double, Manual)
    case 11:
        # Soal no 11
        
        def within_x_percent(ref, subs, x):
            low = ref - (ref*x/100)
            up = ref + (ref*x/100)
            return 1 if low <= subs <= up else 0

        def Observe(ask):
            Ref = {"Water": 100, "Mercury": 357, "Copper":1187, "Silver":2193, "Gold":2660}
            flag = 0
            for Subs,Value in Ref.items():
                if within_x_percent(Value, ask, 5):
                    print(Subs)
                    flag = 1
                    break
            else: print("Substance unknown") 

        Boiling_Point = float(input("Enter the observed boiling point (°C): "))
        Observe(Boiling_Point)