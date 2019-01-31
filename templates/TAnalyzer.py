#Importing the top 5 stories and top 5 comments

import requests

class TwitterNews:
    def __init__(self, positive_vocab, negative_vocab):
        self.positive_vocab = positive_vocab
        self.negative_vocab = negative_vocab

    
    def analyze_news(self, tweets):
        words = tweets.split()

        num_positive_vocab = 0 
        num_negative_vocab = 0 
        for word in words:
         
            if word in positive_vocab:
                num_positive_vocab += 1
            elif word in negative_vocab:
                num_negative_vocab += 1 

        if num_positive_vocab > num_negative_vocab:
            return "positive"

        elif num_positive_vocab < num_negative_vocab:
            return "negative"
        else: 
            return "inconclusive" 

        for sentence in listOfStories:
            tweets = sentence.split(",").strip()

            analyze_news(tweets)
    
 #   hacker = input("What do you want to analyze?")
  #  analyze_news(hacker)
  #  print(analyze_news(hacker))
#

with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/positive_words.txt', 'r') as open_pos:
    positive_vocab=open_pos.readlines()

with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/negative_words.txt', 'r') as open_neg:
    negative_vocab=open_neg.readlines()

tn = TwitterNews(positive_vocab, negative_vocab)

response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%23{}&result_type=recent'.format(searchitem)')

# Get top 5 ids
top_five_ids = response.json()[:5]
print(top_five_ids)



# Fetch top 5 tweets 

tweetsposted = []

for top_id in top_five_ids:
    curr_post_api_url = ''https://api.twitter.com/1.1/search/tweets.json?q=%23{}&result_type=recent'.format(top_id)
    curr_post = requests.get(curr_post_api_url)
    print(curr_post.json())
    tweetsposted.append(curr_post.json())


#print results
for l in listOfTweets:
    print(l)
    print("\n")