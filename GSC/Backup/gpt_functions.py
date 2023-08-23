gpt_functions = [
    {
        "name": "get_web_link_by_name",
        "description": "Get the link of the websites' name one searched for, for example: what is the link for google? (answer = google.com)",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Website names, eg: google, youtube, etc"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "get_web_by_rating",
        "description": "Gets the name of the website by its rating, for example: what is the most popular website? (answer = google.com), what is the number one rated website? (answer = google.com), what is the number 1 website? (answer = google.com)",
        "parameters": {
            "type": "object",
            "properties": {
                "rating": {
                    "type": "integer",
                    "description": "Website ratings, e.g. 1, 2, 3, 4, 5, or first rated, second rated, third rated."
                }
            },
            "required": ["rating"]
        }
    },
    {
        "name": "get_web_by_usage",
        "description": "Gets the name of the website by its usage, for exmple, I want to watch movies online, what websites should I visit? (answer = netflix.com), I want to watch videos online for free, which websites do you recommend me to visit? (answer = youtube.com)",
        "parameters": {
            "type": "object",
            "properties": {
                "usage": {
                    "type": "string",
                    "description": "Website usage, for example, google = makes information searching easier and more accessable, youtube = makes it easy to watch online videos"
                }
            },
            "required": ["usage"]
        }
    },
    {
        "name": "get_usage_by_web",
        "description": "Gets the usage of the website, for exmple, What is the usage of netflix? (answer = watch movies online), What is the usage of youtube? (answer = watch videos online for free), What is the function of google? (answer = to help people in searching information)",
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
        "name": "get_rating_by_name",
        "description": "find out the rating of a book said by the user, for example: What is the popularity rating of google? (answer = number 1), What is the popularity rating of youtube? (answer = second most popular)",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the website, for example, google, youtube, netflix"
                }
            },
            "required": ["name"]
        }
    }
]