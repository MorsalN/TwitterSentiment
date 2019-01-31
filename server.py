from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/twitter', methods=['GET'])
def my_form_post():
	text = request.args.get('text')
	return render_template('index.html', text=text)

#HELPER FUNCTION
def get_tweets(searchitem):
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23{}&result_type=recent'.format(searchitem)
    headers = {'authorization': 'Bearer <BEARERTOKEN>'}
    res = requests.get(url, headers=headers)

if __name__ == '__main__':
  app.run() 