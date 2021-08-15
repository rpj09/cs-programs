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



def delete():
    f = open("student.dat","rb")
    s = pickle.load(f)
    f.close()
    r = int(input("Enter roll no. whose record to be deleted : "))
    f = open("student.dat","wb")
    print("Successfully deleted!")
    reclst = []
    for i in s :
        if i[0] == r :
            continue
        reclst.append(i)
    pickle.dump(reclst,f)
    f.close()  
    

while True :
    print('Press     For')
    print('  1       create')
    print('  2       display')
    print('  3       delete')
    print('  4       exit')
    ch = int(input('Enter your choice  :  '))
    if ch == 1 :
        create()
    elif ch == 2 :
        read()
    elif ch == 3 :
        delete()
    elif ch == 4:
        break
    else :
        print('ERROR : Invalid choice')
















    
        
        
        
