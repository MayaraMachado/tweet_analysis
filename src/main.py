import numpy as np
from twitter import TwitterConnection
from polaridade import AnalizadorPoralidade

class Main():

    def __init__(self):
        '''
        '''
        self.twitterAPI = TwitterConnection()
        self.polaridade = AnalizadorPoralidade()

    def get_mypublic_tweets(self):
        for tweet in self.twitterAPI.get_mypublic_tweets:
            print(tweet.text)

    def search_tweets(self, keyword):
        tweets = self.twitterAPI.search_by_keyword(keyword, count=10)
        return tweets

    def analyze_tweets_sentiments(self, keyword):
        tweets = self.search_tweets(keyword)
        sentiments = self.polaridade.tweet_list_analyzer(tweets)

        print(f"Vetor de polaridade: {sentiments}")
        polarity_mean = np.mean(sentiments)

        return polarity_mean




if __name__ == '__main__':
    main = Main()
    keyword = ('covid OR covid-19 OR corona OR coronavirus')

    print(main.analyze_tweets_sentiments(keyword))

    # tweets = main.search_tweets(keyword)
    # for tweet in tweets:
    #     print(f"User: {tweet.user.screen_name} - Tweet: {tweet.full_text} - \n")


