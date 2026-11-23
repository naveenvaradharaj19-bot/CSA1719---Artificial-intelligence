# Sentiment Analysis

positive_words = [
    "good", "great", "happy", "excellent",
    "love", "wonderful", "best"
]

negative_words = [
    "bad", "sad", "hate", "poor",
    "worst", "terrible"
]

sentence = "I love this movie and it is excellent"

words = sentence.lower().split()

positive_count = 0
negative_count = 0

for word in words:
    word = word.strip(".,!?")

    if word in positive_words:
        positive_count += 1

    if word in negative_words:
        negative_count += 1

if positive_count > negative_count:
    sentiment = "Positive"
elif negative_count > positive_count:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Sentiment:", sentiment)
