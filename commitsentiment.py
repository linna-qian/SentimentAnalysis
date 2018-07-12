from textblob import TextBlob
import urllib.request, json
import math

def print_information(inputrepo):
    with urllib.request.urlopen("https://api.github.com/repos/apache/hadoop/comments") as url:
        data = json.loads(url.read().decode()) 
        sequenceDict = {}
        previousday = 0
        previousmessage = "Hi"
        combinedlist = []
        for index, elem in enumerate(data):
            sequenceDict[index] = elem
            if 'created_at' in elem:
                dates = []
                dates = elem['created_at'] 
                shortdates = dates[:10]
                if "html lang" in elem['body']:
                    print("This body contains additional html text.")
                else:
                    messages = []
                    messages = elem['body']
                    sentence = TextBlob(messages)
                    sentiments = []
                    sentiments = sentence.sentiment.polarity
                    shortsenti = '%.2f' % sentiments
                    if previousday == shortdates:
                        combined = previousmessage + ' ' + messages
                        newsenti = TextBlob(combined)
                        sentis = []
                        sentis = newsenti.sentiment.polarity
                        ssentis = '%.2f' % sentis
                        tabledata = [shortdates, combined, ssentis]
                    else:
                        tabledata = [shortdates, messages, shortsenti]
                    if previousday == shortdates:
                        previousmessage = combined
                    else:
                        previousmessage = messages
                    previousday = shortdates
                    combinedlist.append(tabledata)

    combinedlist.append(['2100-01-01', 'NaN', 0])
    for i, item in enumerate(range(len(combinedlist) - 1)):
        if combinedlist[i][0] < combinedlist[i + 1][0]:
            print(combinedlist[i])

print("What is the repository name?")
inputrepo = input()
if inputrepo == 'hadoop':
    print_information(inputrepo)
else:
    print("No repository information available.")
