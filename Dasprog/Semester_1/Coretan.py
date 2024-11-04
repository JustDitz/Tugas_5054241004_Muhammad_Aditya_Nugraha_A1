#-----------------------------------------------------
# Fibonacci dengan cache

# import functools
# @functools.cache # Cache bisa diganti dengan dictionary
# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
# n = int(input())
# print(fibo(n))

# ---------------------------------------------------
# Tiling Problem 1xN

# def Ubin_1(n):
#     if n == 1:
#         return 1
#     else:
#         return Ubin_1(n-1)+Ubin_2(n-1)

# def Ubin_2(n):
#     if n < 2:
#         return 0 
#     if n == 2:
#         return 1
#     else:
#         return Ubin_1(n-2)+Ubin_2(n-2)

# N = int(input())
# arr = []
# for i in range(1,N):
#     arr.append(Ubin_1(i) + Ubin_2(i))
    
# print(arr)

# Sizenya 1 x N
# ada ubin dengan panjang 1x2 dan 1x1
# Hitung berapa banyak cara

# ---------------------------------------------------
# Menara Hanoi

# def hanoi(n,start_rod,end_rod):
#     other_rod = 6 - (start_rod + end_rod)
#     if n > 0:
#         hanoi(n-1, start_rod, other_rod)
#         print(f"{n}. Move a Disc from {start_rod} to {end_rod} ")
#         hanoi(n-1, other_rod, end_rod)    

# hanoi(2,1,3)

# ---------------------------------------------------
# Fibonacci dengan Dictionary

# import sys
# sys.setrecursionlimit(100000)
# dict_fibo = {0:1, 1:1}
# def fibo(n):
#     if n <= 1:
#         return 1
#     else:
#         if n in dict_fibo:
#             return dict_fibo[n]
#         else:
#             dict_fibo[n] = fibo(n-1) + fibo(n-2)
#             return dict_fibo[n]
# arr = []
# for i in range(20):
#     arr.append(fibo(i))
# print(arr)

# --------------------------------------------------
# Latihan Rekursi dengan dictionary

# dict_unik = {0:0, 1:1, 2:2}
# def unik(n):
#     if n in dict_unik:
#         return dict_unik[n]
#     else :
#         dict_unik[n] = (n * dict_unik[n-1]) + dict_unik[n-2]
#         return dict_unik[n]
# arr = []

# for i in range(350):
#     arr.append(unik(i))
# print(arr)

# --------------------------------------------------
# Tiling problem 1 x N dengan dictionary
# Ubin 1x1 dan 1x2

# dict_tiling = {1:1, 2:2}

# def tiling(n):
#     if n > 0:
#         if n in dict_tiling:
#             return dict_tiling[n]
#         else:
#             dict_tiling[n] = tiling(n-1) + tiling(n-2)
#             return dict_tiling[n]

# arr = []
# for i in range(1,10):
#     arr.append(tiling(i))

# print(arr)

# -------------------------------------------------
# KPK dan FPB

# def fpb(a,b):
#     if a == 1 or b == 1:
#         return 1
#     elif a == 0:
#         return b
#     elif b == 0:
#         return a
#     else :
#         if(a > b):
#             x = a%b
#             if(x == 0): return b
#             else: return fpb(b,x)
#         else:
#             x = b%a
#             if(x==0): return a
#             else: return fpb(a,x)
                
# def kpk(a,b):
#     return int((a* b)/fpb(a,b))
            
# # intinya pake KPK dan pake FPB
# a,b = map(int, input().split())
# c = kpk(a,b)
# d = fpb(a,b)

# print(c, d)
# ans = int(((c*d)*(a+b))/(a*b))
# print(ans)

# -------------------------------------------------
# Tiling Problem 2 x N dengan ubin 1x2 dan 2x2

# dict_tiling = {1:1, 2:3}
# def tiling(n):
#     if n > 0:
#         if n in dict_tiling:
#             return dict_tiling[n]
#         else:
#             dict_tiling[n] = tiling(n-1) + 2*tiling(n-2)
#             return dict_tiling[n]
        
# for i in range(1,1001):
#     print(f"{i} : ",tiling(i))

# -------------------------------------------------
# Bayangan Lapet

# dict_lapet = {0:0, 1:1, 2:1, 3:2}

# def fibo_lapet(n):
#     if n in dict_lapet:
#         return dict_lapet[n]
#     else:
#         dict_lapet[n] = fibo_lapet(n-1) + fibo_lapet(n-2)
#         return dict_lapet[n]

# n = int(input())
# if fibo_lapet(n) % 2 == 0:
#     v_lapet = fibo_lapet(n)*321
# else:
#     v_lapet = fibo_lapet(n)*123
    
# if v_lapet % 5 == 0:
#     print("AKU TERJEBAK DALAM DUNIAKU")
# else :
#     print("TERIMAKASIH LUPUT TELAH MENJADI PASANGANKU")

# -------------------------------------------------
# Minimal dek

# N,T = map(int, input().split())
# A = list(map(int, input().split()))

# ans = []
# for i in range(T):
#     p, q = map(int, input().split())
#     minimal = 1000000000
#     for i in range(p-1, q):
#         minimal = min(minimal, A[i])
#     ans.append(minimal)

# for i in ans:
#     print(i)

# -------------------------------------------------
# Gimana kalau tiga?

# dict_sim = {0:0, 1:1, 2:2}

# def sim(n):
#     if n in dict_sim:
#         return dict_sim[n]
#     else:
#         dict_sim[n] = sim(n-1) + sim(n-2) + sim(n-3)
#         return dict_sim[n]

# n = int(input())
# ans = []

# for i in range(n+1):
#     ans.append(sim(i)%100)

# for i in range(len(ans)-1,-1,-1):
#     print(ans[i], end=" ")

# -------------------------------------------------
# Analisa pola password

# dict_pass = {1:[1]}
# def len_string(n):
#     if n in dict_pass:
#         return dict_pass[n]
#     else:
#         for i in range(2,n+1):
#             dict_pass[i] = dict_pass[i-1] + [i] + dict_pass[i-1]
#         return dict_pass[i]

# def password(n):
#     for i in len_string(n):
#         if i == n:
#             print("z"*i)
#         elif i % 2 == 1:
#             print("d"*i)
#         else:
#             print("e"*i)

# N = int(input())
# password(N)

# -------------------------------------------------