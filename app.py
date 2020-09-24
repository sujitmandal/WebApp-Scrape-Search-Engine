from ScrapeSearchEngine.ScrapeSearchEngine import Google
from ScrapeSearchEngine.ScrapeSearchEngine import Duckduckgo
from ScrapeSearchEngine.ScrapeSearchEngine import Ecosia
from ScrapeSearchEngine.ScrapeSearchEngine import Givewater
from ScrapeSearchEngine.ScrapeSearchEngine import Bing
from flask import Flask, render_template

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
"""

userAgent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36') #my user agent
search = ('pyhon') #Enter Anything for Search

app = Flask(__name__)

'''
@app.route('/')
def home():
	return(render_template('home.html'))'''

@app.route('/')
def Links():
	googleSearch = Google(search, userAgent)
	duckduckgoSearch = Duckduckgo(search, userAgent)
	givewaterSearch = Givewater(search, userAgent)
	ecosiaSearch = Ecosia(search, userAgent)
	bingSearch = Bing(search, userAgent)

	googleSet = set(googleSearch)
	duckduckgoSet = set(duckduckgoSearch)
	givewaterSet = set(givewaterSearch)
	ecosiaSet = set(ecosiaSearch)
	bingSet = set(bingSearch)

	intersection1 = googleSet.intersection(givewaterSet)
	intersection2 = intersection1.intersection(duckduckgoSet)
	intersection3 = intersection2.intersection(ecosiaSet)
	intersection4 = intersection3.intersection(bingSet)

	intersectionList = list(intersection4)
	finalList = []

	for i in intersectionList:
		finalList.append(i)

	keys = []
	for j in range(len(finalList)):
		key = j + 1
		keys.append(key)

	commonLinks = {}
	commonLinks = dict(zip(keys, finalList))

	return(render_template('base.html', commonLinks=commonLinks))


if __name__ == "__main__":
	app.run(port=8000)