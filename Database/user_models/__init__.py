#!/usr/bin/python3


#from user_models.engine.user_db import UserDataBase
#storage = UserDataBase()
#print("HHIOOOONN")
#storage.reload()

try:
    from user_models.engine.user_db import UserDataBase
    storage = UserDataBase()
    storage.reload()
except Exception as e:
    print("An error occurred:", str(e))
