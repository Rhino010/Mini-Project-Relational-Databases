WELCOME TO THE LIBRARY MANAGEMENT SYSTEM

-This system will allow you to:
    -Add books to a library's inventory.
    -Have a specific user borrow from these books and track which books they have checked out.
    -Deduct the book from the user's record of checked out books when returned and show it is again available at the library.
    -Search for a particular book in the library's inventory list.
    -Browse the entire library's inventory to see what books are regularly carried.
        -This portion will also show if they are available to check out or not.

-Main Menu-
    -This portion of the program will allow you to select the category you would like to start with
        -Typing the corresponding number to the operation you wish to access and pressing enter will bring the sub menu of that category
        Example:
            Main Menu:
            1. Book Operations
            2. User Operations
            3. Author Operations
            4. Quit

            Typing '1' and pressing 'Enter' will take you to the sub menu with all operations to interact with the book inventory.

-Book Operations-
    -This menu contains all operations to access the library's book inventory

    1. Add a new book
        -Here you will be prompted to add the title, author, genre, publication year.
            -It is assumed that books will not be added to the inventory until they are physically in the library so 'availabile' will be
            set to 'Yes' automatically.
    2. Borrow a book
        -You will be prompted to provide the title of the book the book to be borrowed.
            -The program will check if it is carried by the library and if it is available to borrow
            -If all criteria are met, it will prompt the user for a library user's ID.
            -It will then check if the user's ID is valid. 
            -If all criteria are met, then the book will be added to the user's borrowed book list
    3. Return a book
        -This will ask for a book title to be returned.
        -Type in the book title and press 'Enter'
            -After it will be checked that the book is intially carried by the library and has been checked out
            -If the above criteria is met it will prompt for the library user's ID returning the book
            -This ID will be checked to make sure the user is valid
            -Once this is done it will show remove the book from the user's borrowed book list and then
            show the book available to borrow again in the library's inventory
    4. Search for a book
        -Here you will be prompted for the book title you wish to search for.
            -This title will be searched for in the library inventory
                -If it is carried by the library you will be shown the title and whether it is currently avaialable to borrow.
                -If it is not carried, the program will inform you that this book is not carried by the library
    5. Display all books
        -Selecting this option will bring a list of all books and all information available i.e. Title, Author, Genre, Publication Year
        and whether it is currently available to borrow.

-User Operations-
    -This menu contains all available operations for interacting with user accounts

    1. Add a user
        -Selecting this will prompt for a user's numerical ID to be input, as well as their name
        -After inputing this information it will be added to the library's records
    2. View user details
        -This option will prompt for the user's ID
            -The library's user records will be checked to ensure that ID currently exists in the system
            -If the user ID exists, the User ID, Name, and Books they currently have borrowed will be shown
    3. Display all users
        -Here you will find a list of all user's, their IDs, names, and the books each has currently borrowed
    4. View User's Borrowed books
        -by selecting this option and providing the user's ID, you will be able to see all the books the user currently has checked out.
        
-Author Operations-
    -This section will allow you to interact with author information contained withing the program
    
    1. Add a new author
        -Selecting this will prompt for an author's name as well as a bio of the author
        -After this information is entered and 'Enter' is selected after each input, it will be added to the library's system
    2. View author details
        -This option will ask for the author's name you are searching for.
        -If the library has this information, you will be shown the author name as well as a bio of the author.
        -If the author is not in the system you will be informed that there is no information contained.
    3. Display all authors.
        -Selecting this will show the names and bios of all authors that have currently been input in the library's system

I hope you find this program useful to track books, users, and authors of your library.
Thank you for choosing the Library Management System!