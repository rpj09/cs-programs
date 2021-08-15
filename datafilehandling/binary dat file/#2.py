import pickle

def create_file():
    file = open('student.dat','wb')
    while True:
        roll = int(input('Enter your roll no: '))
        name = input('Enter your name: ')
        marks= float(input('Enter your marks: '))
        grade= input('Enter your grade: ')
        stud_rec= [roll,name,marks,grade]
        pickle.dump(stud_rec,file)
        user_choice=input('Do you want to enter more records: ')
        if user_choice in 'Nn':
            break
    file.close()

def read():
    file = open('student.dat','rb')
    user_in=(input('Enter grade of which you want to display details: ')).lower() 
    try:
        while True:
            stu=pickle.load(file)
            if stu[-1].lower() == user_in:
                print(stu)
    except EOFError:
        file.close
    
while True :
    print('Press     For')
    print('  1       create')
    print('  2       display')
    print('  3       Exit')
    ch = int(input('Enter your choice  :  '))
    if ch == 1 :
        create_file()
    elif ch == 2 :
        read()
    elif ch == 3 :
        break;
    else :
        print('ERROR : Invalid choice')
















    
        
        
        
