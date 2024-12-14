from connect_mysql import connect_database
    
conn = connect_database()
cursor = conn.cursor()

# Function to prompt the user for a user's information
def add_user():
    try:
        user_name = input("Please enter the user's name:\n")
        library_id = int(input("Please provide the user a unique ID number:\n"))
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (user_name, library_id))
        conn.commit()
        print(f"User with ID: {library_id} and Name: {user_name} has been added.")
    except ValueError:
        print("User ID must be a number.")
# Function to print out all of a selected user's information
def view_user_details():
    user_id = int(input("Enter the user's ID."))
    get_user_query = "SELECT id, name, library_id FROM users WHERE id = %s"
    cursor.execute(get_user_query, (user_id, ))
    user_info = cursor.fetchone()
    # print(user_info)
    print(f"User ID: {user_info[0]}, User Name: {user_info[1]}, Library ID: {user_info[2]}")
# Function to print out all users currently held in the user dictionary
def show_all_users():
    get_users_query = "SELECT * FROM users"
    cursor.execute(get_users_query)
    users = cursor.fetchall()
    for user in users:
        print(f"Name: {user[1]},    Library ID: {user[2]}")

# Function to add a book to each instance of a user when checking out a book with the given user's id number
def user_borrowed_books():
    user_id = int(input("Enter the user's ID:\n"))
    borrowed_books_query = "SELECT book_id FROM borrowed_books WHERE user_id = %s"
    cursor.execute(borrowed_books_query, (user_id, ))
    users_books = cursor.fetchall()
    try:
        for book in users_books:
            get_title_query = "SELECT title FROM books WHERE id = %s"
            cursor.execute(get_title_query, (book[0], ))
            this_book = cursor.fetchall()
            print(f"Title: {this_book[0][0]}")
    except Exception as e:
        print(f"Error: {e}")

def check_valid_user(user_id):
    check_query = "SELECT id FROM users WHERE id = %s"
    cursor.execute(check_query, (user_id, ))
    user = cursor.fetchone()
    return user
