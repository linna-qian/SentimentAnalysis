user_input = input()
import sentistrength
senti = sentistrength('EN')
result = senti.get_sentiment(user_input)
print(result)
