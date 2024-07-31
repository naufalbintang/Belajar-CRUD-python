import os
import CRUD

if __name__ == '__main__':
    sistem_operasi = os.name
    
    match sistem_operasi:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')
    
    print('SELAMAT DATANG DI PROGRAM')
    print('DATABASE PERPUSTAKAAN')
    print('=' * len('SELAMAT DATANG DI PROGRAM'))    
        
        
    # cek database
    CRUD.init_console()
    
    while True:
        match sistem_operasi:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
        
        print('SELAMAT DATANG DI PROGRAM')
        print('DATABASE PERPUSTAKAAN')
        print('=' * len('SELAMAT DATANG DI PROGRAM'))
            
        print('1. Read Data')
        print('2. Create Data')
        print('3. Update Data')
        print('4. Delete Data')
        
        user_option = input('\nMasukkan pilihan: ')
        
        match user_option:
            case '1': CRUD.read_console()
            case '2': print('Create Data')
            case '3': print('Update Data')
            case '4': print('Delete Data')
        
        is_done = input('\nApakah sudah selesai (y/N)? ')
        if is_done.lower() == 'n' or is_done == '':
            pass
        else:
            break

    print('program selesai, makasiii')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        