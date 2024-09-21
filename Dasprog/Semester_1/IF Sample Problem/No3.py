def fun1 ():
    x = input("[T/F] : ")
    if x == "T" : return 1
    else : return 0

def fun2 () :
    print("fun2 executed")
    return 1

print("Testing &&")
if fun1() and fun2():
    print("Test of && complete") 

print("Testing ||")    
if fun1() or fun2():
    print("Test of || complete")