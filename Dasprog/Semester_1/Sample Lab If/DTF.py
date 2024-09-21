def Dif(Stream_Time, Ali_Time):
    # Stream Time = 1, Ali Time = 2
    
    # Stream Time
    Hour1, Minute1, Second1 = int(Stream_Time[0:2]), int(Stream_Time[3:5]), int(Stream_Time[6:8])
    # Ali Time
    Hour2, Minute2, Second2 = int(Ali_Time[0:2]) -5 , int(Ali_Time[3:5]), int(Ali_Time[6:8])
    
    # calculate
    Second_Dif = Second1 - Second2 
    Minute_Dif = Minute1 - Minute2    
    Hour_Dif = Hour1 - Hour2 
    
    if(Second_Dif < 0):
        Second_Dif += 60 
        Minute_Dif -= 1 
    if(Minute_Dif < 0):
        Minute_Dif += 60 
        Hour_Dif -= 1
        
    # Output
    if(Hour_Dif < 0):
        print("See you on the next Pear Event!")
    else:
        print(f"{Hour_Dif:02}:{Minute_Dif:02}:{Second_Dif:02}")

Time_Live = input("Stream Time [HH:MM:SS]: ")
Ali_Time = input("Ali Time [HH:MM:SS]: ")

Dif(Time_Live,Ali_Time)