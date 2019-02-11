from flask import Flask, request, render_template
from templates.TAnalyzer import TwitterNews
import requests
import pandas as pd
import sqlite3

# a serrver just communitcate with a client it does not or is not intended to store 
#REST api no client saving 
#the problem with tweets.txt is that it's limiited because if I want to know who wrote that tweet it won;t let you test that 

all_tweets = [] 

app = Flask(__name__)
conn = sqlite3.connect('twitter.db') #our database is twitter.db 

c = conn.cursor()

# Create table at the top of the table globally


#this was added so you don't need to create one every single time it runs 
#c.execute("CREATE TABLE IF NOT EXISTS twittertable (id INTEGER PRIMARY KEY AUTOINCREMENT, tweet text)") #creating a table with id and tweet - our id is an integer and we want it to be our primary key and we want to type in 
c.execute("CREATE TABLE IF NOT EXISTS twittertable (id INTEGER PRIMARY KEY AUTOINCREMENT, tweet text, user_tweet text, FOREIGN KEY(user_tweet) REFERENCES user(id))")
c.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text)")



# Insert a row of data


def insert(tweet, c): #the ,c is calling the c from above so we don't need to keep typing it in all the time
    query = "INSERT INTO twittertable(tweet) VALUES ('{}')".format(tweet) #the '{}' will format all the new tweets into the tweet section if we were to just type in tweet as the value then that is what it will print  
    print(query) #looking at what it will print out 
    c.execute(query)
@app.route('/twitter_clone', methods = ['GET','POST']) 
def insert_table(): #this is creating a funtion "def name():"
    conn = sqlite3.connect('twitter.db')

    c = conn.cursor()

    #it it's a POST Input: a tweet    Output: 
    if request.method == 'POST': #the client writes into the text then we receive a post from a form 
        tweet = request.form['text'] #getting the tweet through the form 
        insert(tweet, c)
        conn.commit()
    get_comments = select_table(c) #you are calling the function from below so it will show all the tweets that were typed ie you are getting the tweets 
    return render_template('twitter_clone.html', get_comments=get_comments) 
    
    
def select_table(c): #calling in the c from above 
    #input: none
    #output: tweets 
    table = c.execute("select * from twittertable;") #writing an sql statement showing all the attributes in the table 
    return table.fetchall() #this is returning all the attributes in the table


#tweets
#id INT PRIMARY KEY AUTOINK
#tweet - text 
#user_id INT FOREIGN KEY 

#user table 
#id 
#username
#password  




with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/positive_words.txt', 'r') as open_pos:
    positive_vocab=open_pos.readlines()
    positive_vocab = list(map(lambda word: word.replace("\n", ""), positive_vocab)) #this take away the "/n" at the end of every tweet or comment

with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/negative_words.txt', 'r') as open_neg:
    negative_vocab=open_neg.readlines()
    negative_vocab = list(map(lambda word: word[:-1], negative_vocab)) #another way of removing the "/n" at the end of a tweet


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/twitter', methods=['GET'])
def my_form_post():
    text = request.args.get('text') #creating a variable called text
    currenttweets = get_tweets(text)
    #print(currenttweets)
    return render_template('index.html', text=text, currenttweets=currenttweets)

#this is a new route localhost:5000/tweets_list
@app.route('/tweets_list', methods = ['GET','POST'])
def post_dict():
    if request.method == 'POST':
        tweet = request.form['text']
        all_tweets.append(tweet)
    return render_template('tweet_dict.html', all_tweets=all_tweets)


#reading files so that they don't delete every time after you restart 
@app.route('/tweets_files', methods = ['GET','POST'])
def post_files():
    if request.method == 'POST':
        tweet = request.form['text']
        write_files(tweet)
    read = read_files()
    return render_template('saved_files.html', read = read)


def read_files():
    # Input: none
    # Output: all tweets in tweets.txt
    with open('tweets.txt', 'r') as f:
        x = f.readlines()
        return x


def write_files(tweet):
    # Input: tweet (str)
    # Output: nothing
    with open('tweets.txt', 'a+') as f:
        y = f.write(tweet + "\n")
        return y 



#HELPER FUNCTION
def get_tweets(searchitem):
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23{}&result_type=recent'.format(searchitem)
    headers = {'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKKX9QAAAAAAqPRkW0wMLgOF29YuPvrLJLMETI0%3D3x0GtJuEXLEIzYvRKG8fjPB02vwQJp7xd5Z2rOBWY4jGmnD7Ma'}
    res = requests.get(url, headers=headers)

    status = res.json()['statuses'] #inside the res(responses there is a bunch of information about the tweet and we want to get the text so inside the statues there is text so we first get the statuses try print out the repsonses to see what's inside then print out the statues to see if the text is actually in there)
    
    tweetlist = [] #a list that will have the sentiment and the text for each tweet 

    twitter_analyzer = TwitterNews(positive_vocab, negative_vocab) #you are calling the class TwitterNew from TAnalyzer.py

    for item in status: #now we are trying to get the text that is inside the status 
        #print(item['text'])
        tweet = item['text']
        
        sentiment, percentagepos, percentageneg = twitter_analyzer.analyze_news(tweet) #you are calling the sentiment part from the TwitterNews class called analyze_news
        #print(sentimenttweet)
        # {'sentiment': 'positive', 'tweet': 'i love twitter'} -structure of a dictionary
        actualtweets = {}  #a dictionary
        actualtweets["Sentiment"] = sentiment #the key - the right hand side is calling the sentiment tweets made from above 
        actualtweets["Tweet"] = tweet #the value
        actualtweets["Percent Positive"] = percentagepos
        actualtweets["Percent Negative"] = percentageneg

        #print(actualtweets) 

        tweetlist.append(actualtweets) #adding the acutaltweets dictionary into the tweetlist 
   
    
    return tweetlist

    #data = pd.DataFrame(data=[actualtweets], columns=['Tweets'])


if __name__ == '__main__':
  app.run() 



