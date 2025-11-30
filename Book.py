class Book:
    def __init__(self, title, author, year_published, status='available'):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.status = status

    def get_summary(self):
        return f"'{self.title}' by {self.author}, published in {self.year_published}. Status: {self.status}."

    def is_available(self):
        return self.status == 'available'
    
    def borrow(self):
        if self.is_available():
            self.status = 'borrowed'
            return True
        return False