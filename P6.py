# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 00:46:19 2017

@author: ranveer
"""

import	mysql.connector	as	db	
from	mysql.connector	import	Error	
"""	Connect	to	MySQL	database	"""	
try:	
        conn=db.connect(host='localhost’,database='dbase1’,user='ranvir’,password='ranvir1')	
            if	conn.is_connected():	
                cursor	=	conn.cursor()	
                except	Error	as	e:	
        print(e)	
finally:	
conn.close()	
print press A to see rating
print press B to give rating
print press C to exit

user_input = input('')

sql12 = select RESTAURANT_NAME, RATING from table restaurant1 
cursor.execute(sql12)
print('select NEW_RESTAURANT')
Z=input()
print('Enter new R')
NEW_RATING =  input('')
sql13 = update restaurant1 set RATING = ((RATING*NO._OF_VISITORS)+NEW_RATING)/(NO._OF_VISITORS+1) where RESTAURANT_NAME= Z
cursor.execute(sql13)
cursor.execute(sql12)



                 