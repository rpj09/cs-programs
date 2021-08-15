'''
Q18)#PRAC......WAP to menu driven progrm to do the following:- 
        (a)Create a binary file 'item.dat' consisting of item_id,item_name,price,quantity following format 
            [[121,pen,20,5],[21,pencil,10,10],.....]
        (b)Display the above file
        (c)Add more item details in the existing file
        (d)Display the details of an item for a given item_id
'''



import pickle as pk

def create() :
    sfile = open('item.dat','wb')
    lst = []
    while True :
        irem_id = int(input("Enter the id of item  =  "))
        item_name = input("Enter the name of the item  =  ")
        price = int(input("Enter the price  =  "))
        quantity = int(input("Enter the quantity  =  "))
        lst = lst + [[irem_id,item_name,price,quantity]]
        ans = input("Wanna Enter more(y/n) = ").lower()
        if ans == 'n' :
            break
    pk.dump(lst,sfile)
    sfile.close()


def display() :
    sfile = open('item.dat','rb')
    try :
        while True :
            nst_lst = pk.load(sfile)
            print(nst_lst)
    except EOFError:
        sfile.close()

def display_specific():
    nst_lst = pk.load(sfile)
    for i in nst_lst:
        if i[2]>30:
            print(i)            


def add() :
    sfile = open('item.dat','rb')
    try :
        while True :
            nst_lst = pk.load(sfile)
    except EOFError:
        sfile.close()
    while True :
        irem_id = int(input("Enter the id of item to be added =  "))
        item_name = input("Enter the name of the item to be added  =  ")
        price = int(input("Enter the price to be added  =  "))
        quantity = int(input("Enter the quantity to be added  =  "))
        lst = lst + [[irem_id,item_name,price,quantity]]


create()
display()
