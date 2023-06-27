from textblob import TextBlob
from GoogleNews import GoogleNews


def get_emotions(company_name: str):

    googlenews = GoogleNews()
    googlenews.search(company_name)
    news = googlenews.result(sort=True)

    sentiment_scores = []

    for new in news:
        analysis = TextBlob(new['desc'])

        sentiment = 0  # 0 is positive, 1 is neutral, 2 is negative
        if analysis.sentiment.polarity > 0:
            sentiment = 0
        elif analysis.sentiment.polarity < 0:
            sentiment = 2
        else:
            sentiment = 1

        sentiment_scores.append(sentiment)

    # Calculate sentiment score percentage
    total_tweets = len(sentiment_scores)
    positive_tweets = sentiment_scores.count(0)
    neutral_tweets = sentiment_scores.count(1)
    negative_tweets = sentiment_scores.count(2)


    positive_percentage = (positive_tweets / total_tweets) * 100
    neutral_percentage = (neutral_tweets / total_tweets) * 100
    negative_percentage = (negative_tweets / total_tweets) * 100

    # Print results
    print(f"Positive tweets: {positive_percentage:.2f}%")
    print(f"Neutral tweets: {neutral_percentage:.2f}%")
    print(f"Negative tweets: {negative_percentage:.2f}%")

    return positive_percentage, neutral_percentage, negative_percentage, news[:5]
