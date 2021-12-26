import mysql.connector as db
import urllib.request
import pickle
import os

#Internet baigaa esehiig testlev
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

#Hadgalah Ugugluud
sql = (
    "INSERT INTO STUDENT(FIRST_NAME, LAST_NAME, AGE, SEX, SCODE)"
    "VALUES ('Battseren', 'Badral', 20, 'M', 'B160910083')"
)

#Ugugdliin base ee internet baigaa esehees hamaarch hadgalah
if(connect()==True):
    mydb=db.connect(host="localhost",    user="root",    passwd="",  database="test")
    cursor = mydb.cursor()
    if(mydb):

        try:
            cursor.execute(sql)
            mydb.commit()

        except:
            mydb.rollback()

        print("Ugugdul hadgalagdlaa!!!")
    else:
        print("Ugugdul hadgalagdsangui!!!")
else:
    pickle.dump(sql, open("lab2.txt","wb"))
    print("LOCALd hadgallaa")






