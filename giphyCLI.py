from giphyAPI import GiphyAPI


class GiphyCLI:

    def __init__(self, KEY):
        self.API_KEY = KEY

    #limit = 1 == lucky = True 

    def trending(self, limit=5, markdown=False):
        if(limit > 50): 
            print("The maximum number of results is 50, setting limit to 50")
            limit = 50 
        api = GiphyAPI(self.API_KEY)
        gifs = api.callTrending(limit=limit)
        for i in range(limit):
            gif = gifs[i]
            bitlyUrl = gif["bitly_gif_url"]
            title = gif["title"]
            url = gif["images"]["original"]["url"]
            if(markdown):
                print(str(i+1) + ") ![" + title + "](" + url + ")") 
            else: 
                print(str(i + 1) + ") " + title + " (" + bitlyUrl +")")
        
    def search(self, query="cats", limit=5, markdown=False):
        if(len(query) > 50):
            print("There is a char limit of 50 on search terms")
            print("I will shorten your search to the limit")
            print("trying again with a shorter query recomended!")
            query = query[:50]
        if(limit > 50): 
            print("The maximum number of results is 50, setting limit to 50")
            limit = 50 

        api = GiphyAPI(self.API_KEY)
        gifs = api.callSearch(query=query, limit=limit)

        for i in range(limit):
            gif = gifs[i]
            bitlyUrl = gif["bitly_gif_url"]
            title = gif["title"]
            url = gif["images"]["original"]["url"]
            if(markdown):
                print(str(i+1) + ") ![" + title + "](" + url + ")") 
            else: 
                print(str(i + 1) + ") " + title + " (" + bitlyUrl +")")
