import random
import string
import datetime

TEMPLATE = {
    'pk': 'XXXXXX',
    'date_add': 'yyyy-mm-dd',
    'penulis': ' ' * 255,
    'judul': ' ' * 255,
    'tahun': 'yyyy'
}

penulis = input('Penulis: ')
judul = input('Judul: ')
tahun = input('Tahun: ')
data = TEMPLATE.copy()

data['pk'] = ''.join(random.choice(string.ascii_letters) for i in range(6))
data['date_add'] = datetime.datetime.now()