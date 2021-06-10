#database functions module

import sqlite3
import os
import pandas as pd

package_dir = os.path.dirname(os.path.abspath(__file__))
#create connection to database
def dbConection():
    return sqlite3.connect('management.db')

def init_db():
    with dbConection() as con, open(f"{package_dir}/create_db.sql") as script:
        con.executescript(script.read())

#add resource
def addResource(rid, rname, rdesc):
    with dbConection() as con:
        con.execute("INSERT INTO resources(rid, rname, rdesc) VALUES (?, ?, ?)",(rid, rname, rdesc))

#add scanner
def addScanner(scanid, rid):
    with dbConection() as con:
        con.execute("INSERT INTO rfidscanner(scannerid, rsid) VALUES (?,?)",(scanid,rid))

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
def accessLog(usrid,rfidcard,rid,rname,status,reason):
    with dbConection() as con:
        logs = [(str(usrid), str(rfidcard), str(rid), str(rname), str(status), str(reason))]
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