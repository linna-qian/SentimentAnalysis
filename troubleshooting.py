import urllib.request, json

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def print_commit_hash(inputrepo): 
    opener = AppURLopener()
    response = opener.open("https://api.github.com/repos/mtedone/podam/commits")
    data = json.loads(response.read().decode())
    sequenceDict = {}
    for index, elem in enumerate(data):
        sequenceDict[index] = elem
        if 'sha' in elem:
            commithash = []
            commithash = elem['sha']
            if 'commit' in elem:
                commit = []
                commit = elem['commit']
                if 'author' in commit:
                    author = []
                    author = commit['author']
                    if 'date' in author:
                        date = []
                        date = author['date']
                        shortdate = date[:10]
                        commitid = [shortdate, commithash]
                        print(commitid)

print("What is the repository name?")
inputrepo = input()
if inputrepo == 'mtedone/podam':
    print_commit_hash(inputrepo)
else:
    print("No repository information available.")
