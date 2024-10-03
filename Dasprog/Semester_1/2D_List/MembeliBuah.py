N,K = map(int, input().split())
A = list(map(int, input().split()))
Kemungkinan = 0
Buah = []

for i in range(N):
    if (A[i] <= K):
        Kemungkinan+=1
        Buah.append(i+1)

print(Kemungkinan)

print(f"Dengan uang {K} ia bisa membeli dengan kemungkinan {Kemungkinan} jenis buah yaitu buah",end=" ")
for i in range(len(Buah)):
    print(f"jenis ke-{Buah[i]},",end="")
    
# 5 1000
# 1000 2000 500 400 3000