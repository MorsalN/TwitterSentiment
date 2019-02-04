#Importing the top 5 stories and top 5 comments
class TwitterNews:
    def __init__(self, positive_vocab, negative_vocab):
        self.positive_vocab = positive_vocab #you are calling the vocab from above
        self.negative_vocab = negative_vocab

    def clean_tweets(self, tweet):
        """
        Input: tweet (str)
        Output: words (list) without #, @, $
        """
        tweet = tweet.lower() #these are making the tweets on twitter lowercase, taking away #,@ etc. and replacing it with ""(which is blank)
        tweet = tweet.replace("#", "")  #so that our analyzer can give us an analysis without being confused
        tweet = tweet.replace("@","")
        tweet = tweet.replace("$", "")
        return tweet

    def analyze_news(self, tweet):
        tweet = self.clean_tweets(tweet)
        words = tweet.split()

        num_positive_vocab = 0
        num_negative_vocab = 0
        percentagepos = 0
        percentageneg = 0
        sentiment = ""

        for word in words:
            if word in self.positive_vocab:
                num_positive_vocab += 1 
            elif word in self.negative_vocab:
                num_negative_vocab += 1 
                #print(num_negative_vocab)
        total = num_positive_vocab + num_negative_vocab
        #print("total: " + str(total))
        try:
            percentagepos = round((num_positive_vocab/total)*100,2)
            percentageneg = round((num_negative_vocab/total)*100,2)
        except ZeroDivisionError:
            percentagepos = 0
            percentageneg = 0

        print(percentageneg)

        if num_positive_vocab != num_negative_vocab:
            if num_positive_vocab > num_negative_vocab:
               # print("positive: " + str(percentage))
                sentiment =  "Positive"
            if num_positive_vocab < num_negative_vocab:
                #total = len(positive_vocab) + len(negative_vocab)
                
                #print("negative: " + str(percentage))
                sentiment =  "Negative"
        else:
            sentiment = "Neutral"

        return sentiment, percentagepos, percentageneg

        

