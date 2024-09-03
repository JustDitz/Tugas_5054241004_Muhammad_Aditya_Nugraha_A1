Grade = (input("Enter desired grade > "))
MinAvg = float(input("Enter Minimum Average Required > "))
CurAvg = float(input("Enter Current Average in Course > "))
Poin = float(input("Enter How much the final counts as a percentage of the course grade > "))/100

Answer = (MinAvg-(CurAvg*(1-Poin))) * (1/Poin)
print("You need a score of ", '{0:.2f}'.format(Answer) , "on the final to get a ", Grade)