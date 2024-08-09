from . import Operasi
from . import Input

def delete_console():
    read_console()
    while True:
        print('Silakan pilih nomor buku yang akan dihapus')
        no_buku = Input.input_no_buku()
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][-1]
            
            # data yang ingin dihapus
            print('\n' + '=' * 100)
            print('Data yang ingin anda hapus')
            print(f'1. Penulis {penulis:.40}')
            print(f'2. Judul {judul:.40}')
            print(f'3. Tahun {tahun:4}')
            
            is_done = input('\nApakah anda yakin(y/N)? ')
            if is_done.lower() == 'n' or is_done == '':
                pass
            elif is_done.lower() == 'y':
                Operasi.delete(no_buku)
                break
            else:
                print('Input tidak valid, silakan masukkan lagi.')
        else:
            print('Nomor tidak valid, silakan masukkan lagi')
    print('Data berhasil dihapus')

def update_console():
    read_console()
    while True:
        print('Silakan pilih buku yang akan diupdate')
        no_buku = Input.input_no_buku()
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print('Nomor tidak valid, silakan masukkan lagi')
            
    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    while True:
        # data yang ingin diupdate
        print('\n' + '=' * 100)
        print('Silahkan pilih data yang ingin anda ubah')
        print(f'1. Penulis\t: {penulis:.40}')
        print(f'2. Judul\t: {judul:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        
        # memilih mode untuk update
        user_option = input('Pilih data (1, 2, 3): ')
        match user_option:
            case '1': penulis = input('Penulis\t: ')
            case '2': judul = input('Judul\t: ')
            case '3': tahun = Input.input_tahun()
            case _: print('index tidak cocok')
        
        print('Data baru anda')
        print(f'1. Penulis\t: {penulis:.40}')
        print(f'2. Judul\t: {judul:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        
        is_done = input('\nApakah data sudah sesuai (y/N)? ')
        if is_done.lower() == 'n' or is_done == '':
            pass
        else:
            break
        
        Operasi.update(no_buku, pk, date_add, penulis, judul, tahun)
        
def create_console():
    print('\n\n' + '=' * 100)
    print('Silakan tambah data buku\n')
    penulis = input('Penulis\t: ')
    judul = input('Judul\t: ')
    tahun = Input.input_tahun()
    
    Operasi.create(penulis, judul, tahun)
    print('Berikut adalah data baru anda')
    read_console()
    

def read_console():
    data_file = Operasi.read()
    index = 'No'
    penulis = 'Penulis'
    judul = 'Judul'
    tahun = 'Tahun'
    
    # header
    print('=' * 100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    print('-' * 100)
    
    # data
    for index, data in enumerate(data_file, 1):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f'{index:4} | {judul:.40} | {penulis:.40} | {tahun:5}', end='')
    
    # footer
    print('=' * 100)
    
