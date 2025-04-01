book_store = {
    "The Great Gatsby": 5,
    "To Kill a Mockingbird": 8,
    "1984": 4,
    "Dune": 2
}

def display_books():
    print("\nCurrent Books in Store:")
    for book, stock in book_store.items():
        print(f"{book}: {stock} copies")


def update_stock(title, quantity):
    if title in book_store:
        book_store[title] += quantity
        print(f"Updated stock of '{title}' to {book_store[title]}.")
    else:
        print(f"'{title}' not found in store.")


def add_book(title, quantity):
    if title in book_store:
        print(f"'{title}' already exists. Updating stock instead.")
        update_stock(title, quantity)
    else:
        book_store[title] = quantity
        print(f"Added '{title}' with {quantity} copies.")

def delete_book(title):
    if title in book_store:
        del book_store[title]
        print(f"Deleted '{title}' from store.")
    else:
        print(f"'{title}' not found in store.")

# Example Usage
# display_books()
# add_book("Pride and Prejudice", 6)
# update_stock("1984", 3)
# delete_book("Dune")
# display_books()
