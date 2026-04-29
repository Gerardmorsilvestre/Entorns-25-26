from dataclasses import dataclass, asdict
from flask import jsonify
import mysql.connector
import hashlib
from time import time
import random


class UserDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection
     
    def getUserByToken(self,token):
        # connexió a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token = '" + token + "'"
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user


    def login(self, identifier, password):
        # connexió a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        token=""
        if user:
            token=self.setTokenUser(user['username'])
            #print(user)
            user['token']=token
        cursor.close()
        con.close()
        return user
    
    def setTokenUser(self, username):
        # connectar BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        # generar Token
        token=self.getHash() #token=self.getHash(username)
        # Update a BBDD camp Token al usuari per username
        print(type(token))
        query = "UPDATE User SET token ='" + token + "' WHERE username = '" + username +"'"
        # print(query)
        cursor.execute(query)
        con.commit()
        # Close BBDD
        cursor.close()
        con.close()
        return token
    
    def getHash(self):
        milliseconds = str(time() * random.randrange(10000))
        data=  milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""
    
    def getHash2(self,username):
        milliseconds = str(time() * 1000)
        data=username + milliseconds
        hash_object =  hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""


class ChildDAO:

    def getChilds(self,id_user):
        return  "TO-DO Get Childs"
   
'''
dao=UserDAO()
u=dao.getUserByToken("5b8656c4f2dc8461550dc44543e4fdb23a481c1d76fcf2e1353fe5425f50ee40")
print(u)
u=dao.getUserByToken("123455")
print(u)
'''