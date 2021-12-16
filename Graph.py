def menu_v():  
    print('+========================================================================+')
    print('|                        PROGRAM PENJADWALAN FILM                        |')
    print('+========================================================================+')

menu = {
    1: 'Masukkan Film',
    2: 'Reset',
    3: 'Exit'
}

def p_menu():
    for key in menu():
        print('', key, '--', menu[key])

def add():
    print()

def reset():
    print()

if __name__=='__main__':
    while(True):
        menu_v()
        p_menu()
        option = ''
        try:
            print('+------+----------------+------------------------------------------------+')
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            add()
        if option == 2:
            reset()