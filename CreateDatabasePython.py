#pip install mysql-connector-python
import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "manager")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #creating a new database  
    #cur.execute("drop database PythonDB3")
    cur.execute("create database PythonDB3")  
  
    #getting the list of all the databases which will now include the new database PythonDB  
    #dbs = cur.execute("show databases")  
    cur.execute("show databases")
except:  
    myconn.rollback()  
  
for x in cur:  
        print(x)  
          
myconn.close()   