#Importing the top 5 stories and top 5 comments
with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/positive_words.txt', 'r') as open_pos:
    positive_vocab=open_pos.readlines()
    positive_vocab = list(map(lambda word: word.replace("\n", ""), positive_vocab)) #this take away the "/n" at the end of every tweet or comment

with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/negative_words.txt', 'r') as open_neg:
    negative_vocab=open_neg.readlines()
    negative_vocab = list(map(lambda word: word[:-1], negative_vocab)) #another way of removing the "/n" at the end of a tweet


class TwitterNews:
    def __init__(self):
        self.positive_vocab = positive_vocab #you are calling the vocab from above
        self.negative_vocab = negative_vocab

    
    def analyze_news(self, tweet):
        
        tweet = tweet.lower() #these are making the tweets on twitter lowercase, taking away #,@ etc. and replacing it with ""(which is blank)
        tweet = tweet.replace("#", "")  #so that our analyzer can give us an analysis without being confused
        tweet = tweet.replace("@","")
        tweet = tweet.replace("$", "")
        words = tweet.split()
        print(self.positive_vocab) #need to put the self.
        print(self.negative_vocab)

        num_positive_vocab = 0 
        num_negative_vocab = 0 
        for word in words:
            if word in self.positive_vocab:
                num_positive_vocab += 1 
            elif word in self.negative_vocab:
                num_negative_vocab += 1 
                print(num_negative_vocab)
               

        if num_positive_vocab > num_negative_vocab:
            
            return "positive"

        elif num_positive_vocab < num_negative_vocab:
            return "negative"
        else: 
            return "neutral" 

        

