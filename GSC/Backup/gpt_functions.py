gpt_functions = [
    {
        "name": "find_book_location_by_name",
        "description": "Get the book location given the book name. e.g. where can i find the book, where is the location, i am looking for",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Book names, e.g. Frankenstein, The Chronicles of Narnia"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "list_book_by_rating",
        "description": "lists the book names of the same rating or similar rating. e.g. can i get the names of the books with the rating of (x), what are the good rating books you have, recommend me the highest rating book you have.",
        "parameters": {
            "type": "object",
            "properties": {
                "rating": {
                    "type": "string",
                    "description": "Book ratings, e.g. 1, 2, 3, 4, 5."
                }
            },
            "required": ["rating"]
        }
    },
    {
        "name": "list_book_by_genre",
        "description": "lists the book names of the same genre. e.g. do you have books with the ganre_____, what are the books with the genre____, recommend books with the genre____",
        "parameters": {
            "type": "object",
            "properties": {
                "genre": {
                    "type": "string",
                    "description": "Book genre, e.g. Dystopian Fiction, Classic Fiction, Epic Poetry"
                }
            },
            "required": ["genre"]
        }
    },
    {
        "name": "find_rating_by_name",
        "description": "find out the rating of a book said by the user, for example: What is the rating of Harry Potter and the Sorcerer's Stone? (answer = 4.8), What is the rating of To Kill a Mockingbird? (answer = 5)",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Book name, e.g. Dystopian Fiction, Classic Fiction, Epic Poetry"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "find_genre_by_name",
        "description": "find out the genre of a book said by the user, for example: What is the genre of The Name of the Rose (answer = Mystery/Historical Fiction), What is the genre of The Divine Comedy? (answer = Epic Poetry)",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Book name, e.g. Dystopian Fiction, Classic Fiction, Epic Poetry"
                }
            },
            "required": ["name"]
        }
    }
]
