import json

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
        return resp.json()["data"]

    def callSearch(self, query="cats", limit=5):
        callParams = self.buildSearchCall(self.API_KEY, query, limit)
        resp = requests.get(self.searchUrl, params=callParams)
        return resp.json()["data"]

    def cachedJSON(self):
        return self.openJSON("A")

    def storeJSON(self, gif_list, filename):
        with open(filename + ".json", "w") as json_file:
            json.dump(gif_list, json_file)

    def openJSON(self, filename):
        with open(filename + ".json", "r") as json_file:
            data = json.load(json_file)
            return data

    def pruneJSON(self, toBeRemoved, filename):
        letterList = self.openJSON("letters/" + filename)
        toBeRemoved.sort(reverse=True)
        for i in toBeRemoved:
            if 0 <= i < len(letterList):
                del letterList[i]
            else:
                print(f"Ignoring index {i}: Index out of range")

        self.storeJSON(letterList, "letters/" + filename)
