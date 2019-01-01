import mysql.connector
from random import randint

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password = "123pass",
  database = "mydatabase"
)


myCursor = mydb.cursor()

#myCursor.execute("CREATE TABLE students(name VARCHAR(255), studentID VARCHAR(255))")  #Use this command once to create a new table on the database
#myCursor.execute("SHOW TABLES")    #COMMAND TO SHOW THE TABLE FROM THE DATABASE


deleteByName = "DELETE FROM students WHERE name = %s"
deleteByID = "DELETE FROM students WHERE studentID = %s"
orderByName = "SELECT * FROM students ORDER BY name"

val = [
  ('John Doe', '7315342'),
  ('Amy Adams', '7845693'),
  ('Hannah Montana', '7124583'),
  ('Michael Jordan', '8412579'),
  ('Sandy Hill', '9463278'),
  ('Betty White', '8411235'),
  ('Richard Hammond', '8456721'),
]


def insertInTable():
  insert = "INSERT INTO students (name, studentID) VALUES (%s, %s)"
  newName = raw_input("Enter the student Name: ")
  newStudentId = raw_input("Enter the student ID: ")
  myCursor.execute(insert, (newName, newStudentId))
  mydb.commit()


def deleteByName():
  deleteByName = "DELETE FROM students WHERE name = %s"
  name = raw_input("Enter the student Name: ")
  myCursor.execute(deleteByName, (name,))
  mydb.commit()


def deleteByID():
  deleteByName = "DELETE FROM students WHERE studentID = %s"
  studentID = raw_input("Enter the student ID: ")
  myCursor.execute(deleteByName, (studentID,))
  mydb.commit()

def viewTable():
  myCursor.execute("SELECT * FROM students")
  myResult = myCursor.fetchall()
  for x in myResult:
    print(x)


def viewTableInOrder():
  myCursor.execute("SELECT * FROM students ORDER BY name")
  myResult = myCursor.fetchall()
  for x in myResult:
    print(x)




quit = 'N'
while(quit != 'Q'):
  print("\nChoose one of the following options: ")
  print("1 to insert in the table")
  print("2 to Delete from the table by Name")
  print("3 to Delete from the table by ID")
  print("4 to view the table")
  print("5 to view the table in order")
  print("Enter Q to quit")
  choice = raw_input("Enter your choice: ")

  if (choice == '1'):
    insertInTable()
  if (choice == '2'):
    deleteByName()
  if (choice == '3'):
    deleteByID()
  if (choice == '4'):
    viewTable()
  if (choice == '5'):
    viewTableInOrder()
  if(choice == 'Q'):
    quit = 'Q'














