from collections import defaultdict

def MarkovChain(text):

    tokens = text.split(' ')

    d = defaultdict(list)

    for token, nToken in zip(tokens[0:-1], tokens[1:]):
        d[token].append(nToken)

    ret = dict(d)

    return ret