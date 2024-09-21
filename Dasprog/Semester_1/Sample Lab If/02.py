n = int(input("N: "))
final_kata = ""
for i in range(n):
    x = int(input("Xi: "))
    binary_n = bin(x)[2:].zfill(32)
    listbin = [binary_n[0:8], binary_n[8:16], binary_n[16:24], binary_n[24:32]]
    des = [int(listbin[0], 2), int(listbin[1], 2), int(listbin[2], 2), int(listbin[3], 2)]
    kata = ''   
    kata = kata + chr(des[0]) + chr(des[1]) + chr(des[2]) + chr(des[3])
    final_kata+=kata
print(final_kata)