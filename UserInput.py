from textblob import TextBlob
user_input = input()
sentence = TextBlob(user_input)
print(sentence.sentiment)
