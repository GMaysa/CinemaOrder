import os #header function clean and pause
from conn import read

# SQL
# HOW TO USE INUPDEL
# sql = "INSERT or UPDATE or DELETE something from tabel"
# inupdel(sql)

# HOW TO USE READ
# sql = "SELECT * FROM tabel"
# data = read(sql)
# for data in data:
#     print(data)

#fungsi clean
def cls():
    os.system('pause')
    os.system('cls')


#head menu pertama
def menu_visual():  
    print('+========================================================================+')
    print('|                          MENU CINEMA ORDER                             |')
    print('+========================================================================+')

#head isi menu pertama
menu_options = {
    1: 'Jadwal Film',
    2: 'Pesan Film',
    3: 'Exit',
}

#fungsi panggil isi menu pertama
def print_menu():
    for key in menu_options.keys():
        print ('', key, '--', menu_options[key] )

#fungsi isi graph penjadwalan film
def graph():
     print('Masukin metode graph')

#fungsi isi queue untuk entry tiket
def queue():
     print('Masukin metode queue')

#menu pertama
if __name__=='__main__':
    while(True):
        menu_visual()
        print_menu()
        option = ''
        try:
            print('+------+----------------+------------------------------------------------+')
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            graph()
            cls()
        elif option == 2:
            queue()
            cls()
        elif option == 3:
            print('Thanks, the program is exiting')
            cls()
            exit()
        else:
            print('Invalid option. Try to input again!')
            cls()
