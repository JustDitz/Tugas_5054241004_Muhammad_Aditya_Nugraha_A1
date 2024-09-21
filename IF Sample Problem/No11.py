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