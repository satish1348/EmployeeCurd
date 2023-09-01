import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "manager",database = "PythonDB3")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #adding a column branch name to the table Employee  
    cur.execute("alter table Employee add branch_name varchar(20) not null")  
    print("Table Employee Altered Successfully")
except:  
    myconn.rollback()  
  
myconn.close()  