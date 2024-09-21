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