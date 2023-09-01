import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "manager",database = "PythonDB3")  
#creating the cursor object  
cur = myconn.cursor()  
sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"  
  
#The row values are provided in the form of tuple   
val = ("Satish", 110, 25000.00, 201, "India")  
  
try:  
    #inserting the values into the table  
    cur.execute(sql,val)  
  
    #commit the transaction   
    myconn.commit()  
      
except:  
    myconn.rollback()  
  
print(cur.rowcount,"record inserted!")  
myconn.close() 