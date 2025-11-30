class Book:
    def __init__(self, title, author, year_published, status='available'):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.status = status

    def display_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year_published}. Status: {self.status}."

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    def get_yearPublished(self):
        return self.year_published

    def get_status(self):
        return self.status

    def is_available(self):
        return self.status == 'available'

    def borrow_boo(self):
        if self.is_available():
            self.status = 'unavaible'
            return True
        return False
    
    def return_book(self):
        if not self.is_available():
            self.status = 'available'
            return True
        return False
        