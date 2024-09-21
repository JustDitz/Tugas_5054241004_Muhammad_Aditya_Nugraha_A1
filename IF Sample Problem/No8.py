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