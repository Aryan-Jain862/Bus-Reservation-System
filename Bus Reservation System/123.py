import MySQL.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='@ARYAN1234')
print (mydb.connection_id)
