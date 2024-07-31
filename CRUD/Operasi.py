from . import Database
from . import Util
import time

def create_first_data():
    penulis = input('Penulis: ')
    judul = input('Judul: ')
    tahun = input('Tahun: ')
    
    data = Database.TEMPLATE.copy()
    
    data['pk'] = Util.random_str(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun
    
    data_str = f'{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('gagal membuat database.')
    
def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print('gagal membaca data')