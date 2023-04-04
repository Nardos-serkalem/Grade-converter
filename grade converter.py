

import sqlite3

con=sqlite3.connect('Test3_Student_Management_System.db')
cur=con.cursor()
# to commit to data base con.commit()

def studentDb_making():
       con



table_student=""
create table student(
stu_id int not null primary key,
first_name char(20) not null,
last_name char(20) not null,
total_grade float not null,
avaerage float not null
);
                
                        "" 


# creates table
cur.execute(table_student)
# should be commited
con.commit()


for i in result:
        print(i)


def grade(lst):
        avg=sum(lst)/len(lst)
        Sum=sum(lst)
        g=""
        if avg>=90 and avg<=100:
                g="grade=A+"
        elif avg>=80 and avg<=89:
                g="grade=A"
        elif avg>=70 and avg<=79:
                g="grade=B+"
        elif avg>=60 and avg<=69:
                g="grade=B"
        elif avg>=50 and avg<=59:
                g="grade=C+"
        elif avg>=40 and avg<=49:
                g="grade=C"
        elif avg>=30 and avg<=39:
                g="grade=D+"
        elif avg>=20 and avg<=29:
                g="grade=D"
        elif avg>=0 and avg<=19:
                g="grade=F"
        return (g,Sum,avg)
student_id=input("Enter Student Id: ")
first_name=input("Enter First Name: ")
last_name=input("Enter Last Name: ")
subno=int(input("enter number of subjects: "))
lst=[]
while subno>0:
        mark=float(input("Enter number "))
        if(mark>100 or mark<0):
                print("Mark invalid")
        else:
                lst.append(mark)
                subno-=1
print(grade(lst))


