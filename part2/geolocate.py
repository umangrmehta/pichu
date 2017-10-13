#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvita Pradhan & Vaishnavi Srinivasan

import copy

total_tweets = 0
locations = {}
words = {}


class WordLocationClassifier:
	def __init__(self, location=None):
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
	return 0;


# Classify Tweet based on Prior Knowledge
def classify_tweet(tweet):
	process_copy = copy.deepcopy(tweet)
	# TODO: Tweet Pre-processing

	# Tweet Parsing here
	tweet_words = process_copy.split(" ")

	# TODO: Find Location with Max Score for each word and Then Find the Location with Max occurrence for Best Score

