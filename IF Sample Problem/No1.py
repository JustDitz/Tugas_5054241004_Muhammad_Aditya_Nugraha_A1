Purchase = float(input("Total Purchase: "))
Status = input("Are you a student? [Y/N] ")
Total = 0

if(Status == "Y"):
    Total = ((Purchase-(Purchase*0.2)) + (Purchase-(Purchase*0.2))*0.05)
    print('{0:.2f}'.format(Total))
else :
    Total = (Purchase+(Purchase*0.05))
    print('{0:.2f}'.format(Total))