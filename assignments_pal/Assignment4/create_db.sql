--PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS accesslog;
DROP TABLE IF EXISTS resourceaccess;
DROP TABLE IF EXISTS rfidscanner;
DROP TABLE IF EXISTS resources;
DROP TABLE IF EXISTS rfidcard;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    userid TEXT PRIMARY KEY NOT NULL,
    fname TEXT,
    lname TEXT,
    access_status TEXT
);

CREATE TABLE rfidcard (
    rfcode VARCHAR(12) PRIMARY KEY NOT NULL,
    usrid TEXT,
    Foreign Key(usrid) references users(userid)
);

CREATE TABLE resources (
    rid TEXT PRIMARY KEY NOT NULL,
    rname TEXT,
    rdesc TEXT
);


CREATE TABLE rfidscanner (
    scannerid TEXT PRIMARY KEY NOT NULL,
    rsid TEXT NOT NULL,
    Foreign Key(rsid) references resources(rid)
);

CREATE TABLE resourceaccess (
    num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    usrrid TEXT NOT NULL,
    ressid TEXT NOT NULL,
    Foreign Key(usrrid) references users(userid),
    Foreign Key(ressid) references resources(rid)
);

CREATE TABLE accesslog (
    num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    usrsid TEXT NOT NULL,
    rfidcode TEXT NOT NULL,
    resid TEXT NOT NULL,
    resname TEXT NOT NULL,
    access_time datetime default CURRENT_TIMESTAMP,
    --fname TEXT NOT NULL,
    --lname TEXT NOT NULL,
    approval_status TEXT NOT NULL,
    reason TEXT,
    Foreign Key(resid) references resources(rid),
    Foreign Key(rfidcode) references rfidcard(rfcode),
    Foreign Key(usrsid) references users(userid),
    Foreign Key(resname) references resources(rname)
    --Foreign Key(lname) references users(lname)
);
