#Q2)WAP to create a text file story.txt with writelines() and readline() functions
def create():
    sfile = open('story.txt','w')
    l_str = []
    while True:
        sentence = input('Enter a string: ')
        sentence = sentence + '\n'
        l_str.append(sentence)
        user_choice=input('want to enter more values(y/n)')
        if user_choice in "Nn":
            break
    sfile.writelines(l_str)
    
    sfile.close()


def display():
    try:
        a=' '
        sfile= open("story.txt",'r')
        while a:
            a = sfile.readline()
            print(a,end='')
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
