import sqlite3 as sql


def sql_connection():

    connector = sql.connect('collections.db')
    print("Connection is established")
    return connector
    

def sql_table(connection):

    cursorObj = connection.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS movies(id integer, name text, releasing_year integer, type text)")
    #cursorObj.execute("drop TABLE movies")
    connection.commit() 


def addMovie(connection,entities):
  
    cursorObj = connection.cursor()
    cursorObj.execute("INSERT INTO movies(id, name, releasing_year, type) VALUES(?, ?, ?, ?)", entities)
    connection.commit()

def userMovie():
  
    print("Enter the movie data as per sequence (id,name,releasingYear,Genre)::")
    data =()
    
    for _ in range(1,5):
        data = data + (input(),)
    return data


def listMovie(connection):

    cursorObj = connection.cursor()
    cursorObj.execute("SELECT * FROM  movies")
    [print(row) for row in cursorObj.fetchall()]
    connection.commit()


def searchMovie(connection,searchInput=None):

    cursorObj = connection.cursor()
    sql ="SELECT * FROM  movies "
    column = searchInput[0].lower()
    
    if len(searchInput)>0 :
        sql = sql + f"where {column} in ('{searchInput[1]}')" 
    
    cursorObj.execute(sql)
    [print(row) for row in cursorObj.fetchall()]

    if len([[print(row) for row in cursorObj.fetchall()]]) > 0:
       print("Movies found")
    else:
      print("No Movies found")
    connection.commit()


def userSearchMovie():

    column = input()
    value = input()
    return column,value


def menu():
    
    print("Enter the following keywords to perform its corresponding tasks : \n 1. 'a' for adding the movie \n 2. 'l' for list them all \n 3. 'f' for searching the movie \n 4. 'q' for quitting")
    menu_input = input(" ")
    
    while menu_input != 'q':
        
        if menu_input == 'a':
            entities = userMovie()
            addMovie(connection,entities)
            print("Movie is successfully added to your collection!!")
        
        elif menu_input == 'l':
            print("The movies are listed below: ")
            listMovie(connection)
            print(" ")
        
        elif menu_input == 's':
            print("Enter the movie data as per sequence (Name,value)::")
            entities=userSearchMovie()
            searchMovie(connection,entities)
        
        else:
            print("Kindly enter the valid input.!!")
        menu_input = input("Want to perform another then choose the given options or you can exit by pressing q: ")    
    print("Bye!! Have a nice day.")

connection = sql_connection()
sql_table(connection)


menu()
