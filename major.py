# COMPUTER SCIENCE INTERSHIP PROGRAM


# INTERSHIP

'''This coding is done by Me (Prashant) with the help of my teammate -- Ashish.'''

# Codes start from here...

import mysql.connector as H

# Making code to connect to the database.

mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
mycursor = mydb.cursor()
if mydb.is_connected():
    print('   Successfully Connected to MySQL Database')

# TABLE CREATION

# Table1
mycursor.execute(
    "Create table if not exists Interner(RegNo int(10),Name varchar(22),Age int(2),Field varchar(15),Salary int(6),RegDate varchar(30),Expdate varchar(30))")
mydb.commit()

# Table2
mycursor.execute(
    "Create table if not exists staff(Sfno int(5),Sfname varchar(15),Design varchar(15),Salary int(7),Inidate varchar(15))")
mydb.commit()

# Table3
mycursor.execute("Create table if not exists Fee(RegNo int(5),Fee int(6),Month varchar(12),Paid varchar(15))")
mydb.commit()

# Table4
mycursor.execute(
    "Create table if not exists Examination(Name varchar(15),RegNo int(5),Percentage float(5),Result varchar(15))")
mydb.commit()

print('   \n\n\n   This is the database of Computer Science Internship\n\n\n')
print("""
                                                        
                                                           *************************************
                                                             -- COMPUTER SCIENCE INTERNSHIP --
                                                           *************************************
                                                             --MAKE A BETTER FUTURE WITH CODES--                                                 """)

# ADDING PRIMARY KEY...

'''sql = "alter table Interner add Primary key(RegNo)"
mycursor.execute(sql)
mydb.commit()
sql = "alter table staff add Primary key(SfNo)"
mycursor.execute(sql)
mydb.commit()
sql = "alter table Fee add Primary key(RegNo)"
mycursor.execute(sql)
mydb.commit()
sql = "alter table examination add Primary key(RegNo)"
mycursor.execute(sql)
mydb.commit()
print("Primary key added successfully")'''


# Function to take values from the user....

def insert1():
    try:
        RegNo = int(input("   Enter Interner's registration no. :"))
        Name = input("   Enter Interner's name:")
        Age = int(input("   Enter Interner's age "))
        Field = input("   Enter Interner's field:")
        Salary = int(input("   Enter Interner's salary "))
        RegDate = input("   Enter Interner's registration date(yyyy-mm-dd):")
        ExpDate = input("   Enter Interner's Expiration date(yyyy-mm-dd):")
        mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
        mycursor = mydb.cursor()
        mysql = "INSERT INTO interner(RegNo,Name,Age,Field,Salary,RegDate,Expdate) VALUES( '%d', '%s', '%d', '%s', '%d', '%s','%s')" % (
        RegNo, Name, Age, Field, Salary, RegDate, ExpDate)
        mycursor.execute(mysql)
        print("   Data was entered correctly")
        mydb.commit()
    except:
        print('   Something went wrong')


# INFORMATION_DATABSE_DETAILS

