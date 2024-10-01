import sqlite3  
conn = sqlite3.connect('farmer.db') 

# if mysql installed  
# import mysql.connector as mc 
# conn=mc.connect(host ='localhost' , user = 'root' , password = 'Jigar@975919',database="dbname")

query = "create table farmerdata (N int,P int,k int,t int,h int,ph int,r int,prediction int)"
curs_obj = conn.cursor()

curs_obj.execute(query)
print("successfully created database and table!")
conn.commit()
curs_obj.close()
conn.close()