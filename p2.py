# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:42:18 2017

@author: ranveer
"""

print ('***********WELCOME TO ONLINE FEEDBACK PROCESS*****************')
import	sqlite3	
conn	=	 sqlite3.connect('dbase3')
curs	=	conn.cursor()	
tblcmd	= 'create table	restaurant3 (serial_no int(4), res_name char(30), address char(10), phone_no int(10), no_of_visitors int(4), rating int(2) )'	
curs.execute(tblcmd)	
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (101, 'SCOOP ', 'sector-1 ', 9878005641, 100, 4.5)')
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (102, 'AZAD HIND ', 'sector-2 ', 9878005691, 100, 4.6)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (103, 'THE SILVER SPOON ', 'sector-3 ', 9868005621, 100, 4.2)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (104, 'CALIBER ', 'sector-4 ', 9878005521, 100, 4.4)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (105, 'THE SILVER FORK ', 'sector-5 ', 8978005631, 100, 3.5)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (106, 'MEHAK- E - PUNJAB ', 'sector-1 ', 8578005621, 100, 3.5)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (107, 'CHOWMAN ', 'sector-2 ', 8478005621, 100, 4.5)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (108, 'DOMINOS ', 'sector-3 ', 8678005621, 100, 4.9)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (109, 'PIZZA HUT ', 'sector-4 ', 8978005621, 100, 4.7)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (110, 'KFC ', 'sector-5 ', 7878005621, 100, 4.3)' )
curs.execute('insert into restaurant3 (SERIAL_NO,RESTAURANT_NAME,MOBILE_NO.,ADDRESS,RATING) values (111, 'RASOI ', 'sector-1 ', 8878005621, 100, 4.5)' )
print ('press - A  to see rating')
print ('press - B  to see rating')
print ('press - C  to exit')
A = curs.execute('select res_name from restaurant3')
user_input = input(':')
print (A)