def display_1info(course):
    while True:
        if course == '1':
            print("""
   Algorithm design is a specific method to create a mathematical process in problem solving
   processes.In computer science, the analysis of algorithms is the determination of the of
   the computational complexity of algorithms, that is the amount of time, storage and/or
   other resources necessa0ry to execute them.""")
            display_1a()
        elif course == '2':
            print("""
   A data structure is a specialized format for organizing, processing, retrieving and storing data.
   While there are several basic and advanced structure types, any data structure is designed to
   arrange data to suit a specific purpose so that it can be accessed and worked with in appropriate ways""")
            display_1a()

        elif course == '3':
            print("""
   A compiler translates the code written in one language to some other language without
   changing the meaning of the program. Compiler design covers basic translation mechanism
   and error detection & recovery. It includes lexical, syntax, and semantic analysis as front end,
   and code generation and optimization as back-end.""")
            display_1a()

        elif course == '4':
            print("""
   Object-oriented programming is a programming paradigm based on the concept of 'objects',
   which can contain data, in the form of fields, and code, in the form of procedures.
   A feature of objects is an object's procedures that can access and often modify the data fields
   of the object with which they are associated.""")
            display_1a()

        elif course == '5':
            print("""
   Computer security, cybersecurity or information technology security is the protection of
   computer systems from the theft of or damage to their hardware, software, or electronic
   data, as well as from the disruption or misdirection of the services they provide.\n
   Ethical hacking and ethical hacker are terms used to describe hacking performed by
   a company or individual to help identify potential threats on a computer or network.
   An ethical hacker attempts to bypass system security and search for any weak points that
   could be exploited by malicious hacker""")
            display_1a()

        elif course == '6':
            print("""
   Artificial intelligence (AI) is the simulation of human intelligence processes by machines,
   especially computer systems. These processes include learning (the acquisition of
   information and rules for using the information), reasoning (using rules to reach
   approximate or definite conclusions) and self-correction.""")
            display_1a()

        elif course == '7':
            print("""
   Web design encompasses many different skills and disciplines in the production and
   maintenance of websites. The different areas of web design include web graphic design;
   interface design; authoring, including  code and proprietary software; user
   experience design; and search engine optimization""")
            display_1a()

        elif course == '8':
            print("""
   Graphic design is the process of visual communication and problem-solving through the
   use of typography, photography, and illustration. The field is considered a subset of visual
   communication and communication design, but sometimes the term 'graphic design' is
   used synonymously.""")
            display_1a()

        elif course == '9':
            print("""
   Cryptography or cryptology is the practice and study of techniques for secure
   communication in the presence of third parties called adversaries.""")
            display_1a()

        elif course == '10':
            print("""
   Digital marketing is the marketing of products or services using digital technologies
   on the Internet, including through mobile phones Apps, using display advertising,
   and any other digital mediums.""")
            display_1a()

        elif course == 'E':
            break

        else:
            print("\n   Wrong Entry, Check it again !\n")
            display_1a()


# STAFF_DATABASE_DETAILS

def display_2a1(staff):
    while True:
        if staff == '1':
            print("""\n   ACADEMIC STAFF\n
    |Prof. Sanjay Kumar Singh|
    ~Professor~

    |Dr. Chandra Prakash Singh|
    ~Associate Professor~

    |Mr. Anand Srivastava|
    ~Assistant Professor~

    |Mr. Vinay Kumar|
    ~Assistant Professor~

    |Mr. Bimal Kumar Rai|
    ~Assistant Professor~\n""")
            display_2a()

        elif staff == '2':
            print("""\n   ACADEMIC TEACHING STAFF\n

    |Mr. Ashutosh Srivastava|
    ~Lecturer~

    |Mr. Anand Mohan Pandey|
    ~Lecturer~

    |Mr. Sujeet Singh |
    ~Lecturer~ 

    |Mr. Vijay Kumar Pandey |
    ~Lecturer~

    |Dr. Shailendra Tiwar|
    ~Senior Lecturer~ 

    |Mr. Anurag Singh|
    ~Programmer~

    |Mr. Shalesh Pratap Sing|
    ~Programmer~\n""")

    
            display_2a()

        elif staff == 'E':
            break

        else:
            print("\n   Wrong Entry, Check it again !\n")
            display_2a()


# FEE_DATABASE_DETAILS

def display_3a1(ch1):
    while True:
        print("""\n
   Computer Science is a pass in 10+2 with science subjects.
   The approximate tuition fee of this program in government-funded institutes is
   INR 15,000 to 25,000 for three years. This figure may go up to Lakhs in case of private institutes.""")

        if ch1 == '1':
            print("""\n
    Average Starting Salary: INR 3-7 Lakhs per annum

    Course Fee: INR 15,000 to 25,000

    Admission Process: Merit-based

    Eligibility: 10+2 with science subjects\n""")
            display_3a()

        elif ch1 == '2':
            print("""\n
    Average Starting Salary: INR 8-14 Lakhs per annum

    Course Fee: INR 30,000 to 55,000

    Admission Process: Merit-based + Eligibility Test

    Eligibility: 10+2 with science subjects\n""")
            display_3a()

        elif ch1 == '3':
            print("""\n
    Average Starting Salary: INR 12-18 Lakhs per annum

    Course Fee: INR 15,000 to 25,000

    Admission Process: Merit-based + Eligibility Test + Interview

    Eligibility: 10+2 with science subjects\n""")
            display_3a()

        elif ch1 == 'E':
            break

        else:
            print("\n   Wrong Entry, Check it again !\n")
            display_3a()


