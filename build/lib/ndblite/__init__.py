#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 08/01/2018

@author: jeanmachuca


Example:

class User(ndb.Model):
    firstname = ndb.StringProperty('firstname') #the name of the property must to be the same name of the field
    lastname = ndb.StringProperty('lastname')
    age = ndb.IntegerProperty('age')

# create a new user
user = User()


# add infos about the user
user.firstname = 'Jean'
user.lastname = 'Machuca'
user.age = 35


# save the user into the database
user.put()
'''

from sqlitemodel import  Database, SQL
from sqlitemodel import Model as SQLITEModel

Database.DB_FILE = 'sqlite3.db'


def set_db(dbname):
    Database.DB_FILE = dbname

def IntegerProperty(name,*arg,**kargs):
    return {'name':name,'type':'INTEGER'}
def StringProperty(name,*arg,**kargs):
    return {'name':name,'type':'TEXT'}
def DateTimeProperty(name,*arg,**kargs):
    return {'name':name,'type':'TEXT'}
def FloatProperty(name,*arg,**kargs):
    return {'name':name,'type':'TEXT'}
def BooleanProperty(name,*arg,**kargs):
    return {'name':name,'type':'TEXT'}

_columns={}

class Model(SQLITEModel):
    id = {'name':'id','type':'INTEGER'}

    def __init__(self, id=None):
        SQLITEModel.__init__(self, id)
        # Tries to fetch the object by its rowid from the database
        self.getModel()
        self.createTable()
    # Tells the database class the name of the database table
    def tablename(self):
        return self.__class__.__name__.lower()
    # Tells the database class more about the table columns in the database
    def columns(self):
        if not _columns.has_key(self.__class__.__name__.lower()):
            keys = filter(lambda k: (not type(vars(self.__class__)[k]).__name__.__eq__('function')) and (not k.startswith('__')),[v for v in vars(self.__class__)])
            _columns[self.__class__.__name__.lower()] = [vars(self.__class__)[key] for key in keys]
        return _columns[self.__class__.__name__.lower()]
    def put(self,*args,**kargs):
        self.save(*args,**kargs)
