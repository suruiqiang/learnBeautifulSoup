## -*- coding:utf-8 -*- ＃
__author__ = 'Ray'
import MySQLdb
import sys

db = MySQLdb.connect("localhost","root","suruiqiang","article", charset="utf8")
cursor = db.cursor()
sql = "INSERT INTO science(title,link, image, summary) VALUES(%s,%s,%s,%s)"
def insert_item(item):
    param = (item['title'], item['link'], item['image'], item['summary'])
    cursor.execute(sql,param)
    db.commit()