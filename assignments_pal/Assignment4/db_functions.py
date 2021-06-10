#database functions module

import sqlite3
import numpy as np
import random
import pandas as pd

random.seed(8000)
np.random.seed(8000)

#create connection to database
def dbConection():
    return sqlite3.connect('management.db')

def init_db():
    with dbConection() as con, open("create_db.sql") as script:
        con.executescript(script.read())

#initialize database with test data
def test_data(resources, rfidscanners):
    with dbConection() as con:
        
        for resource in resources:
            con.execute("INSERT INTO resources(rid, rname, rdesc) VALUES (?,?,?)",resource)
        
        for scanner in rfidscanners:
            con.execute("INSERT INTO rfidscanner(scannerid, rsid) VALUES (?,?)",scanner)
       
#add user
def addUser(uid, fname, lname, acc_stat):
    with dbConection() as con:
        con.execute("INSERT INTO users(userid, fname, lname, access_status) VALUES (?, ?, ?, ?)",(uid, fname, lname, acc_stat))

#assign card to user
def assignCard(rfid, uid):
    with dbConection() as con:
        con.execute("INSERT INTO rfidcard(rfcode, usrid) VALUES (?, ?)",(rfid, uid))

#disable user
def disableUser(uid):
    with dbConection() as con:
        con.execute("UPDATE users set access_status = ? where userid = ?",('False',uid))

#assign resource
def assignResource(uid, rid):
    with dbConection() as con:
        con.execute("INSERT INTO resourceaccess(usrrid, ressid) VALUES (?, ?)",(uid, rid))

#check access
def checkAccess(scid, rfid):
    with dbConection() as con:
        temp = "SELECT * FROM rfidscanner where scannerid = \'" + str(scid) +"\'"
        df_scanner = pd.read_sql(temp,con)
        temp = "SELECT * FROM resourceaccess where ressid = \'" + str(df_scanner['rsid'][0]) +"\'"
        df_raccess = pd.read_sql(temp,con)
        temp = "SELECT * FROM users where userid = \'" + str(df_raccess['usrrid'][0]) +"\'"
        df_user = pd.read_sql(temp,con)
        temp = "SELECT * FROM resources where rid = \'" + str(df_scanner['rsid'][0]) +"\'"
        df_resource = pd.read_sql(temp,con)
        
        if df_user['access_status'][0] == "True":
            logs = [(str(df_user['userid'][0]), str(rfid), str(df_resource['rid'][0]), str(df_resource['rname'][0]), 'True', '')]
        elif df_user['access_status'][0] == "False":
            logs = [(str(df_user['userid'][0]), str(rfid), str(df_resource['rid'][0]), str(df_resource['rname'][0]), 'False', "User left building or doesn't have access")]
        for log in logs:
                con.execute("INSERT INTO accesslog(usrsid, rfidcode, resid, resname, approval_status, reason) VALUES (?, ?, ?, ?, ?, ?)",log)
        

#commit changes    
def tableCommit():
    with dbConection() as con:
        con.commit()

#return tables as pandas dataframe
def getTable(arg):
    with dbConection() as con:
        if arg == "users":
            df = pd.read_sql("SELECT * FROM users",con)
        elif arg == "resources":
            df = pd.read_sql("SELECT * FROM resources",con)
        elif arg == "rfidcard":
            df = pd.read_sql("SELECT * FROM rfidcard",con)
        elif arg == "rfidscanner":
            df = pd.read_sql("SELECT * FROM rfidscanner",con)
        elif arg == "resourceaccess":
            df = pd.read_sql("SELECT * FROM resourceaccess",con)
        elif arg == "accesslog":
            df = pd.read_sql("SELECT * FROM accesslog",con)
        else:
            df = "Wrong Table name"
        return df