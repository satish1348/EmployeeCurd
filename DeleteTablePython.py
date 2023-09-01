import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "manager",database = "PythonDB3")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #Deleting the employee details whose id is 110  
    cur.execute("delete from Employee where id = 104")  
    myconn.commit()  
except:  
      
    myconn.rollback()  
  
myconn.close()  