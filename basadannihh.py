from sqlite3 import *
from sqlite3 import Error
from os import *

def create_connect(path:str):
    connection=None
    try:
        connection=connect(path)
        print("Ühendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection

def execute_query(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Table on loodud või andmed on sisestatud")
    except Error as e:
        print(f"Tekkis viga: {e}")

def execute_read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
       print(f"Tekkis viga: {e}")

def execute_insert_query(connection,data):
    query = "INSERT INTO users(Name,Lastname,Age,Birthday,Gender,Email,AutoId) VALUES(?,?,?,?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

def dropTable(connection,table):
    try:
        cursor=connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table}") 
        connection.commit()
    except Error as e:
        print(f"Tekis viga: {e}")

def search_user_name(connection,name):
    try:
        query = "SELECT * FROM users WHERE Name = ?"
        cursor = connection.cursor()
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekis viga: {e}")


create_users_table = """
CREATE TABLE IF NOT EXISTS users(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lastname TEXT NOT NULL,
Age INTEGER NOT NULL,
Birthday DATE NOT NULL,
Gender TEXT NOT NULL,
Email TEXT NOT NULL,
AutoId INTEGER,
FOREIGN KEY (AutoId) REFERENCES auto(Id)
)
"""

create_auto_table = """
CREATE TABLE IF NOT EXISTS auto(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Model TEXT NOT NULL,
Colour TEXT NOT NULL
)
"""

insert_users = """
INSERT INTO
users(Name,Lastname,Age,Birthday,Gender,Email,AutoId)
VALUES
("Roman","Sandakov",18,'2005-06-17',"male","sand2@gmail.com", 1),
("Jimmmy","Beast",31,'1993-02-16',"male","mrbeast@mail.au", 2),
("Patrik","Bateman",42,'1982-12-30',"male","awsn@dsjk.ny", 3)
"""

insert_auto = """
INSERT INTO
auto(Model, Colour)
VALUES
("BMW", "Red"),
("Mercedes", "Blue"),
("Tesla", "Green")
"""

select_users = "SELECT * FROM users"
select_auto = "SELECT * FROM auto"
#select_auto = "SELECT users.Name,users.Lastname,users.Age,users.Birthday,users.Gender,users.Email,users.Auto.Nimetus from users INNER JOIN gender ON users.AutoId=auto.Id"

filename = path.abspath(__file__)
dbdir = filename.rstrip('basadannihh.py')
dbpath = path.join(dbdir,"data.db")
conn = create_connect(dbpath)

execute_query(conn, create_auto_table) 
execute_query(conn, create_users_table) 
execute_query(conn, insert_auto) 
execute_query(conn, insert_users) 

users = execute_read_query(conn, select_users)
print("Kasutajate tabel 1:")
for user in users:
    print(user)

auto = execute_read_query(conn, select_auto)
print("Kasutajate tabel 2:")
for auto in auto:
    print(autos)

insert_user = (
    input("Eesnimi:"),
    input("Perenimi:"),
    input("Vanus:"),
    input("Birthday:"),
    input("Sugu:"),
    input("mail:"),
    input("autoId:"),
)
search_name = input("search name: ")
found_users = search_user_name(conn, search_name)
if found_users:
    print("users:")
    for user in found_users:
        print(user)
else:
    print("not found")

execute_insert_query(conn, insert_user)

dropTable(conn,table)



