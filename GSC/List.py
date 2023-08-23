websites = [
    {
        "ranking": "1st",
        "name": "Google Search",
        "link": "google.com",
        "about": "it is a search engine",
        "usage": "organize the world's information and make it universally accessible and useful"
    },
    {
        "ranking": "2nd",
        "name": "Youtube",
        "link": "youtube.com",
        "about": "its a free video sharing website",
        "usage": "makes it easy to watch online videos"
    }
]
 
gpt_functions = [
    {
        "name": "find_website_name_by_ranking",
        "description": "Get the website name according to its ranking . e.g. what is the most popular website, what is the number 1 most popular website, what is the number 1 webstie",
        "parameters": {
            "type": "object",
            "properties": {
                "ranking": {
                    "type": "string",
                    "description": "webstie rankings, eg: google = 1st ranked, youtube = 2nd ranked"
                }
            },
            "required": ["ranking"]
        }
    }
]

class Finder:
    @staticmethod
    def find_website_name_by_ranking(input):
        # Search for a specific book's location by name
        for site in websites:
            if site["ranking"] == input["ranking"]:
                return {"website_ranking": site["ranking"], "name": site["name"]}
        return None