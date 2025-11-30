from Book import Book

class LBMS:
    
    def __init__(self):
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

                
    def borrow_book(self):
        print("Hello")
    
    def return_book(self): 
        print("Hello")

    def display_books(self):
        for key, book in self.books.items():
            print(f"[{key}] {book.get_title()} ({book.get_yearPublished()})")

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
        ==== Choose Your Book ==== """)
        print()

        while(True): 
            self.display_books()

            try:
                selection = int(input("Selection [1-20]: "))

                if(selection < 0):
                    print("Invalid Selection. Please type a positive number [1-10]")
                    

                    

                
            except:
                print("Invalid Selection")
            

    
if __name__ == "__main__":
    lbms = LBMS()
    lbms.main()
    