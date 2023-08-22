websiteLists = """
    {
        "name":Google Search
        "link":google.com
        "company":Computers Electronics and Technology > Search Engines,United States 
    1,YouTube,youtube.com,Arts & Entertainment > Streaming & Online TV,United States
    2,Facebook,facebook.com,Computers Electronics and Technology > Social Media Networks,United States
    3,Twitter,twitter.com,Computers Electronics and Technology > Social Media Networks,United States
    4,Instagram,instagram.com,Computers Electronics and Technology > Social Media Networks,United States
    5,Baidu,baidu.com,Computers Electronics and Technology > Search Engines,China
    6,Wikipedia,wikipedia.org,Reference Materials > Dictionaries and Encyclopedias,United States
    7,Yandex,yandex.ru,Computers Electronics and Technology > Search Engines,Russia
    8,Yahoo,yahoo.com,News & Media Publishers,United States
    9,xVideos,xvideos.com,Adult,Czech Republic
    10,WhatsApp,whatsapp.com,Computers Electronics and Technology > Social Media Networks,United States
    11,Pornhub,pornhub.com,Adult,Canada
    12,Xnxx,xnxx.com,Adult,France
    13,Amazon,amazon.com,eCommerce & Shopping > Marketplace,United States
    14,Yahoo JP,yahoo.co.jp,News & Media Publishers,Japan
    15,Live,live.com,Computers Electronics and Technology > Email,United States
    16,Netflix,netflix.com,Arts & Entertainment > Streaming & Online TV,United States
    17,Reddit,reddit.com,Computers Electronics and Technology > Social Media Networks,United States
    18,TikTok,tiktok.com,Computers Electronics and Technology > Social Media Networks,China
    19,Docomo,docomo.ne.jp,Computers Electronics and Technology > Telecommunications,Japan
    20,LinkedIn,linkedin.com,Computers Electronics and Technology > Social Media Networks,United States
    21,Office,office.com,Computers Electronics and Technology > Programming and Developer Software,United States
    22,Samsung,samsung.com,Computers Electronics and Technology > Consumer Electronics,South Korea
    23,Yandex Turbo Pages,turbopages.org,News & Media Publishers,Russia
    24,VK,vk.com,Computers Electronics and Technology > Social Media Networks,Russia
    25,xHamster,xhamster.com,Adult,Cyprus
    26,Weather,weather.com,Science and Education > Weather,United States
    27,Twitch,twitch.tv,Games > Video Games Consoles and Accessories,United States
    28,Mail.Ru,mail.ru,Computers Electronics and Technology > Email,Russia
    29,Naver,naver.com,News & Media Publishers,South Korea
    30,Discord,discord.com,Computers Electronics and Technology > Social Media Networks,United States
    31,Bing,bing.com,Computers Electronics and Technology > Search Engines,United States
    32,Roblox,roblox.com,Games > Video Games Consoles and Accessories,United States
    33,Bilibili,bilibili.com,Arts & Entertainment > Animation and Comics,China
    34,Microsoft Online,microsoftonline.com,Computers Electronics and Technology > Programming and Developer Software,United States
    35,Pinterest,pinterest.com,Computers Electronics and Technology > Social Media Networks,United States
    36,Zoom,zoom.us,Computers Electronics and Technology > Other Computers Electronics and Technology,United States
    37,QQ,qq.com,News & Media Publishers,China
    38,DuckDuckGo,duckduckgo.com,Computers Electronics and Technology > Search Engines,United States
    39,Microsoft,microsoft.com,Computers Electronics and Technology > Programming and Developer Software,United States
    40,Fandom,fandom.com,Arts & Entertainment > Other Arts and Entertainment,United States
    41,Quora,quora.com,Reference Materials > Dictionaries and Encyclopedias,United States
    42,Yahoo! News,news.yahoo.co.jp,News & Media Publishers,United States
    43,RealSRV,realsrv.com,Adult,United States
    44,eBay,ebay.com,eCommerce & Shopping > Marketplace,United States
    45,MSN,msn.com,News & Media Publishers,United States
    46,Globo,globo.com,News & Media Publishers,Brazil
    47,Stripchat,stripchat.com,Adult,Cyprus
    48,Booking,booking.com,Travel and Tourism > Accommodation and Hotels,Netherlands
    49,OK.ru,ok.ru,Computers Electronics and Technology > Social Media Networks,Russia
"""

class BookFinder:
    @staticmethod
    def get_book_location_by_name(input):
        # Search for a specific book's location by name
        for book in library_books:
            if book["name"] == input["name"]:
                return {"book_name": book["name"], "location": book["location"]}
        return None