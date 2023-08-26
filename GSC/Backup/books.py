from typing import List

websites = [
    {
        "name": "google",
        "link": "https://www.google.com",
        "about": "it is a search engine",
        "usage": "information searching",
        "rating": 1
    },
    {
        "name": "youtube",
        "link": "https://www.youtube.com",
        "about": "its a free video sharing website",
        "usage": "watch videos online for free",
        "rating": 2
    },
    {
        "name": "facebook",
        "link": "https://www.facebook.com",
        "about": "social networking site",
        "usage": "communicate with eachother over the internet",
        "rating": 3
    },
    {
        "name": "instagram",
        "link": "https://www.instagram.com",
        "about": "social netowkring site",
        "usage": "communicate with eachother over the internet",
        "rating": 4
    },
    {
        "name": "netflix",
        "link": "https://www.netflix.com",
        "about": "movie streaming website",
        "usage": "watch movies online",
        "rating": 5
    },
    {
        "name": "baidu",
        "link": "https://www.baidu.com",
        "about": "search engine",
        "usage": "information searchung",

        "rating": 6
    },
    {
        "name": "codeforces",
        "link": "https://codeforces.com",
        "about": "competitive coding site",
        "usage": "improve coding skills",
        "rating": 7
    },
    {
        "name": "wikipedia",
        "link": "https://www.wikipedia.org",
        "about": "information library",
        "usage": "learn new information",
        "rating": 8
    },
    {
        "name": "quora",
        "link": "https://www.quora.com",
        "about": "information library",
        "usage": "learn new information",
        "rating": 9
    },
    {
        "name": "pintrest",
        "link": "https://www.pinterest.com",
        "about": "image viewing site",
        "usage": "get images",
        "rating": 10
    }

]

class WebFinder:
    @staticmethod
    def list_web_names():
        return ", ".join([d["name"] for d in websites])

    @staticmethod
    def get_web_link_by_name(input):
        # Search for a specific book's location by name
        for web in websites:
            if web["name"] == input["name"]:
                return {"book_name": web["name"], "link": web["link"]}
        return None

    @staticmethod
    def get_web_by_rating(rating):
        # Search for book's location by genre
        for web in websites:
            if web["rating"] == rating["rating"]:
                return {"book_name": web["rating"], "name": web["name"]}
        return None
    
    @staticmethod
    def get_usage_by_web(webs):
        # Search for book's location by rating
        for web in websites:
            if web["name"] == webs["name"]:
                return {"book_name": web["name"], "usage": web["usage"]}
        return None
    
    @staticmethod
    def get_rating_by_name(name):
        # Search for book's location by genre
        for web in websites:
            if web["name"] == name["name"]:
                return {"book_name": web["name"], "rating": web["rating"]}
        return None
        