# EXAMINATION_DATABASE_DETAILS

def display_4a1(ch2):
    while True:

        if ch2 == '1':
            print("""
\n   Weekly exams on Saturday \n""")
            display_4a()

        elif ch2 == '2':
            print("""
\n   Monthly exam on last day of month\n""")
            display_4a()

        elif ch2 == '3':
            print("""
\n   Yearly exam have three parts :-
   First one will occur in JUNE month and the
   Second one in SEPTEMBER month and the
   Third i.e., the last one in FEBRUARY month\n""")
            display_4a()


        elif ch2 == 'E':
            break

        else:
            print("\n   Wrong Entry, Check it again !\n")
            display_4a()


# FUNCTION TO SHOW DETAILS

def display_1(regno):
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    cursor = mydb.cursor()
    print("   What you wanna know about")
    kno = input()
    know = kno.upper()
    if know == "NAME":
        mycursor.execute("Select name from interner where RegNo=%s" % (regno))
        result = mycursor.fetchone()
        print("   Name =", result)
    elif know == "AGE":
        mycursor.execute("Select age from interner where RegNo=%s" % (regno))
        result = mycursor.fetchone()
        print("   Age =", result)
    elif know == "FIELD":
        mycursor.execute("Select field from interner where RegNo=%s" % (regno))
        result = mycursor.fetchone()
        print("   Field =", result)
    elif know == "SALARY":
        mycursor.execute("Select salary from interner where RegNo=%s" % (regno))
        result = mycursor.fetchone()
        print("   Salary =", result)
    elif know == "REGISTRATION DATE":
        mycursor.execute("Select  RegDate from interner where RegNo=%s" % (regno))
        result = mycursor.fetchone()
        print("   Registation Date =", result)
    elif know == "EXPIRY DATE":
        mycursor.execute("Select ExpDate from interner where RegNo=%s" % (regno))
        result = mycursor.fetchone()
        print("   Expiry Date =", result)
    else:
        print("   Column dosen't exist")


def display_2(sfno):
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    cursor = mydb.cursor()
    print("   What you wanna know about")
    kno = input()
    know = kno.upper()
    if know == "NAME":
        mycursor.execute("Select sfname from staff where Sfno=%s" % (sfno))
        result = mycursor.fetchone()
        print("   Name =", result)
    elif know == "DESIGNATION":
        mycursor.execute("Select design from staff where Sfno=%s" % (sfno))
        result = mycursor.fetchone()
        print("   Designation=", result)
    elif know == "SALARY":
        mycursor.execute("Select salary from Staff where Sfno=%s" % (sfno))
        result = mycursor.fetchone()
        print("   Salary =", result)
    elif know == "JOINING DATE":
        mycursor.execute("Select Inidate from Staff where Sfno=%s" % (sfno))
        result = mycursor.fetchone()
        print("   Joining Date =", result)
    else:
        print("   Column dosen't exist")


def display_3(regno):
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    cursor = mydb.cursor()
    print("   What you wanna know about")
    kno = input()
    know = kno.upper()
    if know == "FEE":
        mycursor.execute("Select fee from Fee where regno=%s" % (regno))
        result = mycursor.fetchone()
        print("   Fee =", result)
    elif know == "MONTH":
        mycursor.execute("Select month from Fee where regno=%s" % (regno))
        result = mycursor.fetchone()
        print("   Month=", result)
    elif know == "PAID":
        mycursor.execute("Select paid from fee where regno=%s" % (regno))
        result = mycursor.fetchone()
        print("   Paid =", result)
    else:
        print("   Column dosen't exist")


def display_4(regno):
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    cursor = mydb.cursor()
    print("   What you wanna know about")
    kno = input()
    know = kno.upper()
    if know == "NAME":
        mycursor.execute("Select name from examination where regno=%s" % (regno))
        result = mycursor.fetchone()
        print("   Name =", result)
    elif know == "PERCENTAGE":
        mycursor.execute("Select percentage from examination where regno=%s" % (regno))
        result = mycursor.fetchone()
        print("   Percentage=", result)
    elif know == "RESULT":
        mycursor.execute("Select result from examination where regno=%s" % (regno))
        result = mycursor.fetchone()
        print("   Result =", result)
    else:
        print("   Column dosen't exist")


