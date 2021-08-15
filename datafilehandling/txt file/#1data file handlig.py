def create():
    sfile = open('story.txt','a')
    while True:
        sentence = input('Enter a string: ')
        sfile.write(sentence+'\n')
        user_choice=input('want to enter more values(y/n)')
        if user_choice in "Nn":
            break
    
    sfile.close()


def display():
    try:
        sfile= open("story.txt",'r')
        a = sfile.read()
        print(a)
        sfile.close()
    except FileNotFoundError:
        print('File does not exist')


    

while True :
    print('Press     For')
    print('  1       create')
    print('  2       display')
    print('  3       Exit')
    ch = int(input('Enter your choice  :  '))
    if ch == 1 :
        create()
    elif ch == 2 :
        display()
    elif ch == 3 :
        break;
    else :
        print('ERROR : Invalid choice')
