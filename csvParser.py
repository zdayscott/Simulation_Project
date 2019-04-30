import csv

def ImportTrumpData():
    finalString = ""
    with open('trumpData.csv') as csvFile:
        readFile = csv.reader(csvFile, delimiter=',')
        tweetContents = []

        for i in range(831):
            row = next(readFile)
            tweet = row[0]
            if "http" not in tweet:
                tweet.replace("â€™", '\'')
                tweetContents.append(tweet)

            #print(tweet)
        #next(readFile)
        finalString = " @b@ ".join(tweetContents)
    # csvFile.close()
    # print("First Done!")
    # with open('trumpData1.csv') as csvFile:
    #     readFile = csv.reader(csvFile, delimiter=',')
    #     tweetContents = []

    #     for i in range(831):
    #         row = next(readFile)
    #         tweet = row[0]
    #         if "http" not in tweet:
    #             tweet.replace("â€™", '\'')
    #             tweetContents.append(tweet)

    #         print(tweet)
    #     #next(readFile)
    #     finalString = " @b@ ".join(tweetContents)
    # #print(finalString)
    return finalString

if __name__ == "__main__":
    ImportTrumpData()

#print(tweetContents)