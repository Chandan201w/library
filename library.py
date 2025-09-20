import random

class Book:
    def __init__(self, title, author, subject):
        self.title = title
        self.author = author
        self.subject = subject
        self.is_borrowed = False
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Rating must be between 1 and 5.")

    def get_avg_rating(self):
        if self.ratings:
            return round(sum(self.ratings) / len(self.ratings), 2)
        return "No ratings yet"


class Library:
    def __init__(self):
        self.books = []
        self.create_books()

    def create_books(self):
        subjects = {
            "Computer Science": ["Python Programming", "Data Structures", "AI Basics", "Machine Learning", "Database Systems"],
            "Finance": ["Banking Principles", "Financial Markets", "Corporate Finance", "Investment Basics", "Risk Management"],
            "Chemistry": ["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry", "Biochemistry"],
            "Literature": ["Shakespeare Plays", "Modern Poetry", "Classic Novels", "Drama Anthology", "Short Stories"],
            "History": ["World History", "Ancient Civilizations", "Medieval Era", "Modern History", "Indian Freedom Struggle"]
        }

        authors = ["Author A", "Author B", "Author C", "Author D", "Author E"]

        # Create 300 books (60 per subject, random author assigned)
        for subject, titles in subjects.items():
            for i in range(60):  # 60 books per subject
                title = f"{titles[i % len(titles)]} Vol-{i+1}"
                author = random.choice(authors)
                self.books.append(Book(title, author, subject))

    def display_books(self):
        print("\n===== Available Books =====")
        for idx, book in enumerate(self.books, start=1):
            if not book.is_borrowed:
                print(f"{idx}. {book.title} | {book.author} | {book.subject} | Rating: {book.get_avg_rating()}")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"\nYou borrowed '{book.title}'.")
                    return
                else:
                    print("\nSorry, this book is already borrowed.")
                    return
        print("\nBook not found.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"\nYou returned '{book.title}'.")
                    return
        print("\nBook not found or not borrowed.")

    def rate_book(self, book_title, rating):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                book.add_rating(rating)
                print(f"\nYou rated '{book.title}' with {rating} stars.")
                return
        print("\nBook not found.")


def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Rate a Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book = input("Enter the book title you want to borrow: ")
            library.borrow_book(book)
        elif choice == "3":
            book = input("Enter the book title you want to return: ")
            library.return_book(book)
        elif choice == "4":
            book = input("Enter the book title you want to rate: ")
            try:
                rating = int(input("Enter rating (1-5): "))
                library.rate_book(book, rating)
            except ValueError:
                print("Invalid rating. Must be a number 1–5.")
        elif choice == "5":
            print("\nThank you for using the Library System. Goodbye!")
            break
        else:
            print("\nInvalid choice, try again.")


if __name__ == "__main__":
    main()
