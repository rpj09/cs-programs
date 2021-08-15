import pickle as pk

def create() :
    sfile = open('student.dat','wb')
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
create()