# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 23:19:51 2017

@author: ranveer
"""
import	mysql.connector as	conn
db = conn.connect(host='localhost',user = 'root' , database = 'dbase1',password =' ')	
if	db.is_connected():	
        print('Connected	to	MySQL	database')
        cursor	=	db.cursor()
        sql1="""insert into restaurant1  (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (101, 'SCOOPvalues 'sector-1values 9878005641, 100, 4.5)"""
        sql2="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (102, 'AZAD HINDvalues 'sector-2values 9878005691, 100, 4.6)"""
        sql3="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (103, 'THE SILVER SPOONvalues 'sector-3values 9868005621, 100, 4.2)"""
        sql4="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (104, 'CALIBERvalues 'sector-4values 9878005521, 100, 4.4)"""
        sql5="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (105, 'THE SILVER FORKvalues 'sector-5values 8978005631, 100, 3.5)"""
        sql6="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (106, 'MEHAK- E - PUNJABvalues 'sector-1values 8578005621, 100, 3.5)"""
        sql7="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (107, 'CHOWMANvalues 'sector-2values 8478005621, 100, 4.5)"""
        sql8="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (108, 'DOMINOSvalues 'sector-3values 8678005621, 100, 4.9)"""
        sql9="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (109, 'PIZZA HUTvalues 'sector-4values 8978005621, 100, 4.7)"""
        sql10="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (110, 'KFCvalues 'sector-5values 7878005621, 100, 4.3)"""
        sql11="""insert into restaurant1 (SERIAL_NO,restaurant_NAME,MOBILE_NO.,ADDRESS,RATING) values (111, 'RASOIvalues 'sector-1values 8878005621, 100, 4.5)"""
        try :
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            cursor.execute(sql4)
            cursor.execute(sql5)
            cursor.execute(sql6)
            cursor.execute(sql7)
            cursor.execute(sql8)
            cursor.execute(sql9)
            cursor.execute(sql10)
            cursor.execute(sql11)

            db.commit()	
            print("record	created	......!")
        except:
            db.rollback()
            print('record	could	not	be	created…...!')	
        
        finally:	
            db.close()
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    																


    
