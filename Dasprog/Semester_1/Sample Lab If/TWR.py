def Answer(a,b,c,d):
    # a = cat, b = amount, c = jump, d = index
    for i in range(c):
        x = a[len(a)-b:] 
        a = x+a
        del a[len(a)-b:]
    
    print(a[d[0]], a[d[1]], a[d[2]])
        
Cat = list(map(int,input("Cats Number: ").split()))
Amount_Cat = int((input("Amount of cat that will jump: ")))
Jump = int(input("How many times cat will jump: "))
Index = list(map(int, input("Index: ").split()))
 
Answer(Cat,Amount_Cat,Jump,Index)

# def Answer(a,b,c,d):
#     # a = cat, b = amount, c = jump, d = index
#     x = c % len(a)
    