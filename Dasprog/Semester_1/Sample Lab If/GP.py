x = input("Enter the max jump distance and distance of each pillar: ").split() 
Jump_Distance = int(x[0])
Dis = list(map(int, x[1:]))

if(Jump_Distance >= max(Dis)): print("YES HE CAN")
else: print("NO HE CAN'T")