books = {"George R. R. Martin": ["A Game of Thrones", "The Winds of Winter", "Fire & Blood"],
         "John R. R. Tolkien": ["The Lord of the Rings", "The Hobbit", "The Fellowship of the Ring"]}

try:
    input = str(input("Enter Author: "))
    output = ", ".join(books[input])
    print(f"The books are: {output}")
except: 
    print("Doesn't exist")