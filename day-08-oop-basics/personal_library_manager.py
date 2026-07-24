class BookNotFoundError(Exception):
    pass

class InvalidRatingError(Exception):
    pass


def add_book(title,author,rating):
    if rating < 1 or rating > 5:
        raise InvalidRatingError("Rating must be between 1 and 5")
    else:
        with open("library.txt","a") as file:
            file.write(f"{title}|{author}|{rating}\n")


add_book("Atomic Habits", "James Clear", 5)
add_book("1984", "George Orwell", 1)
    


def view_library():
    try:
        with open("library.txt","r") as file:
            for i,line in enumerate(file,1):
                title,author,rating = line.strip().split("|")
                print(f"{i}. {title.strip()} by {author.strip()} - {rating.strip()}\n")
    
    except FileNotFoundError:
        print("No file found")

view_library()




def find_book(title):
    with open("library.txt","r") as file:
        for line in file:
            book_title,author,rating = line.strip().split("|")
            if book_title == title:
                return f"Title: {book_title}, author: {author}, rating: {rating}"
    
    raise FileNotFoundError(f"'{title}' not found in library")


def average_rating():
    total = 0
    count = 0
    with open("library.txt","r") as file:
        for line in file:
            title,author,rating = line.strip().split("|")
            total = total + int(rating)
            count = count + 1
    return round(total/count,2)

def remove_book(title):
    with open("library.txt","r") as file:
        books = file.readlines()

    updated_books = []
    found = False

    for line in books:
        book_title,author,rating = line.strip().split("|")
        if book_title == title:
            found = True
        else:
            updated_books.append(line)
    
    if not found:
        raise BookNotFoundError(f"{title} not found in library")
    
    with open("library.txt","w") as file:
        file.writelines(updated_books)



view_library()


