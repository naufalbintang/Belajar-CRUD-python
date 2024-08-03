def input_tahun():
    while True:
        try:
            hasil = int(input('Tahun\t: '))
            break
        except:
            print('tolong masukkan angka')
    return hasil

def input_no_buku():
    while True:
        try:
            hasil = int(input('Nomor buku: '))
            break
        except:
            print('Tolong masukkan nomo buku yang valid')
    
    return hasil
