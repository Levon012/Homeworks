"""Create a dictionary of book titles and their authors. Write a function to search for a book
by its title and return the author's name."""



def book_titles(title):
    for k, v in books.items():
        if k in title:
            return v
books = {'Anasnaferma': 'George Orwell', 'Odaparuk trcnoxy': 'Xaled Hoseyni', 'Astxern en mexavor': 'John Grin'}
print(book_titles('Anasnaferma'))



