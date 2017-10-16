#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan

import copy

total_tweets = 0
locations = {}
words = {}


class WordLocationClassifier:
	def __init__(self, location):
		self.location = location
		self.words = {}
		self.tweetCount = 0

	def parse(self, tweet):
		process_copy = copy.deepcopy(tweet)
		# TODO: Training Tweet Pre-processing

		# Training Tweet Parsing here
		tweet_words = process_copy.split(" ")
		for word in tweet_words:
			if word in self.words.keys():
				self.words[word] += 1
				words[word] += 1
			else:
				self.words[word] = 1
				if word in words.keys():
					words[word] += 1
				else:
					words[word] = 1
		self.tweetCount += 1

	def top_5_words(self):
		location_scores = {}
		for word in self.words.keys():
			location_scores[word] = location_for_word_score(word, self)

		top5 = {}
		while len(top5) < 5:
			top = {k: v for k, v in location_scores.items() if v == max(location_scores.values())}
			top5 += top
			location_scores -= top
		return top5


# Returns P(L|w) for the given Location and Word
def location_for_word_score(word, location_classifier):
	location_classifier
	# TODO: Calculate and Return P(L|w) using location_classifier
	for key in location_classifier.words:
		prob_word_given_location=key/location_classifier.tweetCount
	return 0;


# Classify Tweet based on Prior Knowledge
def classify_tweet(tweet):
	process_copy = copy.deepcopy(tweet)
	# TODO: Tweet Pre-processing

	# Tweet Parsing here
	tweet_words = process_copy.split(" ")

	# TODO: Find Location with Max Score for each word and Then Find the Location with Max occurrence for Best Score


tweets = []
USAStatesAbbr = [',_AS',',_DC',',_FM',',_GU',',_MH',',_MP',',_PW',',_PR',',_VI',',_AL',',_AK',',_AZ',',_AR',',_CA',',_CO',',_CT',',_DE',',_FL',',_GA',',_HI',',_ID',',_IL',',_IN',',_IA',',_KS',',_KY',',_LA',',_ME',',_MD',',_MA',',_MI',',_MN',',_MS',',_MO',',_MT',',_NE',',_NV',',_NH',',_NJ',',_NM',',_NY',',_NC',',_ND',',_OH',',_OK',',_OR',',_PA',',_RI',',_SC',',_SD',',_TN',',_TX',',_UT',',_VT',',_VA',',_WA',',_WV',',_WI',',_WY']
try:
	trainFile = open("/nfs/nfs7/home/vsriniv/a2/tweets.test2.txt", "rt")
except:
	trainFile = open("/nfs/nfs7/home/vsriniv/a2/tweets.test2.txt", "rt", encoding="latin1")

for line in trainFile:
	parsedLine = line.split(" ")
	if any(parsedLine[0][-4:] in statesAbbr for statesAbbr in USAStatesAbbr):
		tweetLine = ""
		tweets.append(tweetLine)
		tweetLine = str(line).rstrip("\n\r")
		total_tweets += 1
	else:
		tweetLine = (tweetLine + " " + str(line)).rstrip("\n\r")


for tweet in tweets:
	tweet_tokens = tweet.split(" ")
	if tweet_tokens[0] in locations.keys():
		classifier = locations[tweet_tokens[0]]
	else:
		classifier = WordLocationClassifier(tweet_tokens[0])
		locations[tweet_tokens[0]] = classifier
	classifier.parse(" ".join(tweet_tokens[1:]))