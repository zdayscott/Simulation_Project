import random

# Test input to place hold for the front end. [(string, int), (Name/Event, rank of hate 1-10)]
input1 = [("Ivanca", 1)]
input2 = [("Democrats", 9), ("Avocado toast", 8)]

fillins = ["I really hate replaceme", "Hillary just wants replaceme, that should tell you enough", "replaceme is the greatest"]

class Responces:
    def __init__(self, response, person, place, thing, event, dislike):
        self.resp = response
        self.person = person
        self.place = place
        self.thing = thing
        self.event = event

        self.dislikes = dislike

def TweetCreator(inp):
    tweet = fillins[random.randrange(0, fillins.__len__())]
    tweet = tweet.replace("replaceme", inp[random.randrange(0, inp.__len__())][0])
    print(tweet)
    return tweet


if(__name__ == "__main__"):
    TweetCreator(input1)
    TweetCreator(input2)

