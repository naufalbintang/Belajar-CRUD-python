from . import Operasi

DB_NAME = 'data.txt'
TEMPLATE = {
    'pk': 'XXXXXX',
    'date_add': 'yyyy-mm-dd',
    'penulis': ' ' * 255,
    'judul': ' ' * 255,
    'tahun': 'yyyy'
}


def init_console():
    try:
        with open(DB_NAME, 'r') as file:
            print('database ditemukan')
    except:
        print('database tidak ditemukan, silakan buat database baru.')
        Operasi.create_first_data()