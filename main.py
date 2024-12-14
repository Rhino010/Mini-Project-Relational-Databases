# Imports from all files to incorporate all classes and functionality into main.py
from book import add_book, borrow_book, return_book, find_book, show_all_books
from user import add_user, show_all_users, view_user_details, user_borrowed_books
from author import add_author, find_author, show_all_authors
from connect_mysql import connect_database
import os

def main():
    conn = connect_database()
    if conn is not None:
        try:
            while True:
                # The cursor is the python method that stores the data coming back from the database after the data has been called.
                cursor = conn.cursor()
                invalid = "Invalid selection, please try again."
                
                print("Welcome to the Library Management System with Database Integration!")
                print("--Main Menu--\nPlease select from the following options:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit Program")
                choice = input("Please choose the number of your selection.\n")

                if choice == '1':
                    os.system('cls||clear')
                    print("--Book Operations Menu--\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
                    selection = input("Please select from the above menu:\n")
                    if selection == '1':
                        add_book()
                    elif selection == '2':
                        book_id = int(input("What is the book ID you would like to check out?"))
                        borrow_book(book_id)
                    elif selection == '3':
                        book_id = input("What is the ID of the book you're returning?\n")
                        return_book(book_id)
                    elif selection == '4':
                        find_book()
                    elif selection == '5':
                        show_all_books()
                    else:
                        print(invalid)

                elif choice == '2':
                    os.system('cls||clear')
                    print("--User Operations--\n1. Add a new user\n2. View User Details\n3. Display all users\n4. Show User's Current Books")
                    selection = input("Please select from the above menu:\n")
                    if selection == '1':
                        add_user()
                    elif selection == '2':
                        view_user_details()
                    elif selection == '3':
                        show_all_users()
                    elif selection == '4':
                        user_borrowed_books()
                    else:
                        print(invalid)

                elif choice == '3':
                    os.system('cls||clear')
                    print("--Author Operations--\n1. Add a new author\n2. View author details\n3. Display all authors")
                    selection = input("Please select from the above menu:\n")
                    if selection == '1':
                        add_author()
                    elif selection == '2':
                        find_author()
                    elif selection == '3':
                        show_all_authors()
                    else:
                        print(invalid)

                elif choice == '4':
                    os.system('cls||clear')
                    print("Shutting down......")
                    break
                else:
                    print(invalid)
        
        except Exception as e:
            print(f"Unexcpected error: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()