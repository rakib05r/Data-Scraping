# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3


class TutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("my_dict_db.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS my_dict_db_table""")
        self.curr.execute("""create table my_dict_db_table(
					 id integer primary key autoincrement,
                     eng_word  text,
                     ban_mean  text
                     )""")

    def store_db(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into my_dict_db_table values(NULL,?,?)""", (
            item['eng_word'],
            item['ban_mean']
        ))
        self.conn.commit()
