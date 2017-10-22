#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan
import sys
from collections import Counter
import copy
import re
import subprocess 

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
			processedWord=re.sub('[\[\]\\-_+=;:\"\',.?/!@#$%^&*(){}<>\n]', '', word)
			if processedWord in self.words.keys():
				self.words[processedWord] += 1
				words[processedWord] += 1
			else:
				self.words[processedWord] = 1
				if processedWord in words.keys():
					words[processedWord] += 1
				else:
					words[processedWord] = 1
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
	# TODO: Calculate and Return P(L|w) using location_classifier
	if word in location_classifier.words.keys() and word in words.keys():
		prob_word_given_location = location_classifier.words[word] / location_classifier.tweetCount
		prob_word = words[word] / total_tweets
		return prob_word_given_location / prob_word
	return 0;


# Classify Tweet based on Prior Knowledge
def classify_tweet(tweet):
	process_copy = copy.deepcopy(tweet)
	# TODO: Tweet Pre-processing

	# Tweet Parsing here
	tweet_words = process_copy.split(" ")
	

	# Find Location with Max Score for each word and Then Find the Location with Max occurrence for Best Score
	# Find Location with Max Score for each word
	for word in tweet_words:
		score = -1
		final_location_per_word = ''
		location_value_per_tweet = []
		for location in locations:
			location_per_word = location_for_word_score(word,location)
			final_location_per_word = location if location_per_word > score else final_location_per_word
		print("final" + final_location_per_word)
		location_value_per_tweet = location_value_per_tweet.append(final_location_per_word)
	# Find the Location with Max occurrence for Best Score		  
	count_of_locations = Counter(location_value_per_tweet)
	print(count_of_locations)
	final_location = ''
	maximum = max(count_of_locations.values())
	for key in count_of_locations:
		if loc_values[key] > maximum:
			final_location = key
	return final_location

trainingFile=sys.argv[1]
testingFile=sys.argv[2]
outputFile=sys.argv[3]
tweets = []

#https://gist.github.com/sebleier/554280
#https://piazza.com/class/j6lbw30o3z35cw?cid=233
nltkStopWords=['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']
nltkStemWords=['ing','ed','s','er']
#https://piazza.com/class/j6lbw30o3z35cw?cid=258
commandTrain='cat '+trainingFile+' | tr \'\200-\377\' \' \' | tr \'\\r\' \' \' > '+trainingFile+'.clean'
commandTest='cat '+testingFile+' | tr \'\200-\377\' \' \' | tr \'\\r\' \' \' > '+testingFile+'.clean'
subprocess.call(commandTrain, shell=True)
subprocess.call(commandTest, shell=True)
pattern = re.compile(r'.*,_[A-Z][A-Z]\s')

trainFile=trainingFile+'.clean'
testFile=testingFile+'.clean'

train=open(trainFile,'r')
for line in train:
	line=line.lower()
	tweets.append(line)

for tweet in tweets :
	tweet_tokens = tweet.split(" ")
	if tweet_tokens[0] in locations.keys() :
		classifier = locations[tweet_tokens[0]]
	else :
		classifier = WordLocationClassifier(tweet_tokens[0])
		locations[tweet_tokens[0]] = classifier
	classifier.parse(" ".join(tweet_tokens[1:]))

output = open(sys.argv[3],"w+")
with open(sys.argv[2],"r") as train_tweets:
	for tweet in train_tweets:
		location_for_tweet = classify_tweet(tweet)
		file.write(location_for_tweet + ' ' + tweet)
