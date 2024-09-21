U = int(input()) # HP Ucup
K = int(input()) # Banyak Knight
M = int(input()) # Banyak Minion

Damage_Taken = (M//2) * 2 + (5 * (K//2))*5 + 1000

if(U-Damage_Taken >= 0):
    print(f"Yey! Ucup Menang! HP tersisa: {U-Damage_Taken}")
else:
    print("Yah! Ucup Meninggoy.")