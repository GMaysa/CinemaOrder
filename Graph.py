from conn import inupdel, read
from main import cls

def menu_v(): 
    cls() 
    print('+========================================================================+')
    print('|                        PROGRAM PENJADWALAN FILM                        |')
    print('+========================================================================+')

menu = {
    1: 'Masukkan Film',
    2: 'Reset',
    3: 'Exit'
}

def p_menu():
    for key in menu.keys():
        print('', key, '--', menu[key])

def addEdge(adj, v, w):
     
    adj[v].append(w)
    adj[w].append(v) 
    return adj

def greedyColoring(adj, V):
     
    result = [-1] * V
    
    result[0] = 0; # Assign the first color to first vertex

    # A temporary array to store the available colors.
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * V
 
    # Assign colors to remaining V-1 vertices
    for u in range(1, V):
        
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = True
 
        # Find the first available color
        cr = 0
        while cr < V:
            if (available[cr] == False):
                break
             
            cr += 1
             
        # Assign the found color
        result[u] = cr
 
        # Reset the values back to false
        # for the next iteration
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = False
 
    # Print the result
    for u in range(V):
        # print("Vertex", u, " --->  Color", result[u])
        res = str(result[u]+1)
        d = str(u+1)
        sql = ("INSERT INTO cinema_show (filmId, theatreId) VALUES ('"+d+"', '"+res+"')")
        inupdel(sql)

def add():
    v = int(input("Jumlah film : "))

    for i in range(1,v+1):
        cls()
        film = input("Masukkan Judul :")
        d = str(i)
        sql = ("INSERT INTO cinema_film (id_film, nama_film) VALUES ('"+d+"', '"+film+"')")
        inupdel(sql)

    cls()
    g = [[] for i in range(v)]
    h = 0
    for i in range(v-1):
        h+=1
        for j in range(h,v):
            if i != j:
                print("1. jika sama")
                print("0. jika tidak")
                print("Apakah Film -- ",i," = ",j," :")
                n = int(input())
                if n == 1:
                    g = addEdge(g, i, j)
            j+=1
        i+=1

    print("Coloring of graph 1 ")
    greedyColoring(g, v)

def reset():
    sql = "DELETE  FROM cinema_film WHERE id_film > 0"
    inupdel(sql)
    sql = "DELETE  FROM cinema_show WHERE id_show > 0"
    inupdel(sql)
    print("Success..")

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
        if option == 3:
            quit()