#to retrieve and display all the employees working in a given department

import mysql.connector as m

connection=m.connect(host='localhost',user = 'root',passwd='',database='xaviers')
mycursor=connection.cursor()
empno = int(input("Enter department number: "))
print('List of employees working in this department')
mycursor.execute("select ename from employee where deptno = {}".format(empno))
myrec=mycursor.fetchall()
for x in myrec:
    print(x)
