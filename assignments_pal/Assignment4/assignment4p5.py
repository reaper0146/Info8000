import sqlite3
import pandas as pd

def dbConection():
    return sqlite3.connect('management.db')

#all enabled users
def enabledUsersLog():
    with dbConection() as con:
        df = pd.read_sql("SELECT userid, fname, lname, rfidcode, approval_status FROM accesslog, users WHERE users.access_status ='True' AND accesslog.usrsid = users.userid GROUP BY users.userid",con)
        return df

#singleDayUsers
def dayUserslog(argm):
    with dbConection() as con:
        temp = "SELECT userid, fname, lname, resid, resname FROM accesslog, users WHERE accesslog.usrsid = users.userid AND access_time between '" + argm +" 00:00:00' AND '"+argm+" 23:59:59'"
        df = pd.read_sql(temp,con)
        return df

#Users most used scanners
def mostused(argm):
    with dbConection() as con:
        temp = "SELECT scannerid FROM accesslog, rfidscanner WHERE accesslog.resid = rfidscanner.rsid and accesslog.usrsid = '" + str(argm)+"' GROUP BY accesslog.resid ORDER BY COUNT(accesslog.resid)"
        df = pd.read_sql(temp,con)
        return df

#failed access due to use disabled
def failed_accessed(argm):
    with dbConection() as con:
        temp = "SELECT rid, rname FROM accesslog, resources WHERE accesslog.resid = resources.rid AND accesslog.approval_status='False' GROUP BY resources.rid"
        df = pd.read_sql(temp,con)
        return df

pd_enabled = enabledUsersLog()
date = '2021-03-26'
pd_day = dayUserslog(date)
userid ='U023'
pd_mostUsed = mostused(userid)
pd_failed = failed_accessed(userid)

print("\nEnables users")
print(pd_enabled)
print("\nDay login for " + date)
print(pd_day)
print("\nMost used scanners by userid", str(userid))
print(pd_mostUsed)
print("\nFailed access due to user access disabled")
print(pd_failed)
print('\n')