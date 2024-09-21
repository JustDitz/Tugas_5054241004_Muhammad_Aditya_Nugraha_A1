def Usage(n):
    if(0.0 < n <= 1.0): print("250")
    elif(1.0 < n <= 2.0): print("500")
    elif(2.0 < n <= 5.0): print("1000")
    elif(5.0 < n <= 10.0): print("1500")
    elif(n > 10.0): print("2000")
    else: print("Bad data")

D_Usage = float(input("Data usage in Gbs: "))
Usage(D_Usage)