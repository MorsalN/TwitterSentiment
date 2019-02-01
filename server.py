from flask import Flask, request, render_template
from templates.TAnalyzer import TwitterNews
import requests

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/twitter', methods=['GET'])
def my_form_post():
    text = request.args.get('text')
    currenttweets = get_tweets(text)
    print(currenttweets)
    return render_template('index.html', text=text, currenttweets=currenttweets)


#HELPER FUNCTION
def get_tweets(searchitem):
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23{}&result_type=recent'.format(searchitem)
    headers = {'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKKX9QAAAAAAqPRkW0wMLgOF29YuPvrLJLMETI0%3D3x0GtJuEXLEIzYvRKG8fjPB02vwQJp7xd5Z2rOBWY4jGmnD7Ma'}
    res = requests.get(url, headers=headers)

    status = res.json()['statuses'] #inside the res(responses there is a bunch of information about the tweet and we want to get the text so inside the statues there is text so we first get the statuses try print out the repsonses to see what's inside then print out the statues to see if the text is actually in there)
    
    tweetlist = [] #a list that will have the sentiment and the text for each tweet 

    twitter_analyzer = TwitterNews() #you are calling the class TwitterNew from TAnalyzer.py
    
    for item in status: #now we are trying to get the text that is inside the status 
        #print(item['text'])
        tweet = item['text']
        sentimenttweet = twitter_analyzer.analyze_news(tweet) #you are calling the sentiment part from the TwitterNews class called analyze_news
        #print(sentimenttweet)
        # {'sentiment': 'positive', 'tweet': 'i love twitter'} -structure of a dictionary
        actualtweets = {}  #a dictionary
        actualtweets["sentiment"] = sentimenttweet #the key - the right hand side is calling the sentiment tweets made from above 
        actualtweets["tweet"] = tweet #the value
        #print(actualtweets) 

        tweetlist.append(actualtweets) #adding the acutaltweets dictionary into the tweetlist 

    
    return tweetlist


if __name__ == '__main__':
  app.run() 

