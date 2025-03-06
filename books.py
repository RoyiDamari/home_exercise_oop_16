from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database (SQLite)
engine = create_engine("sqlite:///books.db", echo=True)

# Base class
Base = declarative_base()


# Define a User model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    price = Column(Integer, nullable=False)


# Create table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# Insert multiple users
session.add_all([
    Book(title="Harry Potter and the Sorcerer's Stone", price=89.90),
    Book(title="The Little Prince", price=45.50),
    Book(title="1984", price=79.90),
Book(title="Les Misérables", price=99.00),
Book(title="Crime and Punishment", price=69.90)
])
session.commit()

# Select all books
books = session.query(Book).all()
print("All Books List:")
for book in books:
    print(book.title, book.price)

# Select only books that are more expensive than 70
print("-" * 50)
expensive_books = session.query(Book).filter(Book.price > 70).all()
print("Expensive Books List:")
for book in expensive_books:
    print(book.title, book.price)

# Update book price
session.query(Book).filter(Book.title == "1984").update({"price": "89.50"})
session.commit()

# Delete books which cost 99
session.query(Book).filter(Book.price == 99).delete()
session.commit()
