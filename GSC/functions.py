gpt_functions = {
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
}