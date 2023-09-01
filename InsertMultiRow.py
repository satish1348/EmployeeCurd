import mysql.connector  
      
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "manager",database = "PythonDB3")  
  
#creating the cursor object  
cur = myconn.cursor()  
sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"  
val = [("John", 102, 25000.00, 201, "Newyork"),("David",103,25000.00,202,"Port of spain"),("Nick",104,90000.00,201,"Newyork")]  
      
try:  
    #inserting the values into the table  
    cur.executemany(sql,val)  
  
    #commit the transaction   
    myconn.commit()  
    print(cur.rowcount,"records inserted!")  
      
except:  
    myconn.rollback()  
  
myconn.close()  