# UPDATE SECTION


def update_1(col, regno_):
    newcol = col.upper()
    if newcol == 'NAME':
        new = input("   Enter the correct name: ")
        sql = "update Interner set name='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'AGE':
        new = int(input("   Enter correct age: "))
        sql = "update Interner set age=%s where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'FIELD':
        new = input("   Enter new field: ")
        sql = "update Interner set field='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'SALARY':
        new = int(input("   Enter correct Salary "))
        sql = "update interner set salary=%s where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'REGISTRATION DATE':
        new = input("   Enter correct registration date ")
        sql = "update Interner set regdate='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'EXPIRY DATE':
        new = input("   Enter correct Expiry date ")
        sql = "update Interner set expdate='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    else:
        mycursor.execute(sql)
        mydb.commit()


# INFORMATION_DISPLAY_FUNCTION

def display_1a():
    print('\n')
    print('''Intership Courses available\n
                    1.Design and Analysis of Algorithm
                    2.Data structures
                    3.Compiler design
                    4.Object Oriented Programming using C++/Java/Python
                    5.Cyber Security and Ethical Hacking
                    6.Artifitial Intelligence
                    7.Web Designing
                    8.Graphics Designing
                    9.Cryptography
                    10.Online Marketing
                    E.Exit\n''')

    course = input('   Choose [1-10] to more about these courses -:').upper()
    display_1info(course)


# STAFF_INFORMATION_DISPLAY_FUNCTION

def display_2a():
    print("""
                    1.ACADEMIC STAFF
                    2.ACADEMIC TEACHING STAFF
                    E.Exit\n""")

    staff = input('   Choose [1-2] for details -:').upper()
    display_2a1(staff)


# FEE_INFORMATION_DISPLAY_FUNCTION

def display_3a():
    print("""
   Internship for
                    1.One year(Basic)
                    2.2 years(Professional)
                    3.4 years(Elite)
                    E.Exit\n""")
    ch1 = input('   Choose [1-3] for details -:').upper()
    display_3a1(ch1)


# EXAMINATION_INFORMATION_DISPLAY_FUNCTION

def display_4a():
    print("""
   EXAMINATION DETAILS
                    1.Weekly
                    2.Monthly
                    3.Yearly
                    E.Exit\n""")

    ch2 = input('   Choose [1-3] for details -:').upper()
    display_4a1(ch2)


# UPDATE__SECTION_2


