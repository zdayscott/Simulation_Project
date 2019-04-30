import random
import csvParser
import MarkovChain

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

def MarkovTweetGen(MC, length = 20):
    word1 = random.choice(list(MC.keys()))
    retSen = word1.capitalize()

    for it in range(length - 1):
        word2 = random.choice(MC[word1])
        if(word2 == "@b@"):
            break
        word1 = word2
        retSen += " " + word1
    
    retSen += '.'
    print(retSen)

def MarkovTrumpReactiveTweetGen(inp):
    return MarkovReactiveTweetGen(MarkovChain.MarkovChain(csvParser.ImportTrumpData()), inp)

def MarkovReactiveTweetGen(MC, inp, length = 20):
    word1 = ""
    retSen = ""
    if inp in MC:
        word1 = inp
        retSen = word1.capitalize()
    else:
        if(inp[:-1].endswith('s')):
            word1 = "are"
        else:
            word1 = "is"
        retSen = inp + ' ' + word1
    
    for it in range(length - 1):
        word2 = random.choice(MC[word1])
        if(word2 == "@b@"):
            break
        word1 = word2
        retSen += " " + word1
    
    if(not (retSen[:-1].endswith(".")) and not (retSen[:-1].endswith("!")) and not (retSen[:-1].endswith("?"))):
        retSen += '.'
    print(retSen)
    return retSen





if(__name__ == "__main__"):
    #TweetCreator(input1)
    chain = MarkovChain.MarkovChain(csvParser.ImportTrumpData())
    for it in range(10):
        print("Test #" + str(it) + ':')
        MarkovReactiveTweetGen(chain, "Hillary")

