import db_functions as dbF

#test data
resources = [
    ('R023', 'Resource1', 'Resource in left wing storage'),
    ('R176', 'Resource2', 'Resource in right wing storage'),
    ('R096', 'Resource3', 'Resource in basement'),
    ('R146', 'Resource4', 'Resource in central storage')]

rfidscanners = [('RSc007','R023'), ('RSc017','R146'), ('RSc194','R096'), ('RSc023','R176')]

dbF.init_db()
dbF.test_data(resources, rfidscanners)
dbF.tableCommit()

df_resources = dbF.getTable("resources")
df_rfidscanner = dbF.getTable("rfidscanner")

dbF.addUser('U023','Amelia','Singh', 'True')
dbF.addUser('U186','Virat','Kolhi', 'True')
dbF.addUser('U010','Lionel','Messi', 'True')
dbF.addUser('U278','Diana','Prince', 'False')

df_user = dbF.getTable("users")

print("\nUsers Table")
print(df_user)

dbF.assignResource('U023', 'R146')
dbF.assignResource('U186', 'R096')
dbF.assignResource('U278', 'R023')
df_resourceAccess = dbF.getTable("resourceaccess")
dbF.assignCard('ASDJLKUH9876','U023')
dbF.assignCard('GFBJPKYT1985','U186')
dbF.assignCard('PLDHWJDH0849','U278')

dbF.disableUser("U010")

dbF.checkAccess('RSc017',"ASDJLKUH9876")
dbF.checkAccess('RSc194',"GFBJPKYT1985")
dbF.checkAccess('RSc017',"ASDJLKUH9876")
dbF.checkAccess('RSc007',"PLDHWJDH0849")

dbF.tableCommit()
df_rfidcard = dbF.getTable("rfidcard")
df_user = dbF.getTable("users")
df_accesslog = dbF.getTable("accesslog")

print("\nUsers Table After Disable")
print(df_user)
print("\nRFID Cards Table")
print(df_rfidcard)
print("\nResources Table")
print(df_resources)
print("\nRFID Scanners Table")
print(df_rfidscanner)
print("\nResource Access Table")
print(df_resourceAccess)
print("\n")
print("Access log")
print(df_accesslog)
print("\n")

dbF.tableCommit()