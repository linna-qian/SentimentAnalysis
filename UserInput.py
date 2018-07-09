from textblob import TextBlob
import urllib.request, json
import math
import itertools

with urllib.request.urlopen("https://api.github.com/repos/apache/hadoop/comments") as url:
    data = json.loads(url.read().decode()) 
    sequenceDict = {}
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
                sentence = TextBlob(elem['body'])
                sentiments = []
                sentiments = sentence.sentiment.polarity
                shortsenti = '%.2f' % sentiments
                tabledata = [shortdates, messages, shortsenti]
                print(tabledata)