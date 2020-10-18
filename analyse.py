# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:08:07 2020

@author: Skywalker
"""

import argparse
import tweepy
import re
import secrets
from textblob import TextBlob
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('-n', help='number of tweets', type=int, default=100)
group = parser.add_mutually_exclusive_group()
group.add_argument('-id', help='twitter id', type=str)
group.add_argument('-s', help='search trend', type=str)

args = parser.parse_args()

id = args.id
num = args.n
search = args.s


class API():
	def __init__(self, apikey, apisec, tokn, toknsec):
		self.apikey = apikey
		self.apisec = apisec
		self.tokn = tokn
		self.toknsec = toknsec
	def Login(self):
		try:
			self.auth = tweepy.OAuthHandler(self.apikey, self.apisec)
			self.auth.set_access_token(self.tokn, self.toknsec)
			self.api = tweepy.API(self.auth)
			print("Authenticated")
		except:
			print("Error: Authentication Failed")
	def percentage(self, part, whole):
		return 100 * float(part)/float(whole)
	def scrape(self):
		self.Login()
		#user_tweets = self.api.user_timeline(screen_name=id, count=num)
		fetched_tweets = self.api.search(q=search, count=num)
		print("Tweets Fetched")
		positive = 0
		negative = 0
		neutral = 0
		print("Analysing public sentiments...")
		for tweet in fetched_tweets:
			blob = TextBlob(tweet.text)
			blob = blob.correct()
			pol = blob.sentiment.polarity
			if pol > 0:
				positive += 1
			elif pol < 0:
				negative += 1
			elif pol == 0:
				neutral += 1

			#sen = sentence.sentiment
		analysis = ['Positive', 'Negative', 'Neutral']
		colors = ['g', 'r', 'y']
		explode = [0, 0.1, 0]
		positive2 = self.percentage(positive, num)
		negative2 = self.percentage(negative, num)
		neutral2 = self.percentage(neutral, num)

		slices = [format(positive2), format(negative2), format(neutral2)]
		print("Visualizing....")
		plt.pie(slices, explode=explode, labels=analysis, colors=colors, startangle=90, shadow=True, autopct='%.1f%%')
		plt.axis('equal')
		plt.savefig(search)
		plt.title(f"Sentiment Analysis: {search}")
		plt.show()



apikey = secrets.apikey
apisec = secrets.apisec
tokn = secrets.tokn
toknsec = secrets.toknsec

print("Processing...")
API(apikey, apisec, tokn, toknsec).scrape()
print("Done")


