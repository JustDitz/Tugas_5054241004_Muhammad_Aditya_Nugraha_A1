# a,b = map(int, input().split())
# print(a+b)

def fpb(a,b):
    if a == 1 or b == 1:
        return 1
    else :
        if(a > b):
            x = a%b
            if(x == 0): return b
            else: return fpb(b,x)
        else:
            x = b%a
            if(x==0): return a
            else: return fpb(a,x)
                
def kpk(a,b):
    return int((a* b)/fpb(a,b))
            
# intinya pake KPK dan pake FPB
a,b = map(int, input().split())
c = kpk(a,b)
d = fpb(a,b)

ans = int(((c*d)*(a+b))/(a*b))
print(ans)