##Q2) WAP to create a table game (game no, name , no_of_players) and insert rows in it using  user defined functions create_tabe() and insert_rows()
##Manasvi,Ripunjay


import mysql.connector as my

mydb=my.connect(host='localhost',user='root',passwd='',database='xaviers')
mycursor=mydb.cursor()

def create_table() :
     try:
          sql_command = "create table if not exists game (game_no integer primary key , name varchar(20) not null , no_of_players integer)"
          mycursor.execute(sql_command)
          print('Table created')
     except Exception as e:
          print(e)

def insert_rows() :
     try :
          while True :
               game_no = int(input('Enter the game number  =  '))
               name = input('Enter the name of game  =  ')
               no_of_players = int(input('Enter the number of players  =  '))  
               sql_command = (f"insert into game values({game_no},'{name}',{no_of_players})")
               mycursor.execute(sql_command)
               user_choice = input('Want to enter more values(y/n)  : ')
               if user_choice in 'Nn' :
                    break
     except Exception as e:
          print(e)

def display():
          mycursor.execute("select * from game")
          myrecords = mycursor.fetchall()
          c = mycursor.rowcount
          if c == 0 :
               print('Not Found')
          else :
               print('\n')
               print('Game No.'.ljust(15), 'Game Name'.ljust(10),'No. of Player'.ljust(10))
               for x in myrecords :
                    print('\n',end='')
                    for i in x:
                         print(str(i).ljust(15) , end = '|')
                         

while True:
    print('1. To create table')
    print('2. To insert rows in the table')
    print('3. To display all the rows of the table')
    print('4. To exit')
    choice=int(input('Enter your choice b/w 1-5 : '))
    if choice==1:
        create_table()
    elif choice==2:
        insert_rows()
    elif choice==3:
        display()
    elif choice==4:
        print('Thankyou')
        break
    else:
        print('Wrong choice,try again')
        continue