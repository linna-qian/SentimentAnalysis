import urllib.request, json

def print_information(inputrepo):
    with urllib.request.urlopen("https://api.github.com/repos/mtedone/podam/statuses/f5ef93dd0aadc4ce67f06fa3cdc0dca1f703b8a4") as url:
        data = json.loads(url.read().decode()) 
        sequenceDict = {}
        for index, elem in enumerate(data):
            sequenceDict[index] = elem
            if 'created_at' in elem:
                dates = []
                dates = elem['created_at'] 
                shortdates = dates[:10]
                if 'state' in elem:
                    statuses = []
                    statuses = elem['state']
                    dayresult = [shortdates, statuses]
                    print(dayresult)

print("What is the repository name?")
inputrepo = input()
if inputrepo == 'podam':
    print_information(inputrepo)
else:
    print("No repository information available.")