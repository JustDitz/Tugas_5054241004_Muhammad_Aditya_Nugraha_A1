R,C,N = map(int, input().split())
Tambang = [[0 for _ in range(R)] for _ in range(C)]
Wrong = X = Y = 0

for i in range(R):
    Tambang[i] = list(map(int,input().split()))
Emas = Tambang[X][Y]

Command = input()

for i in Command:
    if(i == 'R' and (X+1)<C):
        X+=1
        Emas += Tambang[X][Y] + 3
    elif(i == 'L'and (X-1)>=0):
        X-=1
        Emas += Tambang[X][Y] - 2
    elif(i == 'U' and (Y+1)>=0):
        Y-=1
        Emas += Tambang[X][Y] + 3
    elif(i == 'D' and (Y-1)<R):
        Y+=1
        Emas += Tambang[X][Y] - 2
    else:
        Wrong = 1
        break
    
print(Emas)       
if Wrong:
    print("gerakanmu salah bung!")

# 4 4 5
# 1 1 1 2 
# 2 2 3 1
# 3 4 5 7
# 7 2 2 2
# RDLLLU