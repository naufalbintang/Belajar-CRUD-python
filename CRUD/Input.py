def input_tahun():
    while True:
        try:
            hasil = int(input('Tahun\t: '))
            break
        except:
            print('tolong masukkan angka')
    return hasil