from . import Database
from . import Util
from . import Input
import time
import os

def delete(no_buku):
    try:
        with open(Database.DB_NAME, 'r') as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open('data_temp.txt', 'a', encoding='utf-8') as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print('database error')
    os.rename('data_temp.txt', Database.DB_NAME)

def update(no_buku, pk, date_add, penulis, judul, tahun):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = pk
    data['date_add'] = date_add
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    tahun = str(tahun)    
    
    data_str = f'{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    
    panjang_data = len(data_str)
    
    try:
        with open(Database.DB_NAME, 'r+', encoding='utf-8') as file:
            file.seek(panjang_data * (no_buku - 1))
            file.write(data_str)
    except:
        print('error dalam update data')
    
def create(penulis, judul, tahun):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = Util.random_str(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    
    data_str = f'{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('gagal membuat data')
    

def create_first_data():
    penulis = input('Penulis\t: ')
    judul = input('Judul\t: ')
    tahun = Input.input_tahun()
    
    data = Database.TEMPLATE.copy()
    
    data['pk'] = Util.random_str(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    
    data_str = f'{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('gagal membuat database.')
    
def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if 'index' in kwargs:
                index_buku = kwargs['index'] - 1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print('gagal membaca data')
        return False