from collections import defaultdict

def MarkovChain(text):

    tokens = text.split(' ')

    d = defaultdict(list)

    # Sets a dictionary of lists of tokens that follow the key token, The frequency of the token following the previous token
    # is accounted for with repeated entries in the list. This gives a rough probability of the Tokens being chosen in a similiar
    # order to how they are written in the text.

    # @b@ is a special token that was created to signify the begining of a new tweet. This is used to find the most common words
    # that trump starts tweets with.

    tokens.remove('')
    for token, nToken in zip(tokens[0:-1], tokens[1:]):
        # Filtering out Retweets from the start tweet token
        if(token == "@b@" and nToken.endswith(':')):
            #print("ommiting: " + nToken) ---DEBUGGING
            pass
        else:
            d[token].append(nToken)

    ret = dict(d)

    return ret