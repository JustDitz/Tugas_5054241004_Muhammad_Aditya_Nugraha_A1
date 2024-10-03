N,R,C = map(int,input().split())
Petak = [[0 for i in range(R)] for i in range(C)]
X = [0]*N
Y = [0]*N

for i in range(N):
    Urutan, Y[i], X[i] = map(int, input().split())
    Petak[Y[i]-1][X[i]-1] = Urutan

for i in range(N):
    if(Petak[Y[i]-1][X[i]-2] != 0 and X[i]-2 >= 0): #Check Kirinya
        print(Petak[Y[i]-1][X[i]-2])
    elif(Petak[Y[i]-1][X[i]] != 0 and X[i] <= C): #Check Kanannya
        print(Petak[Y[i]-1][X[i]])
    else: print("0")
    
# 5 3 3
# 1 1 1
# 2 1 2
# 3 3 3
# 4 2 1
# 5 3 2
