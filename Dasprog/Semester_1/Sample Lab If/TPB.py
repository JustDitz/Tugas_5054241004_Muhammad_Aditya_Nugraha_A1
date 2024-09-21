import math
def Prime_Checker(n):
    x = math.ceil(math.sqrt(n))+1 # Pembulatan ke atas dari akar nilai n
    if n > 2:
        for i in range(2, x):
            if(n%i==0):
                return "IT IS NOT A PRIME"
    
    return "IT IS A PRIME"
    

Num = int(input("Number: "))
print(Prime_Checker(7))