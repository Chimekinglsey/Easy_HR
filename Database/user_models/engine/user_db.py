#!/usr/bin/python3
"""Conatins the database class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from user_models.user_base import UserBaseModel, UserBase


class UserDataBase():
    """The database session"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatiates a database object"""
        EHR_MYSQL_USER = getenv('ER_MYSQL_USER')
        EHR_MYSQL_PWD = getenv('ER_MYSQL_PWD')
        EHR_MYSQL_HOST = getenv('ER_MYSQL_HOST')
        EHR_MYSQL_DB = getenv('ER_MYSQL_DB')
        EHR_ENV = getenv('ER_ENV')

        print("EHR_MYSQL_USER:", EHR_MYSQL_USER)
        print("EHR_MYSQL_PWD:", EHR_MYSQL_PWD)
        print("EHR_MYSQL_HOST:", EHR_MYSQL_HOST)
        print("EHR_MYSQL_DB:", EHR_MYSQL_DB)
        print("EHR_ENV:", EHR_ENV)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(EHR_MYSQL_USER,
                                             EHR_MYSQL_PWD,
                                             EHR_MYSQL_HOST,
                                             EHR_MYSQL_DB))
        
        if EHR_ENV == "test":
            UserBase.metadata.drop_all(self.__engine)

    def new(self, obj):
        """ add an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commits all changes in the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete fro the database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        print("tttaaaaaaaaaaaaaaanjddklfjjjjjjjjjjjjjjjjjjjjjjjjr")
        #UserBase.metadata.create_all(self.__engine)
        try:
            UserBase.metadata.create_all(self.__engine)
            print("Tables successfully created.")
        except Exception as e:
            print("An error occurred while creating tables:", str(e))
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
        print(Session)

    
    def close(self):
        """cleans up database session"""
        self.__session.remove()

