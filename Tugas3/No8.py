N,M,K = map(int, input("N,M,K: ").split())  # Ada berapa Lantai, Kekuatan Gaem, Berapa Kasus
Power = list(map(int, input("Power: ").split()))
Data_Power = 0

while K>0:
    X,Y = map(int, input("X,Y: ").split())
    
    for i in range(X,Y):
        Data_Power += Power[i-1] # Menghitung Total Power yang Dibutuhkan
    K-=1

if(M >= Data_Power):
    print(f"EZ banget, energiku sisa {M-Data_Power}!")
else:
    print(f"NT, kurang {Data_Power-M} energi sih.")