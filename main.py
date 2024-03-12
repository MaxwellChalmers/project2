import os
import requests
import click 


import click

API_KEY = os.environ["GIF_KEY"] 


@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
def trending():
    print("trending subcommand called!")


@gif.command()
def search():
    print("search subcommand called!")


def buildSearchCall(KEY,
                    query = "cats", 
                    limit = 5,
                    offset = 0,
                    rating = "g",
                    lang = 'en', 
                    random_id = "bob", 
                    bundle = "messaging_non_clips"):
    print("foo")
      

def buildTrendingCall(KEY, 
                      limit = 5, 
                      offset = 0, 
                      rating = "g", 
                      random_id = "rob"
                      bundle = "messaging_non_clips"):
    print("woo")
      

if __name__ == "__main__":
	apiCall = "https://api.giphy.com/v1/gifs/trending?api_key=" + API_KEY + "&limit=1&offset=0&rating=g" 

	resp = requests.get(apiCall)

	gify = resp.json()

	
	print(gify.keys())
	
	data = gify.get("data").pop()
	for k in data.keys():
		print (k + " = " + str(data.get(k)) + "\n")


	gif()