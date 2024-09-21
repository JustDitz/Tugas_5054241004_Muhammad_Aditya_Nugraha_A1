def Traffic(M,N,T):
    # M Front, N Behind, T Time
    Total_Cars = M+N+1
    Passed_Car = 0
    
    while(T > 0):
        T -= 25
        x = 12 # Supaya hanya 12 mobil yang bisa lewat (60/5)
        
        # Counting Cars Passing the Traffic Light
        while(T>=5 and x > 0 and Passed_Car < Total_Cars):
            Passed_Car +=1
            T-=5
            x-=1
    
    Total_Cars -= Passed_Car

    if(Passed_Car>=(M+1)):
        print(f"YES! {Total_Cars}")
    else:
        print(f"NO! {Total_Cars}")
        
M,N,T = map(int, input("Cars in front of you, Cars behind you, Second: ").split())
Traffic(M,N,T)