# Mengecek tanda dari 2 angka
def Cek_Simbol(a,b):
    if(a<0 and b<0):
        return "Neg"
    elif(a>0 and b>0):
        return "Pos"
    elif( (a<0 and b>0) or (a>0 and b<0)):
        return "YES"

# Menentukan di index berapa nilai 0 atau perubahan tanda terjadi
def BinSearch(arr,low,high):
    if high>=low :
        mid = (high+low) // 2
        if arr[mid] == 0 or Cek_Simbol(arr[mid],arr[mid-1]) == "YES": # Apabila nilai 0 atau perubahan tanda terjadi
            return mid                                                
        elif Cek_Simbol(arr[mid], arr[mid+1]) == "YES":               # Apabila perubahan terjadi antara angka saat ini dan setelahnya
            return (mid+1)
        elif Cek_Simbol(arr[mid], arr[mid+1]) == "Pos":               # Apabila kedua angkanya masih bernilai positif
            return BinSearch(arr,low,mid-1)                           # Melakukan Searching lagi, tetapi dibelah jadi dua (ke bawah)
        else:
            return BinSearch(arr,mid+1,high)                          # Apabila kedua angkanya masih bernilai negatif maka dibelah jadi dua (ke atas)
    else: high        
    
N,M = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
P_Total = C_Total = 0

P.sort()
C.sort()

# Bagian P
if(Cek_Simbol(P[0],P[N-1]) == "Pos"):
    for i in range(len(P)):
        P_Total+= P[i]
elif(Cek_Simbol(P[0],P[N-1]) == "Neg"):
    P_Total = P[N-1]
else:
    for i in range(BinSearch(P,0,N),N):
        P_Total += P[i]

# Bagian C
if(Cek_Simbol(C[0],C[N-1]) == "Pos"):
    C_Total = C[0]
elif(Cek_Simbol(P[0],P[N-1]) == "Neg"):
    for i in range(len(C)):
        C_Total += C[i]
else:
    for i in range(0,BinSearch(C,0,M)):
        C_Total += C[i]
    
print(C_Total-P_Total)