from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from collections import Counter
from flask import render_template
from ScrapeSearchEngine.ScrapeSearchEngine import Google
from ScrapeSearchEngine.ScrapeSearchEngine import Duckduckgo
from ScrapeSearchEngine.ScrapeSearchEngine import Ecosia
from ScrapeSearchEngine.ScrapeSearchEngine import Givewater
from ScrapeSearchEngine.ScrapeSearchEngine import Bing
from ScrapeSearchEngine.ScrapeSearchEngine import Yahoo

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""

userAgent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36') #my user agent

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return(render_template('home.html'))

def dictionary(lists):
	finalList = []

	for i in lists:
		finalList.append(i)

	keys = []
	for j in range(len(finalList)):
		key = j + 1
		keys.append(key)

	commonLinks = {}
	commonLinks = dict(zip(keys, finalList))
	return(commonLinks)

@app.route('/result', methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		search = request.form['txt_search']

		googleSearch = Google(search, userAgent)
		duckduckgoSearch = Duckduckgo(search, userAgent)
		duckduckgoSearch = duckduckgoSearch[:10]
		givewaterSearch = Givewater(search, userAgent)
		ecosiaSearch = Ecosia(search, userAgent)
		bingSearch = Bing(search, userAgent)
		yahooSearch = Yahoo(search, userAgent)

		googoleLinks = dictionary(googleSearch)
		duckduckgoLinks = dictionary(duckduckgoSearch)
		givewaterLinks = dictionary(givewaterSearch)
		ecosiaLinks = dictionary(ecosiaSearch)
		bingLinks = dictionary(bingSearch)
		yahooLinks = dictionary(yahooSearch)

		link = []
		for i in googleSearch:
			link.append(i)
		for j in duckduckgoSearch:
			link.append(j)
		for k in givewaterSearch:
			link.append(k)
		for l in ecosiaSearch:
			link.append(l)
		for m in bingSearch:
			link.append(m)
		for n in yahooSearch:
			link.append(n)
	
		commonLink = Counter(link)
	
		commonLinks = sorted(commonLink.items(), key=lambda value: value[1], reverse=True)
		commonLinks = dict(commonLinks)

		finalText = []
		finalLink = []

		text = []
		value = []

		for keys, values in commonLinks.items():
			text.append(keys)
			value.append(values)

		for s in range(len(text)):
			texts = text[s] + ' ' + str(value[s])
			finalText.append(texts)

		for link in commonLinks.keys():
			finalLink.append(link)

		finalResults = zip(finalLink, finalText)

		return(render_template('result.html', 	googoleLinks=googoleLinks, 
												duckduckgoLinks=duckduckgoLinks, 
												givewaterLinks=givewaterLinks, 
												ecosiaLinks=ecosiaLinks,
												bingLinks=bingLinks, 
												yahooLinks=yahooLinks, 
												finalResults=finalResults))
	return(None)

if __name__ == "__main__":
	app.run(
		port=8000
		)
