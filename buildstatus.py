import urllib.request, json
from textblob import TextBlob

def print_information(inputrepo):
    with urllib.request.urlopen("https://api.github.com/repos/mtedone/podam/commits") as url:
        data = json.loads(url.read().decode()) 
        sequenceDict = {}
        for index, elem in enumerate(data):
            sequenceDict[index] = elem
            if 'sha' in elem:
                commithash = []
                commithash = elem['sha']
                if 'commit' in elem:
                    commit = []
                    commit = elem['commit']
                    if 'message' in commit:
                        message = []
                        message = commit['message']
                        sentence = TextBlob(message)
                        sentiments = []
                        sentiments = sentence.sentiment.polarity
                        shortsenti = '%.2f' % sentiments
                        statusurl = "https://api.github.com/repos/mtedone/podam/statuses" + "/" + commithash
                        with urllib.request.urlopen(statusurl) as url2:
                            data2 = json.loads(url2.read().decode())
                            sequenceDict2 = {}
                            for num, item in enumerate(data2):
                                sequenceDict2[num] = item
                                if 'created_at' in item:
                                    dates = []
                                    dates = item['created_at'] 
                                    shortdates = dates[:10]
                                    if 'state' in item:
                                        statuses = []
                                        statuses = item['state']
                                        print([shortdates, commithash, shortsenti, statuses])

print("What is the repository name?")
inputrepo = input()
if inputrepo == 'mtedone/podam':
    print_information(inputrepo)
else:
    print("No repository information available.")