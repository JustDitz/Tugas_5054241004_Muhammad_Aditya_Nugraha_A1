x1, y1 = map(int, input().split()) # Titik Pusat
xs, ys = map(int, input().split()) # Titik awal
xf, yf = map(int, input().split()) # Titik akhir

Start_End = ((xf-xs)**2 + (yf-ys)**2) # Jarak dari start ke tujuan
Center_End = ((xf-x1)**2 + (yf-y1)**2) # Jarak dari pusat ke tujuan

if Start_End < Center_End:
    print("Yes")
else:
    print("No")