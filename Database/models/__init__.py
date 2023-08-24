#!/usr/bin/python3
from models.engine.db import DataBase
from os import getenv

# UHR_MYSQL_USER = getenv('UHR_MYSQL_USER')
# UHR_MYSQL_PWD = getenv('UHR_MYSQL_PWD')
# UHR_MYSQL_HOST = getenv('UHR_MYSQL_HOST')
# UHR_MYSQL_DB = getenv('UHR_MYSQL_DB')
# storage = DataBase(UHR_MYSQL_USER, UHR_MYSQL_PWD, UHR_MYSQL_HOST, UHR_MYSQL_DB)
# storage.reload()

storage = DataBase()
storage.reload()