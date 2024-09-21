def DP_Win(N,C):
    DP = [0] * (N+1)
    DP[1] = 0
    
    for i in range(2, N+1):
        if((not DP[i-1]) or (i>2 and not DP[i-2]) or (i>5 and not DP[i-5])):
            DP[i] = 1
            
    if DP[N]:
        return "Lala" if C==1 else "Lili"
    else:
        return "Lili" if C==1 else "Lala"

N,C = map(int, input(f"(1) Lala\n(2) Lili \nBalls, First Player: ").split())
print(DP_Win(N,C))