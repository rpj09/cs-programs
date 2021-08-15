import pickle 

def create() :
    sfile = open('student.dat','wb')
    lst = []
    while True :
        roll_no = int(input("Enter your roll no. :   "))
        name = input('Enter your name: ')
        marks = float(input('Enter your marks: '))
        grade = input('Enter your grade: ')
        lst = lst + [[roll_no,name,marks,grade]]
        ans = input("Wanna Enter more(y/n) = ").lower()
        if ans == 'n' :
            break
    pickle.dump(lst,sfile)
    sfile.close()

def read():
    file = open('student.dat','rb') 
    try:
        while True:
            stu=pickle.load(file)
            print(stu)
    except EOFError:
        file.close

def update():
    f = open("student.dat" , "rb+")
    s = pickle.load(f)
    found = 0
    rno = int(input("Enter the roll no. ehose record is to be updated : "))
    for i in s :
        if rno == i[0]:
            print("Current marks are : ",i[2])
            i[2] = int(input("Enter new marks : "))
            found = 1
            break
        if found == 0 :
            print("Recod not found")
    else :
        f.seek(0)
        pickle.dump(s,f)
    f.close()  
    
while True :
    print('Press     For')
    print('  1       create')
    print('  2       display')
    print('  3       update')
    print('  4       exit')
    ch = int(input('Enter your choice  :  '))
    if ch == 1 :
        create()
    elif ch == 2 :
        read()
    elif ch == 3 :
        update()
    elif ch == 4:
        break
    else :
        print('ERROR : Invalid choice')
















    
        
        
        
