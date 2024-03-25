import os
import string

from giphyAPI import GiphyAPI

API_KEY = os.environ["GIF_KEY"]

if __name__ == "__main__":

    # Get a list of all uppercase letters
    uppercase_letters = list(string.ascii_uppercase)

    # Get a list of all lowercase letters
    lowercase_letters = list(string.ascii_lowercase)
    single_digit_numbers = [str(i) for i in range(10)]

    allTheChars = uppercase_letters + lowercase_letters + single_digit_numbers
    api = GiphyAPI(API_KEY)

    # for c in lowercase_letters:
    # api.storeJSON(api.callSearch(query="letter V", limit = 50), "letters/" + "V" )

    removal = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
    ]
    keep = [1, 2, 7, 13, 18]
    for k in keep:
        removal = [x for x in removal if x != k]
    # api.pruneJSON(removal , "Z")

    listOletters = api.openJSON("letters/A")
    for i in range(len(listOletters)):
        bitlyUrl = listOletters[i]["bitly_gif_url"]
        title = listOletters[i]["title"]
        url = listOletters[i]["images"]["original"]["url"]
        number = str(i) + ") "
        print(number + "![" "](" + url + ")")

    # api.pruneJSON(removal , "E")
    # api.pruneJSON([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33, 34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], "F")
