import tweepy
from decouple import config

class TwitterConnection():

    def __init__(self):
        '''
        '''

        consumer_key = config('TWITTER_API_KEY')
        consumer_secret = config('TWITTER_SECRET_KEY')
        access_token = config('TWITTER_ACCESS_TOKEN')
        access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.apiConn = tweepy.API(auth)

    def get_mypublic_tweets(self):
        my_public_tweets = self.apiConn.home_timeline()
        return my_public_tweets

    def search_by_keyword(self, keyword, count=10, result_type='mixed', lang='pt', tweet_mode='extended'):
        '''
            Faz busca em tweets por palavra chave.

            - Tiṕos de result_type:
                - mixed (default)
                - recent
                - popular

        '''
        tweets_list = self.apiConn.search(q=keyword, count=count, result_type=result_type, tweet_mode=tweet_mode)
        # tweets_list = self.api.search(q=keyword, count=count, result_type=result_type)
        return tweets_list
