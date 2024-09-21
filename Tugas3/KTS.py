# MENCARI KEY
Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
row, col = 26, 26
tabel = [[" " for i in range(col)] for i in range(row)]  # Membuat Tabel Vigenere Cipher

# Mengisi Tabelnya
temp = 0
for i in range(row):
    for j in range(col):
        if j + temp < len(Alpha):
            tabel[i][j] = Alpha[j + temp]
        else:
            tabel[i][j] = Alpha[j + temp - 26]
    temp += 1

# Inputs: 
original_text = "HELLO MY NAME IS KIWA".replace(" ","") 
encrypted_text = "AVFPG WG YLFV CW CSEL".replace(" ","")


# Mencari Keynya
def find_key(original_char, encrypted_char):
    original_index = Alpha.index(original_char) # Menyimpan index huruf original
    for row in range(26):
        if tabel[row][original_index] == encrypted_char: # Mengikuti prinsip Vignere Ciper
            return Alpha[row] # Keluarkan Huruf tersebut
        
# Mencari Keystream, Ex:KEYKEYKEYKEYKE...
KEY = ""
Keystream = ""
for i in range(len(original_text)):
    Keystream += (find_key(original_text[i], encrypted_text[i]))
    
# Mencari Key, Ex : KEY
for i in range(1, len(original_text) + 1):
    Key_Kandidat = Keystream[:i]
    Key_Berulang = (Key_Kandidat * ((len(original_text) // i) + 1))[:len(original_text)] # Agar panjang key kandidat sama dengan original text
    if Key_Berulang == Keystream:
        KEY=Key_Kandidat
        break
    
# MELAKUKAN ENKRIPSI ATAU DEKRIPSI

T = int(input("T: "))
Mode = int(input("Encrypt/Decrypt [0/1]: "))
Final_Kata = []
while T>0:
    M = input().upper()
    keystream = (KEY * ((len(M)//len(KEY))+1))[:len(M)] # Agar Key akan berulang sepanjang M
    if(Mode == 0):
        keyord = list(ord(i) for i in keystream)
    else:
        keyord = list((ord(i)*(-1) for i in keystream)) 
    kata = ""
    
    temp = 0 # Dibutuhkan agar perhitungan saat " " tidak error    
    for i in range(len(M)):
        if(M[i] != " "):
            kata += chr(((ord(M[i]) + keyord[i-temp] - (2*65))%26)+65) # Ord dari M dan keyord akan dijumlahkan lalu dikurang 2*65 agar sesuai dengan huruf abjad, lalu dimodulo 26 agar tidak lebih. terakhir ditambah 65 agar bisa dioperasikan di ascii 
        else:
            kata+=" "
            temp+=1
    Final_Kata.append(kata)
    T-=1
for ans in Final_Kata:
    print(ans)