import os
from Book import Book

class LBMS:
    
    def __init__(self):
        self.borrowed_books = {}
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


    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def display_books(self):
        print()
        for key, book in self.books.items():
            print(f"""\
            [{key}] {book.get_title()} ({book.get_yearPublished()})
            """)

        print(f"""\
        [0] Exit
        """)

    def display_borrowed_books(self):
        print()
        for key, book in self.borrowed_books.items():
            print(f"""\
            [{key}] {book.get_title()} ({book.get_yearPublished()})
            """)

        print(f"""\
            [0] Exit
        """)


    def get_borrowed_books(self):
        count = 1
        for key, book in self.books.items():
            if(book.get_status() == 'unavailable'):
                self.borrowed_books[count] = book
                count += 1
                

            
        
    def borrow_book(self):
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
                        self.borrow_book()
                    else:
                        print("Thanks for borrowing!")
                        break
                    
                except ValueError:
                    print("Invalid Selection! Try again")
                    break

                    
                
                
            except ValueError:
                print("Invalid Selection! Please try again")

    
    def return_book(self): 
        self.get_borrowed_books()
        self.display_borrowed_books()

        print(r"""
        ==== Choose The Book To Return ==== """)
        print()

        while(True):
            try:
                selection = int(input(f"Selection [0-{len(self.borrowed_books)}]: "))
                
                if(selection == 0):
                    break

                if(selection < 0):
                    print(f"Invalid Selection! Please type a valid umber [0-{len(self.borrowed_books)}]")

                if(selection >= len(self.books)):
                    print(f"Selection exceeded! Only type positive number [0-{len(self.borrowed_books)}]")
                
                print(f"You selected: {self.borrowed_books[selection].get_title()} ({self.borrowed_books[selection].get_yearPublished()}) by {self.borrowed_books[selection].get_author()}")
                confirmation = input("Confirm Selection? [Y/N]: ")

                if(confirmation == 'Y' or confirmation == 'y'): 

                    if(self.borrowed_books[selection].return_book()):
                        print(f"{self.borrowed_books[selection].get_title()} ({self.borrowed_books[selection].get_yearPublished()}) by {self.borrowed_books[selection].get_author()} succesffully returned!")
        
                    else:
                        print(f"Cannot return {self.borrowed_books[selection].get_title()} since book was not borrowed!")
                
                elif(confirmation == 'N' or confirmation == 'n'):
                    print("Returning to main menu....")
                    break

                else:
                    print("Invalid Selection! Try again")
                    break

                again = input("Do you want to return another item? [Y/N]: ")

                if(again == 'Y' or again == 'y'): 
                    self.return_book()
                else:
                    print("Thanks for returning!")
                    break

            except ValueError:
                print("Invalid Selection! Please try again")

                

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
            [1] Borrow a Book
            [2] Return a Book
            [0] Exit
            """)

            try:
                selection = int(input("Selection [0-2]: "))

                if(selection < 0):
                    print("Invalid Selection! Please type a valid selection [0-2]")
                    
                if(selection > 2):
                    print("Selection exceeded! Please type a valid selection [0-2]")
                
                
                if(selection == 1):
                    self.borrow_book()
                
                if(selection == 2):
                    self.return_book()

                if(selection == 0):
                    print("Goodbye! Thanks for coming!")
                    break

 
            except:
                print("Invalid Selection! Please try again")

                



        




    
if __name__ == "__main__":
    lbms = LBMS()
    lbms.main()
    