import random
import string

def random_str(panjang):
    hasil = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil