# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:35:38 2017

@author: ranveer
"""

import	sqlite3	
conn	=	sqlite3.connect('dbase2')	#	if	not	present,	it	creates	a	database	
curs	=	conn.cursor()	
tblcmd	=	'create	table	people	(name	char(30),	job	char(10),	pay	int(4))'	
curs.execute(tblcmd)	
