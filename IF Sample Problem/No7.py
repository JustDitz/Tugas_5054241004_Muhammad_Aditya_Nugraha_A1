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