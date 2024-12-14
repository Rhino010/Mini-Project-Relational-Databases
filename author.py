from connect_mysql import connect_database

conn = connect_database()
cursor = conn.cursor()

# Function to add an author to the dictionary
def add_author():
    name = input("Enter the author's name:\n").lower()
    bio = input("Enter some information about the author:\n")
    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    cursor.execute(query, (name, bio))
    conn.commit()
    # Returns the id of the author to serve as a dual purpose in the add_book function
    id_query = "SELECT id FROM authors WHERE name = %s"
    cursor.execute(id_query, (name, ))
    author_id = cursor.fetchone()
    print(f"Author: {name.title()} with ID: {author_id[0]} has been added.")



# Function to search the authors dictionary for a specific author
def find_author():
    try:
        author_name = input("What is the name of the author?\n").lower()
        author_query = "SELECT name, biography FROM authors WHERE name = %s"
        cursor.execute(author_query, (author_name, ))
        found_author = cursor.fetchone()
        if found_author is not None:
            print(f"Author found, here are the details: {found_author}")
        else:
            print("Author not found.")
    except ValueError:
        print("Please be sure to enter the authors name, and try again.")

# Function to print out all authors from the authors dictionary
def show_all_authors():
    show_all_query = "SELECT * FROM authors"
    cursor.execute(show_all_query)
    authors = cursor.fetchall()
    for author in authors:
        print(author)