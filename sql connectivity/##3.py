'''Q3 Write a program using interface between Python and MySQL to do the following :	
1)To create a table game1 in MySQL.
2)Add records in it by taking values from user at run time.
3)To display all students who have got a particular grade given by user
(Manasvi,ripunjay)'''


import mysql.connector as my


mydb=my.connect(host='localhost',user='root',passwd='',database='xaviers')
mycursor=mydb.cursor()

def create_table() :
     try:
          sql_command = "create table if not exists game11(roll_no integer primary key,\
                                                    Class integer ,\
                                                    Name varchar(20) not null,\
                                                    game1 varchar(20),\
                                                    Grade varchar(20) not null)"
          mycursor.execute(sql_command)
     except Exception as e:
          print(e)


def insert_rows() :
     try :
          while True :
                    Name = input('Enter the name of player  =  ')
                    Class = int(input('Enter the class  =  '))
                    roll_no = int(input('Enter the roll number  =  '))
                    game1 = input('Enter the game1 of player  =  ')
                    Grade = input('Enter the grade of player  =  ') 
                    sql_command = f"insert into game1 values({roll_no},{Class},'{Name}','{game1}','{Grade}')"
                    mycursor.execute(sql_command)
                    user_choice = input('want to enter more values(y/n)  : ')
                    if user_choice in 'Nn' :
                         break
          mydb.commit()
               
     except Exception as e:
          print(e)



def display() :
     try:
          grade = input(' Enter the grade for which the students are to be displayed  = ')
          sql_command = (f"select * from game1 where Grade='{grade}' ")
          mycursor.execute(sql_command)
          myrecords = mycursor.fetchall()
          c = mycursor.rowcount
          if c == 0 :
               print('Not Found')
          else :
               print('roll_no'.ljust(15), 'Class'.ljust(15),'Name'.ljust(15),'game1'.ljust(15),'Grade'.ljust(15))
               for x in myrecords :
                    print('\n',end='')
                    for i in x :
                         print(str(i).ljust(15) , end = '|')              
     except Exception as e :
          print(e)                                            


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
        display()
    elif choice==4:
        print('Thankyou')
        mydb.close()  
        break
    else:
        print('Wrong choice,try again')
        continue