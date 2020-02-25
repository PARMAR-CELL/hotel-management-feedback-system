# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 23:57:18 2017

@author: ranveer
"""
import	mysql.connector	as	db	
from	mysql.connector	import	Error	
"""	Connect	to	MySQL	database	"""	
try:	
        conn=db.connect(host='localhost’,database='dbase1’,user='ranvir’,password='ranvir1')	
            if	conn.is_connected():	
                cursor	=	conn.cursor()	
                cursor.execute("DROP	TABLE	IF	EXISTS	CUSTOMER")	
                sql	=	"""CREATE	TABLE	CUSTOMER(CUST_NAME CHAR(20),RESTAURANT_NAME CHAR(20),COMMENT CHAR(200))"""
                
                cursor.execute(sql)
                																					
                print("Database	Created	....!")	
except	Error	as	e:	
        print(e)	
finally:	
conn.close()	

