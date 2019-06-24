class User(object):
    def __init__(self, name, email):
        self.name = name 
        self.email = email 
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email for {} has been updated to {}".format(self.name, self.email))

    def __repr__(self):
        book_count = len(self.books)
        return " User {name}, email: {email}, books read :{book_count}".format(
            name=self.name,
            email=self.email,
            book_count=book_count
        )

    def __eq__(self, other_user):
        if self.name == other_user.name and \
            self.email == other_user.email:
            return True 
        else:
            return False

    def read_book(self, book, rating=None):
        self.books.setdefault(book, rating)

    def get_average_rating(self):
        tot = 0
        cnt = 0
        
        for rating in self.books.values():
            if rating is not None:
                tot += rating
                cnt += 1
        if cnt > 0:
            return tot / cnt
        else:
            return 0

class Book():
    def __init__(self, title, isbn):
        self.title = title 
        self.isbn = isbn 
        self.ratings = [] 

    def get_title(self):
        return self.title  

    def get_isbn(self):
        return self.isbn  

    def get_ratings_count(self):
        return len(self.ratings)

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN for {} has been updated to {}".format(self.title, new_isbn))

    def add_rating(self, rating):
        if rating is None:
            return
        elif self.valid_rating(rating):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def valid_rating(self, rating):
        if type(rating) == int:
            if rating > -1 and rating < 5:
                return True
        
        return False

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating

        return total / len(self.ratings)

    def __eq__(self, other_book):
        if self.title == other_book.title and \
            self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        stringrep = "{} :<ISBN<{}>".format(self.title, self.isbn)
        return stringrep

class Fiction(Book):
    def __init__(self,title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author
    
    def __repr__(self):
        title = super().get_title() 
        author = self.author 
        stringrep = "{title} by {author}".format(title=title, author=author)
        return stringrep

class Non_Fiction(Book):
    def __init__(self,title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject 

    def get_level(self):
        return self.level

    def __repr__(self):
        title = super().get_title() 
        level = self.level
        subject = self.subject
        stringrep = "{title}, a {level} manual on {subject}".format(title=title,level=level,subject=subject)
        return stringrep

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self,title,isbn):
        book = Book(title, isbn)
        return book 

    def create_novel(self,title,author,isbn):
        novel = Fiction(title, author, isbn)
        return novel

    def create_non_fiction(self,title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self,book,email,rating=None):
        found = False 

        user = self.users.get(email, None)
        if user is not None and user.email == email:
            user.read_book(book,rating)
            book.add_rating(rating)

            user_reads = self.books.get(book, 0) + 1
            self.books.setdefault(book, user_reads)

            found = True 
     
        if not found:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users.setdefault(email,user)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
                
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read = None 
        for book in self.books.keys():
            if most_read is None:
                most_read = book
            else:
                if book.get_ratings_count() > most_read.get_ratings_count():
                    most_read = book
        return most_read
        
    def highest_rated_book(self):
        highest = None 
        for book in self.books.keys():
            if highest is None:
                highest = book 
            else:
                if book.get_average_rating() > highest.get_average_rating():
                    highest = book 
        return highest

    def most_positive_user(self):       
        positivist = None
        for user in self.users.values():
            if positivist is None:
                positivist = user 
            else:
                if user.get_average_rating() > positivist.get_average_rating():
                    positivist = user
        return positivist
