import os
from Book import Book

class LBMS:

    """
    Library Book Management System (LBMS)
    Manages book records, borrowing, and returning for a small library.
    By Rho Alphonce E. Jornadal
    """
    
    def __init__(self):
        # Initializing borrowed books as empty
        self.borrowed_books = {}

        # Initializing 20 Books 
        self.books = {
            1:  Book("To Kill a Mockingbird", "Harper Lee", 1960),
            2:  Book("1984", "George Orwell", 1949),
            3:  Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
            4:  Book("Pride and Prejudice", "Jane Austen", 1813),
            5:  Book("The Catcher in the Rye", "J.D. Salinger", 1951),
            6:  Book("The Hobbit", "J.R.R. Tolkien", 1937),
            7:  Book("The Lord of the Rings", "J.R.R. Tolkien", 1954),
            8:  Book("Fahrenheit 451", "Ray Bradbury", 1953),
            9:  Book("Brave New World", "Aldous Huxley", 1932),
            10: Book("Moby-Dick", "Herman Melville", 1851),
            11: Book("War and Peace", "Leo Tolstoy", 1869),
            12: Book("Crime and Punishment", "Fyodor Dostoevsky", 1866),
            13: Book("The Odyssey", "Homer", -700),
            14: Book("The Iliad", "Homer", -750),
            15: Book("Jane Eyre", "Charlotte Brontë", 1847),
            16: Book("Wuthering Heights", "Emily Brontë", 1847),
            17: Book("The Alchemist", "Paulo Coelho", 1988),
            18: Book("The Da Vinci Code", "Dan Brown", 2003),
            19: Book("The Hunger Games", "Suzanne Collins", 2008),
            20: Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
        }

 
    # Displays all books in the library with their ID and year published.

    def display_books(self):
        print()
        for key, book in self.books.items():
            print(f"""\
            [{key}] {book.get_title()} ({book.get_yearPublished()} by {book.get_author})
            """)

        print(f"""\
        [0] Exit
        """)

    # Display all currently borrwed books
    def display_borrowed_books(self):
        print()
        for key, book in self.borrowed_books.items():
            print(f"""\
            [{key}] {book.get_title()} ({book.get_yearPublished()})
            """)

        print(f"""\
            [0] Exit
        """)


    #Populates the borrowed_books dictionary based on book status. Only books marked as 'unavailable' are considered borrowed.
    def update_borrowed_books(self):
        self.borrowed_books.clear()
        count = 1
        for key, book in self.books.items():
            if(book.get_status() == 'unavailable'):
                self.borrowed_books[count] = book
                count += 1
                

            
        
    # Allows the user to borrow a book from the library. Updates the book's status to 'unavailable'.
    def _borrow_book(self):
        self.display_books()

        print(r"""
        ==== Choose Your Book ==== """)
        print()

        while(True): 

            try:
                selection = int(input("Selection [0-20]: "))

                if(selection == 0):
                    break

                if(selection < 0):
                    print("Invalid Selection! Please type a valid umber [0-20]")

                if(selection >= len(self.books)):
                    print("Selection exceeded! Only type positive number [0-20]")
                   
                print(f"You selected: {self.books[selection].display_info()}")
                confirmation = input("Confirm Selection? [Y/N]: ")

                if(confirmation == 'Y' or confirmation == 'y'): 

                    if(self.books[selection].borrow_book()):
                        print(f"{self.books[selection].get_title()} ({self.books[selection].get_yearPublished()}) by {self.books[selection].get_author()} succesffully borrowed!")
        
                    else:
                        print(f"{self.books[selection].get_title()} not available! Status is: {self.books[selection].get_status()}")
    
                elif(confirmation == 'N' or confirmation == 'n'):
                    print("Returning to main menu....")
                    break

                else:
                    print("Invalid Selection! Try again")
                    break

                try:
                    
                    again = input("Do you want to borrow another item? [Y/N]: ")

                    if(again == 'Y' or again == 'y'): 
                        self._borrow_book()
                    else:
                        print("Thanks for borrowing!")
                        break
                    
                except ValueError:
                    print("Invalid Selection! Try again")
                    break
                
            except ValueError:
                print("Invalid Selection! Please try again")


    #Allows the user to return a borrowed book. Updates the book's status to 'available'.
    def _return_book(self):
        while True:
            self.update_borrowed_books()
            if not self.borrowed_books:
                print("No books currently borrowed.")
                break

            self.display_borrowed_books()
            print("\n==== Choose a Book To Return ====\n")

            try:
                selection = int(input(f"Selection [0-{len(self.borrowed_books)}]: "))

                if selection == 0:
                    break

                if selection not in self.borrowed_books:
                    print(f"Invalid Selection! Please choose a valid number [1-{len(self.borrowed_books)}]")
                    continue

                book = self.borrowed_books[selection]
                print(f"You selected: {book.get_title()} ({book.get_yearPublished()}) by {book.get_author()}")
                confirmation = input("Confirm Selection? [Y/N]: ").lower()

                if confirmation == 'y':
                    if book.return_book():
                        print(f"{book.get_title()} ({book.get_yearPublished()}) by {book.get_author()} successfully returned!")
                    else:
                        print(f"Cannot return {book.get_title()}; it was not borrowed.")

                elif confirmation == 'n':
                    print("Returning to main menu...")
                    break

                else:
                    print("Invalid input! Returning to main menu...")
                    break

                again = input("Do you want to return another book? [Y/N]: ").lower()
                if again != 'y':
                    print("Thanks for returning!")
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

    def _add_book(self):
        try:
            book_title = input("Book Title: ")
            book_author = input("Book Author: ")
            publication_year = input ("Publication Year: ")

            confirmation = input(f"You wish to add: {book_title} ({publication_year}) by {book_author}. Confirm? [Y/N]: ")
            if(confirmation == "Y" or confirmation == "y"):
                self.books[len(self.books) + 1] = Book(book_title, book_author, publication_year)
            else:
                print("Goodbye!")

            again = input("Do you want to add another book? [Y/N]: ")
            
            if(again == "Y" or again == "y"):
                self._add_book()
            

        except:
            print("Something went wrong. Please try again")

    def _show_books(self):
        self.display_books()

    # Main menu loop for the Library Book Management System. Handles borrowing, returning, and exiting the program.
    def main(self):
        print(r"""
        ==== LIBRARY MANAGEMENT SYSTEM by Rho Alphonce ====""")
        print(r"""
        ____________________________________________________
        |____________________________________________________|
        | __     __   ____   ___ ||  ____    ____     _  __  |
        ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
        ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
        ||  |##||  | | || | |RAJ|||-|  | |==|+|+||-|-|~||__| |
        ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
        ||_______________________||__________________________|
        | _____________________  ||      __   __  _  __    _ |
        ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
        || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
        ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
        |____________________ /\~()/()~//\ __________________|
        | __   __    _  _     \_  (_ .  _/ _    ___     _____|
        ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
        ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
        ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
        |_________________ _/    \/\/\/    \_ _______________|
        | _____   _   __  |/      \../      \|  __   __   ___|
        ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
        ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
        ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
        |_________ __________\___\____/___/___________ ______|
        |__    _  /    ________     ______           /| _ _ _|
        |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
        | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
        __|  \/\|/   /(____|/ //                    /  /||~|~|~|__
        |___\_/   /________//   ________         /  / ||_|_|_|
        |___ /   (|________/   |\_______\       /  /| |______|
            /                  \|________)     /  / | |
        """)


        print(r"""
        ==== Library Book Management System ==== """)
        print()

        while(True): 
            print(r"""
            [1] Add a Book
            [2] Show Books
            [3] Borrow a Book
            [4] Return a Book
            [0] Exit
            """)

            try:
                selection = int(input("Selection [0-2]: "))

                if(selection < 0):
                    print("Invalid Selection! Please type a valid selection [0-2]")
                    
                if(selection > 2):
                    print("Selection exceeded! Please type a valid selection [0-2]")
                
                
                if(selection == 1):
                    self._add_book()
                
                if(selection == 2):
                    self._show_books()
                
                if(selection == 3):
                    self._borrow_book
                
                if(selection == 4):
                    self._return_book
                    
                if(selection == 0):
                    print("Goodbye! Thanks for coming!")
                    break

 
            except:
                print("Invalid Selection! Please try again")

                



        




    
if __name__ == "__main__":
    lbms = LBMS()
    lbms.main()
    