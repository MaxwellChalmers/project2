import requests


class GiphyAPI:

    def __init__(self, KEY):
        self.API_KEY = KEY

    searchUrl = "https://api.giphy.com/v1/gifs/search?"
    trendingUrl = "https://api.giphy.com/v1/gifs/trending?"

    @staticmethod
    def buildSearchCall(
        KEY,
        query="cats",
        limit=5,
        offset=0,
        rating="g",
        lang="en",
        random_id="bob",
        bundle="messaging_non_clips",
    ):
        searchParams = {
            "api_key": KEY,
            "q": query,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "lang": lang,
            "random_id": random_id,
            "bundle": bundle,
        }
        return searchParams

    @staticmethod
    def buildTrendingCall(
        KEY,
        limit=5,
        offset=0,
        rating="g",
        random_id="rob",
        bundle="messaging_non_clips",
    ):
        trendingParams = {
            "api_key": KEY,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "random_id": random_id,
            "bundle": bundle,
        }
        return trendingParams

    def callTrending(self, limit=5):
        callParams = self.buildTrendingCall(self.API_KEY, limit)
        resp = requests.get(self.trendingUrl, params=callParams)
        print(resp.json().keys())
        return resp.json()["data"]

    def callSearch(self, query="cats", limit=5):
        callParams = self.buildSearchCall(self.API_KEY, query, limit)
        resp = requests.get(self.searchUrl, params=callParams)
        print(resp.json().keys())
        return resp.json()["data"]
