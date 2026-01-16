from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"{book.title} by {book.author} ({book.publication_year})")
