# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 23:54:23 2017

@author: ranveer
"""

import sqlite3
db = sqlite3.connect('dbase1')
curs = db.cursor()
#sqlcmd = 'create table customer10 ( serial_no integer primary key,name char(2), rating float, comment char(500), FOREIGN KEY (serial_no) REFERENCES res105 (serial_no))'
#curs.execute(sqlcmd)
curs.execute("delete comments  res10  ")



