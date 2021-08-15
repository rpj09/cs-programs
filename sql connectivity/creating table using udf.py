import mysql.connector as m

connection=m.connect(host='localhost',user = 'root',passwd='',database='xaviers')
mycursor=connection.cursor()

def create_table():
    try:
        creating_table="create table if not exists Attributes(GAMEN0 int primary key,NAME varchar(20),no_of_players int);"
        mycursor.execute(creating_table)
        print('Table created')
    except Exception as e :
        print(e)

def insert_rows():
    try:
        user_choice= input('Do you want to insert more records(y/n)? ')
        while user_choice in 'Yy':
            gameno=int(input('enter gameno.  :'))
            name =input(str('enter name:'))
            no_of_players=int(input('enter no. of players'))
            inserting_values=(f"insert into Attributes values({gameno},'{name}',{no_of_players})")
            mycursor.execute(inserting_values)
            user_choice=input('Do you want to insert more records(y/n)? ')
            if user_choice in 'Nn':
                break
        connection.commit()

    except Exception as e:
        print(e)

def display_all():
    try:
        print('Table Game as follows:')
        mycursor.execute('select * from game;')
        myrecords = mycursor.fetchall()
        for x in myrecords:
            print(x)
    except Exception as e:
        print(e)


#MAIN PROGRAM

while True:
    print('1. To create table')
    print('2. To insert rows in the table')
    print('3. To display all the rows of the table')
    print('4. To exit')
    choice=int(input('Enter your choice b/w 1-4 : '))
    if choice==1:
        create_table()
    elif choice==2:
        insert_rows()
    elif choice==3:
        display_all()
    elif choice==4:
        print('Thankyou')
        break
    else:
        print('Wrong choice,try again')
        continue

        
        

     
