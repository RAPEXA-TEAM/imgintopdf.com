#!/usr/bin/env

#import libraries that are needed

import pymysql
import config   #SERVER CONGIG

def connect_to_database():
    '''This function make a connection with datebase'''
    
    db = pymysql.connect(host=config.MYSQL_HOST,
                       user=config.MYSQL_USER,
                       passwd=config.MYSQL_PASS,
                       db=config.MYSQL_DATABASE)
    return(db)

def add_new_post_blog():
    #TODO
    '''this function add new post blog to website'''   
    pass