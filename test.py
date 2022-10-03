import mysql.connector
# Creating python final project on student managment system
# For what you want to login:
#     Technical team
#         Updation of data
#         deletion of data
#         Checking for databases
#     prinicipal
#         students information
#         teachers information
#         writing for notice board
#         any query from parent
#         information of sweepers, garden takecare ,bus drivers,conductors,Technical team
#         any thought of the day
#         admission
#     students                name of table=loginstudent
#         marks for subjects-----------------------------------------------------name of table=student_marksshow
#         attendance
#         report card
#         any information
#     teacher                 name of table=loginteacher
#         marks for students---------------------------------------------------   name of table=teacher_marksstorage
#         attendance of teachers--------------------------------------------------  name of table=teacher_attendancestorage
#         report cards------------------------------------------------------     name of table=teacher_reportcardstorage
#         complaint of students-----------------------------------------------------
#         cocircular activities info
#         any notice for any class---------------------------------------------------
#         any thought of the day----------------------------------------
#         info about school competition
#     admission
#         register for admisiion
#         inquiry of admission
#         results of admission
#         availaibility of admission
#     if you have any query------------------------------------------------
#         about school
#         about teacher
#         about student
#     About school------------------------------------------------------
#         all info about school
hereistheuser="root"
hereisthepassword="newera123"
mydb = mysql.connector.connect(host="localhost", user=hereistheuser, password=hereisthepassword)
mycursor = mydb.cursor()
mycursor.execute("drop database if exists school;")
mycursor.execute("create database if not exists school;")
mycursor.execute("use school;")


mycursor.execute("create table if not exists login(Username varchar(30) NOT NULL,Password varchar(15) NOT NULL,Logintype varchar(30) NOT NULL);")
mycursor.execute("insert into login values('jasjeev','jas123','student');")
mycursor.execute("insert into login values('aryan','ary123','student');")
mycursor.execute("insert into login values('lalit','lal123','teacher');")
mycursor.execute("insert into login values('technical','tec123','technical team');")


mycursor.execute("create table if not exists loginstudent(Username varchar(30) NOT NULL,Password varchar(15) NOT NULL,Name varchar(50) NOT NULL,Class varchar(20) NOT NULL,Admissionnumber varchar(30) ,Logintype varchar(30) NOT NULL,Gender varchar(1) NOT NULL);")
mycursor.execute("insert into loginstudent values('jasjeev','jas123','Jasjeev','XII-F','100073','student','M');")
mycursor.execute("insert into loginstudent values('aryan','ary123','Aryan','XII-F','144534','student','M');")


mycursor.execute("create table if not exists loginteacher(Username varchar(30) NOT NULL,Password varchar(15) NOT NULL,Name varchar(50) NOT NULL,Subject varchar(20) NOT NULL,Logintype varchar(30) NOT NULL,Gender varchar(1) NOT NULL);")
mycursor.execute("insert into loginteacher values('lalit','lal123','Lalit','CS','teacher','M');")
mycursor.execute("insert into loginteacher values('teacher','tea123','Teacher','Maths','teacher','F');")

mydb.commit()
mydb.close()
