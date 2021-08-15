''' Q4)Write a program using interface between Python and MySQL to do the following : [5]	                                                                           									
       a) Create the given table ORDERS with the given structure 
       b) To add records in the given table by taking values from user at run.
       c) Delete a record from table for a given order number. 
       d) Display all the records of the table
  (Manasvi,ripunjay) '''



import mysql.connector as my


mydb=my.connect(host='localhost',user='root',passwd='',database='xaviers')
mycursor=mydb.cursor()


def create_table() :
     try:
          sql_command = ("create table if not exists ORDERS (Order_no integer(10) primary key ,\
                                                    Client_name varchar(30) ,\
                                                    client_location varchar(30) ,\
                                                    Orders integer(10) ,\
                                                    Payments integer(10)")                                                    
          mycursor.execute(sql_command)
     except Exception as e:
          print(e)

def insert() :
     try :
          while True :
               Order_no = int(input('Enter the order number  =  '))
               Client_name = input('Enter the Client name  =  ')
               client_location = input('Enter the location of client  =  ')
               Orders = int(input('Enter the number of orders  =  '))
               Payments = int(input('Enter the amount of payments  =  '))
               sql_command = f"insert into game values({Order_no},'{Client_name}','{client_location}',{Orders},{Payments})"
               mycursor.execute(sql_command)
               user_choice = input('want to enter more values(y/n)  : ')
               if user_choice in 'Nn' :
                    break
     except Exception as e:
          print(e)
     


def delete() :
     try :
          order_no = int(input('Enter the order number for which the record is to be deleated  =  '))
          sql_command = (f"delete from employee where Order_no = {order_no}")
          mycursor.execute(sql_command)
     except Exception as e:
          print(e)


def display() :
     try:
          sql_command = ("select * from ORDERS")
          mycursor.execute(sql_command)
          myrecords = mycursor.fetchall()
          c = mycursor.rowcount
          if c == 0 :
               print('Not Found')
          else :
               print('Order_no'.ljust(15), 'Client_name'.ljust(15),'client_location'.ljust(15),'Orders'.ljust(15),'Payments'.ljust(15))
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
    print('4. To delete rows of a given order no.')
    print('5. To exit')
    choice=int(input('Enter your choice b/w 1-5 : '))
    if choice==1:
        create_table()
    elif choice==2:
        insert()
    elif choice==3:
        display()
    elif choice==4:
        delete()
    elif choice==5:
        print('Thankyou')
        break
        mydb.close()
    else:
        print('Wrong choice,try again')
        continue

mydb.close()
