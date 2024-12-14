from connect_mysql import connect_database
from user import check_valid_user
from author import add_author
from datetime import date, datetime

conn = connect_database()
cursor = conn.cursor()
    
# Function to add a book to library_books dictionary
def add_book():
    try:
        author_id = int(input("What is the corresponding author id number?\n"))
        verify_author_query = "SELECT id FROM authors WHERE id = %s"
        cursor.execute(verify_author_query, (author_id, ))
        author = cursor.fetchone()
        if author is not None:
            title = input("What is the title of the book?\n").lower()
            isbn = int(input("What is the ISBN number of this book?\n"))
            publication_date = input("What is the publication date as (YYYY-MM-DD)?\n")
            query = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s ,%s, %s, %s, True)"
            cursor.execute(query, (title, author_id, isbn, publication_date))
            conn.commit()
            print(f"'{title.title()}' has been successfully added.")
        else:
            print("That ID does not match. Please add the author to our database first and we will provide you with the author's ID.")
            add_author()
    except Exception as e:
        print(f"The following error occurred: {e}\nPlease check your inputs and try again.")   

# Function to reset a books availability to False in the library_books dictionary
def borrow_book(book_id):
    book_check_query = "SELECT id, title FROM books WHERE id = %s AND availability = 1"
    cursor.execute(book_check_query, (book_id, ))
    book = cursor.fetchone()
    if book:
        print(book)
        choice = input(f"{book[1].title()}, with book ID {book[0]}, is currently available to check out. Would you like to rent this? Type 'Yes' or 'No'.").lower()
        if choice == 'yes':
            try:
                user_id = int(input("Enter the user's ID:\n"))
                if check_valid_user(user_id):
                    today = input("Enter today's date as 'YYYY-MM-DD'\n")
                    update_borrowed_query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                    cursor.execute(update_borrowed_query, (user_id, book[0], today))
                    conn.commit()
                    update_availability_query = "UPDATE books SET availability = 0 WHERE id = %s"
                    cursor.execute(update_availability_query, (book_id, ))
                    conn.commit()
                    print(f"User with ID {user_id} has successfully checked out '{book[1].title()}'")
                else:
                    print("There is no user with that ID, please try again.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Transaction canceled")        
    else:
        print("That particular book is currently unavailable.")
# Function to set the availability to True for a book after function is called
def return_book(book_id):
    try:
        select_query = "SELECT book_id FROM borrowed_books WHERE book_id = %s"
        cursor.execute(select_query, (book_id, ))
        found_book = cursor.fetchall()
        if found_book is not None:
            delete_query = "DELETE FROM borrowed_books WHERE book_id = %s"
            cursor.execute(delete_query, (book_id, ))
            update_query = """UPDATE books
                                SET availability = 1
                                WHERE id = %s"""
            cursor.execute(update_query,(book_id, ))
            conn.commit()
            print("Thank you, we hope you enjoyed your book.")
        else:
            print("That book does not appear to have been checked out. Please double check the ID.")

    except Exception as e:
        print(f"Error occurred: {e}")
# Function to find a particular book in the dictionary library_books and show whether it is currently available or not.
def find_book():
    try:
        title = input("Enter the book title.").lower()
        title_query = "SELECT title, isbn, publication_date, availability FROM books WHERE title = %s"
        cursor.execute(title_query, (title, ))
        book = cursor.fetchone()
        if book[-1] == 1:
            print(f"Title: {book[0]} ISBN: {book[1]}, Publication Date: {book[2]}, Available")
        else:
            print(f"Title: {book[0]} ISBN: {book[1]}, Publication Date: {book[2]}, Checked Out")
    except Exception as e:
        print(f"Error occurred: {e}") 

# Function to print out all the books in the library_books dictionary and display all books with all information had on them.
def show_all_books():
    books_query = "SELECT * FROM books"
    cursor.execute(books_query)
    books = cursor.fetchall()
    for book in books:
        if book[-1] == 1:
            print(book[0:-1], "Available")
        else:
            print(book[0:-1], "Checked Out")