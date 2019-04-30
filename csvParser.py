import csv

def ImportTrumpData():
    finalString = ""
    with open('trumpData.csv') as csvFile:
        readFile = csv.reader(csvFile, delimiter=',')
        tweetContents = []

        for i in range(800):
            row = next(readFile)

            #print(row[0])
            tweetContents.append(row[0])
        
        
        finalString = " @b@ ".join(tweetContents)
    #print(finalString)
    return finalString

if __name__ == "__main__":
    ImportTrumpData()

#print(tweetContents)