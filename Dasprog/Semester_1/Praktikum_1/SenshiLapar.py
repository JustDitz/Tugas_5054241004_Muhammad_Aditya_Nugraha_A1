size_x,size_y = map(int, input().split())
x,y = map(int, input().split())
m = int(input())

# Berapa kali pengecekan
if((x==0 and y==0) or (x==0 and y ==size_y) or (x==size_x and y==0) or (x==size_x and y==size_y)):
    Petak = 3
elif((x==0 ) or (x==size_x) or (y==0) or (y==size_y)):
    Petak = 5
else:
    Petak = 8
     
if(m==1):
    x1,y1 = map(int,input().split())
    if (x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
elif(m==2):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
elif(m==3):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
        print("x1")
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
        print("x2")
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
        print("x3")
elif(m==4):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
elif(m==5):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
elif(m==6):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    x6,y6 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
    if(x6+1 == x or x6-1 == x) or (y6+1 == y or y6-1 == y):
        Petak-=1
elif(m==7):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    x6,y6 = map(int,input().split())
    x7,y7 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
    if(x6+1 == x or x6-1 == x) or (y6+1 == y or y6-1 == y):
        Petak-=1
    if(x7+1 == x or x7-1 == x) or (y7+1 == y or y7-1 == y):
        Petak-=1
elif(m==8):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    x6,y6 = map(int,input().split())
    x7,y7 = map(int,input().split())
    x8,y8 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
    if(x6+1 == x or x6-1 == x) or (y6+1 == y or y6-1 == y):
        Petak-=1
    if(x7+1 == x or x7-1 == x) or (y7+1 == y or y7-1 == y):
        Petak-=1
    if(x8+1 == x or x8-1 == x) or (y8+1 == y or y8-1 == y):
        Petak-=1
else:
    Petak = 0

# Output
print(Petak)
if Petak>0:
    print("Senshi makan hari ini!")
else:
    print("Senshi makannya besok aja deh.")
print(Petak)
# Misal senshi di 
# 2,4

# 5 M8 F  F  F     M3
# 4    F  S  F     
# 3 M2 F  F  F     M7
# 2                 
# 1 M5       M6    
# 0 M1       M4    
#   _0 _1 _2 _3 _4 _5 

# FREE : (1,5) (2,5) (3,5) (1,4) (3,4) (1,3) (2,3) (3,3)
# (1,0) (0,3) (5,5) (3,0) (1,1) (3,1) (5,3) (0,5)
# Expected : "Senshi makan hari ini!"
# Output AC : "Senshi makannya besok aja deh."

# Menuju X = 2 dan Y = 4
# Bandingkan dengan codemu di coretan.py

# 5 5 
# 2 4
# 8
# 1 0
# 0 3
# 5 5
# 3 0
# 1 1
# 3 1
# 5 3
# 0 5