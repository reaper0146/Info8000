from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
import db_modules.db_functions as dbF
app = Flask(__name__, template_folder='templetes')

#dbF.init_db()

@app.route('/')
def hello():
    return render_template("main.html",title= 'User Management')

@app.route('/reset')
def db_reset():
    dbF.init_db()
    return redirect('/')

#resource enroll form
@app.route('/resource/add_form')
def resource_add():
    return render_template("resource_form.html",title= 'Add resource')

@app.route('/resource/add_form', methods=['POST'])
def resource():
    rid = request.values['rid']
    rname = request.values['rname']
    rdesc = request.values['rdesc']
    dbF.addResource(rid,rname,rdesc)
    df = dbF.getTable('resources')
    temp = df.to_records()
    print(temp)
    return f"{temp}"

#scanner assign form
@app.route('/scanner/add_form')
def scanner_add():
    return render_template("scanner_form.html",title= 'Assign Scanner')

@app.route('/scanner/add_form', methods=['POST'])
def scanner():
    scanid = request.values['scanid']
    rid = request.values['rid']
    query = "SELECT * FROM resources" + " WHERE rid = '" + str(rid) +"'"
    print(query)
    con = dbF.dbConection()
    df = pd.read_sql(query,con)
    if len(df) == 0:
        return "Resouce not found"
    else:
        dbF.addScanner(scanid,rid)
        df = dbF.getTable('rfidscanner')
        temp = df.to_records()
        print(temp)
        return f"{temp}"

#user enroll form
@app.route('/user/add_form')
def user_add():
    return render_template("user_form.html", title= 'Add User', status=['True', 'False'])

@app.route('/user/add_form', methods=['POST'])
def user():
    uid = request.values['userid']
    fname = request.values['fname']
    lname = request.values['lname']
    access = request.values['access']
    dbF.addUser(uid,fname,lname,access)
    df = dbF.getTable('users')
    temp = df.to_records()
    print(temp)
    return f"{temp}"

#rfid card assigning form
@app.route('/user/card_form')
def rfidCard_add():
    return render_template("rfidcard_form.html", title= 'Assign Card to User')

@app.route('/user/card_form', methods=['POST'])
def rfidCard():
    usrid = request.values['usrid']
    rfid = request.values['rfid']
    dbF.assignCard(rfid,usrid)
    df = dbF.getTable('rfidcard')
    temp = df.to_records()
    return f"{temp}"

#resource access form
@app.route('/user/access_form')
def resourceAccess_add():
    return render_template("resourceAccess_form.html", title= 'User resource access')

@app.route('/user/access_form', methods=['POST'])
def resourceAccess():
    usrid = request.values['usrid']
    rid = request.values['rid']
    access = request.values['access']
    dbF.assignResource(usrid, rid)
    update = "UPDATE users SET access_status = '" +str(access) +"' WHERE userid = '" + str(usrid) +"'"
    with dbF.dbConection() as con:
        con.execute(update)
        con.commit()
    df = dbF.getTable('users')
    temp = df.to_records()
    print(temp)
    return f"{temp}"

#access log form
@app.route('/user/test_access')
def accesslog_add():
    return render_template("access_form.html", title= 'Access log form')

@app.route('/user/test_access', methods=['POST'])
def accesslog():
    usrid = request.values['usrid']
    rfidCard = request.values['rfid']
    rid = request.values['rid']
    rname = request.values['rname']
    status = request.values['status']
    reason = request.values['reason']

    dbF.accessLog(usrid,rfidCard,rid,rname,status,reason)
    df = dbF.getTable('accesslog')
    temp = df.to_records()
    print(temp)
    return "Log entry created"

@app.route('/log')
def accessLog_get():
    data = []
    df = dbF.getTable('accesslog')
    data = df.to_records()
    print(data)
    return render_template("access_log.html",title= 'Access Log', users=data)

app.run(debug=True)