def update_2(col, sfno_):
    newcol = col.upper()
    if newcol == 'NAME':
        new = input("   Enter the correct name: ")
        sql = "update Staff set sfname='%s' where sfno=%s" % (new, sfno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'DESIGNATION':
        new = input("   Enter correct designation: ")
        sql = "update Staff set design='%s' where sfno=%s" % (new, sfno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'SALARY':
        new = int(input("   Enter correct salary "))
        sql = "update Staff set salary=%s where sfno=%s" % (new, sfno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'JOINING DATE':
        new = input("   Enter correct joining date ")
        sql = "update Staff set inidate='%s' where sfno=%s" % (new, sfno_)
        mycursor.execute(sql)
        mydb.commit()

    else:
        mycursor.execute(sql)
        mydb.commit()


##update sec__3


def update_3(col, regno_):
    newcol = col.upper()
    if newcol == 'FEE':
        new = int(input("   Enter the correct Fee: "))
        sql = "update Fee set fee=%s where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'MONTH':
        new = input("   Enter correct designation: ")
        sql = "update Fee set month='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'PAID':
        new = input("   Enter new payment information ")
        sql = "update Fee set Paid='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    else:5
        mycursor.execute(sql)
        mydb.commit()


# UPDATE FUNCTION


def update_4(col, regno_):
    newcol = col.upper()
    if newcol == 'NAME':
        new = input("   Enter the correct name: ")
        sql = "update Examination set name='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'PERCENTAGE':
        new = float(input("   Enter correct percentage: "))
        sql = "update Examination set percentage=%s where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    elif newcol == 'RESULT':
        new = input("   Enter new payment information ")
        sql = "update Examination set result='%s' where regno=%s" % (new, regno_)
        mycursor.execute(sql)
        mydb.commit()

    else:
        mycursor.execute(sql)
        mydb.commit()


# DISPLAY FOR MAIN TABLE- 'INTERNER'


def display1():
    try:
        mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
        cursor = mydb.cursor()
        mysql = "Select * from Interner "
        cursor.execute(mysql)
        results = cursor.fetchall()
        for choice in results:
            RegNo = choice[0]
            Name = choice[1]
            Age = choice[2]
            Field = choice[3]
            Salary = choice[4]
            RegDate = choice[5]
            Expdate = choice[6]
            print("(RegNo=%d,Name=%s,Age=%d,Field=%s,Salary=%d,RegDate=%s,Expdate=%s)" % (
            RegNo, Name, Age, Field, Salary, RegDate, Expdate))
    except:
        print("   Error: Something went wrong !")
        mydb.close()


# UPDATE FOR MAIN TABLE- 'INTERNER'

def update1():
    New1 = int(input("   Enter Registartion no."))
    New2 = input("    Enter new Field ")
    mysql = "Update Interner set Field='%s' where RegNo='%d'" % (New2, New1)
    mycursor.execute(mysql)
    mydb.commit()


# DELETE FOR MAIN TABLE- 'INTERNER'

def delete1():
    try:
        mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
        cursor = mydb.cursor()
        mysql = "Select * from Interner "
        cursor.execute(mysql)
        results = cursor.fetchall()
        for choice in results:
            RegNo = choice[0]
            Name = choice[1]
            Age = choice[2]
            Field = choice[3]
            Salary = choice[4]
            RegDate = choice[5]
            Expdate = choice[6]
    except:
        print("   Error: Something went wrong !")

    New1 = int(input("\n   Enter Registration No to be convicted:"))
    try:
        mysql = "Delete from Interner where RegNo='%d'" % (New1)
        Check = input("   Are you surely want to delete this record(Y/N):")
        if Check == 'Y' or Check == 'y':
            cursor.execute(mysql)
            print("   Data was deleted successfully")
            mydb.commit()
    except Exception as e:
        print(e)
        mydb.close()


# INSERT FOR TABLE- 'STAFF'


def insert2():
    Sfno = int(input("   Enter Staff's No.:"))
    Sfname = input("   Enter Staff's Name:")
    Design = input("   Enter Staff's Designation:")
    Salary = int(input("   Enter Staff's salary "))
    Inidate = input("   Enter date of joining (yyyy-mm-dd) :")
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    mycursor = mydb.cursor()
    mysql = "INSERT INTO staff(Sfno,Sfname,Design,Salary,Inidate) VALUES( '%d', '%s', '%s', '%d', '%s')" % (
    Sfno, Sfname, Design, Salary, Inidate)
    mycursor.execute(mysql)
    mydb.commit()
    print("   Your data was entered  sucessfully")


# DISPLAY FOR TABLE- 'STAFF'

def display2():
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    cursor = mydb.cursor()
    mysql = "Select * from Staff"
    cursor.execute(mysql)
    results = cursor.fetchall()
    for choice in results:
        Sfno = choice[0]
        Sfname = choice[1]
        Design = choice[2]
        Salary = choice[3]
        Inidate = choice[4]
        print("(Sfno=%d,Sfname=%s,Design=%s,Salary=%d,Inidate=%s)" % (Sfno, Sfname, Design, Salary, Inidate))


# UPDATE FOR TABLE- 'STAFF'

def update2():
    New1 = int(input("   Enter Staff no."))
    New2 = input("    Enter new Designation ")
    mysql = "Update staff set design='%s' where sfno=%d" % (New2, New1)
    mycursor.execute(mysql)
    mydb.commit()


# DELETE FOR TABLE- 'STAFF'


def delete2():
    try:
        mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
        cursor = mydb.cursor()
        mysql = "Select * from Staff "
        cursor.execute(mysql)
        results = cursor.fetchall()
        for choice in results:
            Sfno = choice[0]
            Sfname = choice[1]
            Design = choice[2]
            Salary = choice[3]
            Inidate = choice[4]
    except:
        print("   Error: Something went wrong !")

    New1 = int(input("\n   Enter Staff No. to be convicted:"))
    try:
        mysql = "Delete from Staff where Sfno='%d'" % (New1)
        Check = input("   Are you surely want to delete this record(Y/N):")
        if Check == 'Y' or Check == 'y':
            cursor.execute(mysql)
            mydb.commit()
    except Exception as e:
        print(e)
        mydb.close()

    # INSERT FOR TABLE- 'FEE'


def insert3():
    RegNo = int(input("   Enter Registration No.:"))
    Fee = float(input("   Enter Fee amount:"))
    Month = input("   Enter Month:")
    Paid = input("   Paid? Enter Yes/No. ")
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    mycursor = mydb.cursor()
    mysql = "INSERT INTO Fee(RegNo,Fee,Month,Paid) VALUES( '%d', '%d', '%s', '%s')" % (RegNo, Fee, Month, Paid)
    mycursor.execute(mysql)
    mydb.commit()
    print("   Your data was entered  sucessfully")


# DISPLAY FOR TABLE- 'FEE'

def display3():
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    cursor = mydb.cursor()
    mysql = "Select * from Fee"
    cursor.execute(mysql)
    results = cursor.fetchall()
    for choice in results:
        RegNo = choice[0]
        Fee = choice[1]
        Month = choice[2]
        Paid = choice[3]
        print("(RegNo=%d,Fee=%d,Month='%s',Paid='%s')" % (RegNo, Fee, Month, Paid))


# UPDATE FOR TABLE- 'FEE'

def update3():
    try:
        mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
        cursor = mydb.cursor()
        mysql = "Select * from Fee "
        cursor.execute(mysql)
        results = cursor.fetchall()
        for choice in results:
            RegNo = choice[0]
            Fee = choice[1]
            Month = choice[2]
            Paid = choice[3]
    except:
        print("   Error: Something went wrong !")
    print()
    New1 = int(input("   Enter Registartion no."))
    New2 = int(input("    Enter correct fee "))
    try:
        mysql = "Update Fee set Fee=%d where RegNo=%d" % (New2, New1)
        cursor.execute(mysql)
        mydb.commit()
    except Exception as e:
        print(e)
        mydb.close()


# DELETE FOR TABLE- 'FEE'

def delete3():
    try:
        mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
        cursor = mydb.cursor()
        mysql = "Select * from Staff "
        cursor.execute(mysql)
        results = cursor.fetchall()
        for choice in results:
            RegNo = choice[0]
            Fee = choice[1]
            Month = choice[2]
            Paid = choice[3]
    except:
        print("   Error: Something went wrong !")

    New1 = int(input("\n   Enter Registration No. to be convicted:"))
    try:
        mysql = "   Delete from Fee where RegNo='%d'" % (New1)
        Check = input("   Are you surely want to delete this record(Y/N):")
        if Check == 'Y' or Check == 'y':
            cursor.execute(mysql)
            mydb.commit()
    except Exception as e:
        print(e)
        mydb.close()

    # INSERT FOR TABLE- 'EXAMINATION'


def insert4():
    Name = input("   Enter Interner's Name:")
    RegNo = int(input("   Enter Registration No.:"))
    Percentage = float(input("   Enter percentage:"))
    Result = input("   Enter result: ")
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    mycursor = mydb.cursor()
    mysql = "INSERT INTO Examination(Name,RegNo,Percentage,Result) VALUES( '%s', '%d', '%s', '%s')" % (
    Name, RegNo, Percentage, Result)
    mycursor.execute(mysql)
    mydb.commit()
    print("   Your data was entered  sucessfully")


# DISPLAY FOR TABLE- 'EXAMINATION'

def display4():
    mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
    cursor = mydb.cursor()
    mysql = "Select * from Examination"
    cursor.execute(mysql)
    results = cursor.fetchall()
    for choice in results:
        Name = choice[0]
        RegNo = choice[1]
        Percentage = choice[2]
        Result = choice[3]
        print("(Name=%s,RegNo=%d,Percentage=%f,Result=%s)" % (Name, RegNo, Percentage, Result))


# UPDATE FOR TABLE- 'EXAMINATION'

def update4():
    try:
        mydb = H.connect(host="localhost", user="root", passwd="1234", database="Initiative")
        cursor = mydb.cursor()
        mysql = "Select * from Examination "
        cursor.execute(mysql)
        results = cursor.fetchall()
        for choice in results:
            Name = choice[0]
            RegNo = choice[1]
            Percentage = choice[2]
            Result = choice[3]
    except:
        print("   Error: Something went wrong !")
    print()
    New1 = int(input("   Enter Registartion no."))
    New2 = float(input("   Enter correct percentage value : "))
    try:
        mysql = "Update Examination set Percentage=%f where RegNo=%d" % (New2, New1)
        cursor.execute(mysql)
        mydb.commit()
    except Exception as e:
        print(e)
        mydb.close()


# DELETE FOR TABLE- 'EXAMINATION'

def delete4():
    try:
        mydb = H.connect(host="localhost", user="root", passwd="12342", database="Initiative")
        cursor = mydb.cursor()
        mysql = "Select * from Staff "
        cursor.execute(mysql)
        results = cursor.fetchall()
        for choice in results:
            Name = choice[0]
            RegNo = choice[1]
            Percentage = choice[2]
            Result = choice[3]
    except:
        print("   Error: Something went wrong !")

    New1 = int(input("\n   Enter Registration No. to be convicted:"))
    try:
        mysql = "Delete from Examination where RegNo=%d" % (New1)
        Check = input("   Are you surely want to delete this record(Y/N):")
        if Check == 'Y' or Check == 'y':
            cursor.execute(mysql)
            mydb.commit()
    except Exception as e:
        print(e)
        mydb.close()


# USING WHILE FUNCTION _MAIN_

while True:
    print("   \n\n   Choose any option as required:\n")
    print("   1.Interner")
    print("   2.Staff")
    print("   3.Fee ")
    print("   4.Intership Exams")
    print("   5.Help")
    print("   6.Exit")

    ch = int(input("\n\n   Enter your choice [1-6]: "))
    if ch == 6:
        print("   Hope to see you soon")
        break

    while True:
        if ch == 1:
            print("\n    GREETINGS, THIS IS COMPUTER SCIENCE INTERNSHIP\n")
            print("   a.New Admission")
            print("   b.Update your details")
            print("   c.Specific updates")
            print("   d.Issue TC")
            print("   e.Show every detail")
            print("   f.Specific details")
            print("   g.Exit")
            choice = input(" \n  Enter your choice [a-g]: ")

            if choice == 'a':
                print("\n    Initially details are...\n")
                display1()
                print('\n\n')
                insert1()
                print("\n    Modified details are...\n")
                display1()

            elif choice == 'b':
                print("\n    Initially details are...\n")
                display1()
                print('\n\n')
                update1()
                print("\n    Modified details are...\n")
                display1()

            elif choice == 'c':
                print("\n    Initially details are...\n")
                display1()
                print('\n\n')
                print("   Enter the registration  number of Interner")
                regno_ = int(input())
                print("   What do you want to update :")
                update = input()
                update_1(update, regno_)
                print("   Data Updated Successfully")
                print("\n    Modified details are...\n")
                display1()

            elif choice == 'd':
                print("\n    Initially details are...\n")
                display1()
                print('\n\n')
                delete1()
                print("\n    Modified details are...\n")
                display1()

            elif choice == 'e':
                display1()

            elif choice == 'f':
                print("\n   Enter the registration number of Interner")
                Search1 = int(input())
                display_1(Search1)

            elif choice == 'g':
                break

            else:
                print("   Enter correct choice...!!")


        elif ch == 2:
            print("   GREETINGS, THIS IS STAFF MANAGEMENT DATBASE")
            print("   a.New Staff")
            print("   b.Update staff details")
            print("   c.Specific updates")
            print("   d.Delete Staff")
            print("   e.Display all data")
            print("   f.Specific details")
            print("   g.Exit")
            choice = input(" \n  Enter your choice [a-g]:")

            if choice == 'a':
                print("\n    Initially details are...\n")
                display2()
                print('\n\n')
                insert2()
                print("\n    Modified details are...\n")
                display2()

            elif choice == 'b':
                print("\n    Initially details are...\n")
                display2()
                print('\n\n')
                update2()
                print("\n    Modified details are...\n")
                display2()

            elif choice == 'c':
                print("\n    Initially details are...\n")
                display2()
                print('\n\n')
                print("   Enter the staff number of Interner")
                sfno_ = int(input())
                print("   What do you want to update :")
                update = input()
                update_2(update, sfno_)
                print("   Data Updated Successfully")
                print("\n    Modified details are...\n")
                display2()

            elif choice == 'd':
                print("\n    Initially details are...\n")
                display2()
                print('\n\n')
                delete2()
                print("\n    Modified details are...\n")
                display2()

            elif choice == 'e':
                display2()

            elif choice == 'f':
                print("\n   Enter the staff number of Interner")
                Search2 = int(input())
                display_2(Search2)

            elif choice == 'g':
                break
            else:
                print("  \n Enter correct choice...!!")


        elif ch == 3:
            print("   GREETINGS, THIS IS FEE DATABASE")
            print("   a.New Fee")
            print("   b.Update Fee")
            print("   c.Specific updates")
            print("   d.Exempt Fee")
            print("   e.Display all data")
            print("   f.Specific details")
            print("   g.Exit")
            choice = input(" \n  Enter your choice [a-g]:")

            if choice == 'a':
                print("\n    Initially details are...\n")
                display3()
                print('\n\n')
                insert3()
                print("\n    Modified details are...\n")
                display3()

            elif choice == 'b':
                print("\n    Initially details are...\n")
                display3()
                print('\n\n')
                update3()
                print("\n    Modified details are...\n")
                display3()

            elif choice == 'c':
                print("\n    Initially details are...\n")
                display3()
                print('\n\n')
                print("   Enter the registration  number of Interner")
                regno_ = int(input())
                print("   What do you want to update :")
                update = input()
                update_3(update, regno_)
                print("   Data Updated Successfully")
                print("\n    Modified details are...\n")
                display3()

            elif choice == 'd':
                print("\n    Initially details are...\n")
                display3()
                print('\n\n')
                delete3()
                print("\n    Modified details are...\n")
                display3()

            elif choice == 'e':
                display3()

            elif choice == 'f':
                print(" \n  Enter the Registration number of Interner")
                Search3 = int(input())
                display_3(Search3)

            elif choice == 'g':
                break

            else:
                print(" \n  Enter correct choice...!!")


        elif ch == 4:
            print("   GREETINGS, THIS IS EXAMINATION DATABASE")
            print("   a.Internship details")
            print("   b.Update details")
            print("   c.Specific updates")
            print("   d.Delete details")
            print("   e.Display all data")
            print("   f.Specific details")
            print("   g.Exit")
            choice = input("\n   Enter your choice [a-g]:")

            if choice == 'a':
                print("\n    Initially details are...\n")
                display4()
                print('\n\n')
                insert4()
                print("\n    Modified details are...\n")
                display4()

            elif choice == 'b':
                print("\n    Initially details are...\n")
                display4()
                print('\n\n')
                update4()
                print("\n    Modified details are...\n")
                display4()

            elif choice == 'c':
                print("\n    Initially details are...\n")
                display4()
                print('\n\n')
                print("   Enter the registration number of Interner")
                regno_ = int(input())
                print("   What do you want to update :")
                update = input()
                update_4(update, regno_)
                print("   Data Updated Successfully")
                print("\n    Modified details are...\n")
                display4()

            elif choice == 'd':
                print("\n    Initially details are...\n")
                display4()
                print('\n\n')
                delete4()
                print("\n    Modified details are...\n")
                display4()

            elif choice == 'e':
                display4()

            elif choice == 'f':
                print(" \n  Enter the Registration number of Interner")
                Search4 = int(input())
                display_4(Search4)

            elif choice == 'g':
                break

            else:
                print(" \n  Enter correct choice...!!")


        elif ch == 5:
            print("   a.Interner Info")
            print("   b.Staff Info")
            print("   c.Fee Info ")
            print("   d.Intership Exams Info")
            print("   e.Exit")
            choice = input("  \n Enter your choice [a-e]:")

            if choice == 'a':
                display_1a()

            elif choice == 'b':
                display_2a()

            elif choice == 'c':
                display_3a()

            elif choice == 'd':
                display_4a()

            elif choice == 'e':
                break



        elif ch == 6:
            print("  \n Hope to see you soon")
            break

# THE CODE ENDS HERE…
