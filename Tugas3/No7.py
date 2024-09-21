cmd, K = map(int, input("Cmd [1/2] & K: ").split()) # 1 Encrypt 2 Decrypt, Pergeseran
if(cmd == 2): K*=(-1) # Pergesannya mundur

while True: # Selalu berjalan selama ada input
  try: 
    cek = str(input())
    x1 = list(ord(i) for i in cek) # Dari huruf jadi ASCII
    Limit = K % 26 # Sesuai dengan jumlah alpabet
    kata = ""

    for i in range(len(x1)):
      if((cek[i].isupper() and ((x1[i]+Limit)>90)) or (cek[i].islower() and ((x1[i]+Limit) > 122))) : x1[i] -= 26 # Agar tetap dalam rentang Alfabet
      if(cek[i].isalpha()): # Apabila selain huruf tidak dieksekusi
        kata += chr(x1[i]+Limit) # Dari ASCII ke Huruf
      else:
        kata+=cek[i]
    print(kata)
  except EOFError: # Ctrl+Z Enter agar berhenti
    break