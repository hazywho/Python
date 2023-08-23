from typing import List

library_books = [
    {
        "name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic Fiction",
        "location": "Shelf A, Section 1",
        "rating": "3.9"
    }, 
    {
        "name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic Fiction",
        "location": "Shelf B, Section 2",
        "rating": "5"
    },
    {
        "name": "1984",
        "author": "George Orwell",
        "genre": "Dystopian Fiction",
        "location": "Shelf C, Section 3",
        "rating": "4.2"
    },
    {
        "name": "The Lord of the Rings Trilogy",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "location": "Shelf D, Section 4",
        "rating": "4.5"
    },
    {
        "name": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "location": "Shelf E, Section 5",
        "rating": "4.3"
    },
    {
        "name": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "location": "Shelf F, Section 6",
        "rating": "4.8"
    },
    {
        "name": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-Age Fiction",
        "location": "Shelf G, Section 7",
        "rating": "3.8"
    },
    {
        "name": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "location": "Shelf H, Section 8",
        "rating": "4.3"
    },
    {
        "name": "Jane Eyre",
        "author": "Charlotte Brontë",
        "genre": "Classic Fiction",
        "location": "Shelf I, Section 9",
        "rating": "4.1"
    },
    {
        "name": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "Mystery/Thriller",
        "location": "Shelf J, Section 10",
        "rating": "4"
    },
    {
        "name": "Brave New World",
        "author": "Aldous Huxley",
        "genre": "Dystopian Fiction",
        "location": "Shelf K, Section 11",
        "rating": "4.3"
    },
    {
        "name": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Inspirational Fiction",
        "location": "Shelf L, Section 12",
        "rating": "3.5"
    },
    {
        "name": "The Hunger Games Trilogy",
        "author": "Suzanne Collins",
        "genre": "Dystopian Fiction",
        "location": "Shelf M, Section 13",
        "rating": "5"
    },
    {
        "name": "The Kite Runner",
        "author": "Khaled Hosseini",
        "genre": "Historical Fiction",
        "location": "Shelf N, Section 14",
        "rating": "4.3"
    },

    {
        "name": "The Chronicles of Narnia",
        "author": "C.S. Lewis",
        "genre": "Fantasy",
        "location": "Shelf O, Section 15",
        "rating": "3.9"
    },
    {
        "name": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "genre": "Gothic Fiction",
        "location": "Shelf P, Section 16",
        "rating": "4"
    },
    {
        "name": "The Shining",
        "author": "Stephen King",
        "genre": "Horror",
        "location": "Shelf Q, Section 17",
        "rating": "3.8"
        
    },
    {
        "name": "The Adventures of Huckleberry Finn",
        "author": "Mark Twain",
        "genre": "Classic Fiction",
        "location": "Shelf R, Section 18",
        "rating": "4.3"
    },
    {
        "name": "The Handmaid's Tale",
        "author": "Margaret Atwood",
        "genre": "Dystopian Fiction",
        "location": "Shelf S, Section 19",
        "rating": "3"
    },
    {
        "name": "Wuthering Heights",
        "author": "Emily Brontë",
        "genre": "Classic Fiction",
        "location": "Shelf T, Section 20",
        "rating": "3.1"
    },
    {
        "name": "The Girl with the Dragon Tattoo",
        "author": "Stieg Larsson",
        "genre": "Mystery/Thriller",
        "location": "Shelf U, Section 21",
        "rating": "4.2"
    },
    {
        "name": "Moby-Dick",
        "author": "Herman Melville",
        "genre": "Adventure Fiction",
        "location": "Shelf V, Section 22",
        "rating": "3.5"
    },
    {
        "name": "The Adventures of Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "genre": "Mystery",
        "location": "Shelf W, Section 23",
        "rating": "4.4"
    },
    {
        "name": "Frankenstein",
        "author": "Mary Shelley",
        "genre": "Gothic Fiction",
        "location": "Shelf X, Section 24",
        "rating": "4"
    },
    {
        "name": "The Road",
        "author": "Cormac McCarthy",
        "genre": "Post-Apocalyptic Fiction",
        "location": "Shelf Y, Section 25",
        "rating": "3.7"
    },
    {
        "name": "The Grapes of Wrath",
        "author": "John Steinbeck",
        "genre": "Historical Fiction",
        "location": "Shelf Z, Section 26",
        "rating": "4"
    },
    {
        "name": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "genre": "Magical Realism",
        "location": "Shelf AA, Section 27",
        "rating": "4.1"
    },
    {
        "name": "The Odyssey",
        "author": "Homer",
        "genre": "Epic Poetry",
        "location": "Shelf BB, Section 28",
        "rating": "3.5"
    },
    {
        "name": "The Divine Comedy",
        "author": "Dante Alighieri",
        "genre": "Epic Poetry",
        "location": "Shelf CC, Section 29",
        "rating": "4"
    },
    {
        "name": "The Name of the Rose",
        "author": "Umberto Eco",
        "genre": "Mystery/Historical Fiction",
        "location": "Shelf DD, Section 30",
        "rating": "3.9"
    }]

class BookFinder:
    @staticmethod
    def list_book_names():
        return ", ".join([d["name"] for d in library_books])

    @staticmethod
    def get_book_location_by_name(input):
        # Search for a specific book's location by name
        for book in library_books:
            if book["name"] == input["name"]:
                return {"book_name": book["name"], "location": book["location"]}
        return None

    @staticmethod
    def list_book_by_genre(genre_list):
        # Search for book's location by genre
        for book in library_books:
            if book["genre"] == genre_list["genre"]:
                return {"book_name": book["genre"], "name": book["name"]}
        return None

    @staticmethod
    def list_book_by_rating(rating):
        # Search for book's location by rating
        for book in library_books:
            if book["rating"] == rating["rating"]:
                return {"book_name": book["rating"], "name": book["name"]}
        return None
    
    @staticmethod
    def find_rating_by_name(name):
        # Search for book's location by rating
        for book in library_books:
            if book["name"] == name["name"]:
                return {"book_name": book["name"], "rating": book["rating"]}
        return None
    
    @staticmethod
    def find_genre_by_name(name):
        # Search for book's location by rating
        for book in library_books:
            if book["name"] == name["name"]:
                return {"book_name": book["name"], "rating": book["genre"]}
        return None