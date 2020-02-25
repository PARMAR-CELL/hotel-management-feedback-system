# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 23:17:16 2017

@author: ranveer
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:17:06 2017

@author: ranveer
"""
import sqlite3
import pandas as pd
db = sqlite3.connect('dbase1')
curs = db.cursor()
#tblcmd	= 'create table	res10 (serial_no intger PRIMARY KEY, res_name char(30), address char(10), phone_no integer, no_of_visitors integer, rating float)'
#curs.execute(tblcmd)	
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (101, 'SCOOP', 'sector-1', 9878555691, 100, 4.6))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (102, 'AZAD HIND', 'sector-2', 9878005691, 100, 4.6))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (103, 'THE SILVER SPOON', 'sector-3', 9868005621, 100, 4.2))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (104, 'CALIBER', 'sector-4', 9878005521, 100, 4.4))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (105, 'THE SILVER FORK', 'sector-5', 8978005631, 100, 3.5))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (106, 'MEHAK- E - PUNJAB', 'sector-1', 8578005621, 100, 3.5))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (107, 'CHOWMAN', 'sector-2', 8478005621, 100, 4.5))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (108, 'DOMINOS', 'sector-3', 8678005621, 100, 4.9))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (109, 'PIZZA HUT', 'sector-4', 8978005621, 100, 4.7))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (110, 'KFC', 'sector-5', 7878005621, 100, 4.3))
#curs.execute('insert into res10 values (?, ?, ?, ?, ?, ?)', (111, 'RASOI', 'sector-1', 8878005621, 100, 4.5))
print(pd.read_sql_query("select * from res10", db))

#sqlcmd = 'create table customer10 ( serial_no integer primary key,name char(2), rating float, comment char(500), FOREIGN KEY (serial_no) REFERENCES res105 (serial_no))'
#curs.execute(sqlcmd)


def connect(dbase1): 
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(dbase1)
    c = conn.cursor()
    return conn, c

def close(conn):
    """ Commit changes and close connection to the database """
    conn.commit()
    conn.close()

def See_rating() :
    print(pd.read_sql_query("select * from res10",db))
    
        
conn	=	 sqlite3.connect('dbase1')
curs	=	conn.cursor()	
print('=============================\n')
print('Welcome To Online Restaurant Rating System \n')
print('=============================\n')
print(' Please choose from the following option : ')
print()
while True:
	print('1. To See Rating \n' )
	print('2. To Give the Rating \n')
	print('3. To EXIT the program \n')

	choice = int(input("Please Enter your option : "))
	if choice == 1:
		  See_rating()
	elif choice == 2:
         print(pd.read_sql_query("select res_name from res10",db))
         print ('\n please select Restaurant serial no. name in which you want to give Rating')
         A = int(input("serial_no"))
         print ('********PREVIOUS COMMENTS OF THIS RESTAURANT***************')
         print(pd.read_sql_query("select comments from  res10 where serial_no = A ",db))
         print('please enter your details to give comment and ratings\n')
         print('=============================\n')
         print(' Welcome Sir/Madam  \n')
         print('=============================\n')
         conn	=	 sqlite3.connect('dbase1')
         curs	=	conn.cursor()	    
         print(' Please enter your detail : \n')
         Name = str(input("Mr./Mrs.")).upper()
         print ('\n please enter the Rating you want to give it')
         new_rating = float(input())
         conn	=	 sqlite3.connect('dbase1')
         curs = conn.cursor()
         print ('please enter your comment on it')
         comment = str(input())
         conn	=	 sqlite3.connect('dbase1')
         curs = conn.cursor()
         curs.execute("INSERT INTO customer10 values (?,?,?,?)", (A,Name,new_rating,comment))
         print(pd.read_sql_query("select * from customer10",conn))

         #Give_Rating()'
         
	elif choice == 3:
		conn.close()
		break
	else:
		print("Invalid choice ....!!!!\n")
