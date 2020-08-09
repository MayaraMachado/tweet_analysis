from textblob import TextBlob as tb

class AnalizadorPoralidade():

    def __init__(self):
        self.analysis = None

    def tweet_list_analyzer(self, tweets):
        '''
        '''

        tweets_score = []
        for tweet in tweets:
            # print(f"\n {tweet.full_text}")
            analysis = tb(tweet.full_text)

            if analysis.detect_language() != 'en':
                print(f'traduzido')
                translate = tb(str(analysis.translate(to='en')))
                polarity = translate.sentiment.polarity
            else:
                polarity = analysis.sentiment.polarity
            
            tweets_score.append(polarity)

        return tweets_score
