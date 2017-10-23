#!/usr/bin/python
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan
import sys
from collections import Counter
import copy
import re
import subprocess
import os
import math
import string

totalTweets = 0
locations = {}
words = {}


def postProcessingWords(word):
	processedWord = re.sub('[\[\]\\-_+=;:\"\',.?/!@#$%^&*(){}<>~`\|\n]', '', word)
	# processedWord = word.translate(None, string.punctuation)
	if processedWord in nltkStopWords:
		processedWord = ''
	# if processedWord.endswith(nltkStemWords):
	# 	stemWord = next((stemWord for stemWord in nltkStemWords if processedWord.endswith(stemWord)), None)
	# 	processedWord.rstrip(stemWord)
	return processedWord


class WordLocationClassifier:
	def __init__(self, location):
		self.location = location
		self.words = {}
		self.tweetCount = 0

	def parse(self, tweet):
		process_copy = copy.deepcopy(tweet)
		# Training Tweet Parsing here
		tweet_words = process_copy.split(" ")
		for word in tweet_words:
			processedWord = postProcessingWords(word)
			if processedWord == '':
				continue
			elif processedWord in self.words.keys():
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
			top5.update(top)
			for key in top.keys():
				location_scores.pop(key)
		return top5.keys()[:5]


# Returns ln(P(L|w)) for the given Location and Word
def location_for_word_score(tweetWords, locationClassifier):
	# TODO: Calculate and Return ln(P(L|w)) using location_classifier
	probWordGivenLocation = 1
	for word in tweetWords:
		if word in locationClassifier.words.keys():
			probWordGivenLocation *= float(locationClassifier.words[word]) / locationClassifier.tweetCount
		else:
			probWordGivenLocation *= 1.0 / locationClassifier.tweetCount
		# if word in words.keys():
		# 	prob_word = math.log(words[word] + 1) - math.log(totalTweets)
		# else:
		# 	prob_word = - math.log(totalTweets)
	probLocation = float(locationClassifier.tweetCount) / totalTweets
	return probWordGivenLocation * probLocation


# Classify Tweet based on Prior Knowledge
def classify_tweet(tweet):
	processedWords = []
	locationPerWord=0
	testLocations={}
	process_copy = copy.deepcopy(tweet)
	tweet_words = process_copy.split(" ")
	for word in tweet_words[1:]:
		processedWords.append(postProcessingWords(word))

	for location, classifier in locations.items():
		# for word in processedWords:
		# 	locationPerWord += location_for_word_score(word, classifier)
		# 	testLocations[location] = locationPerWord
		locationForWordScore = location_for_word_score(processedWords, classifier)
		testLocations[location] = locationForWordScore
	return [k for k, v in testLocations.items() if v == max(testLocations.values())][0]

#trainingFile=sys.argv[1]
#testingFile=sys.argv[2]
#outputFile=sys.argv[3]
trainingFile='tweets.train.txt'
testingFile='tweets.test1.txt'
outputFile='outputFile.txt'
tweets = []

# https://gist.github.com/sebleier/554280
# https://piazza.com/class/j6lbw30o3z35cw?cid=233
nltkStopWords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
nltkStemWords=('ing', 'ed', 's', 'er')
# https://piazza.com/class/j6lbw30o3z35cw?cid=258

cwd = os.getcwd()
commandTrain='cat '+cwd+'/'+trainingFile+' | tr \'\200-\377\' \' \' | tr \'\\r\' \' \' > '+cwd+'/'+trainingFile+'.clean'
commandTest='cat '+cwd+'/'+testingFile+' | tr \'\200-\377\' \' \' | tr \'\\r\' \' \' > '+cwd+'/'+testingFile+'.clean'
processTrain = subprocess.Popen(commandTrain, shell=True, stdout=subprocess.PIPE)
outTrain,errTrain = processTrain.communicate()
processTest = subprocess.Popen(commandTest, shell=True, stdout=subprocess.PIPE)
outTest,errTest = processTest.communicate()
pattern = re.compile(r'.*,_[A-Z][A-Z]\s')

trainFile = cwd+'/'+trainingFile+'.clean'
testFile = cwd+'/'+testingFile+'.clean'
outFile = cwd+'/'+outputFile

train = open(trainFile, 'r')
for line in train:
	line = line.lower()
	tweets.append(line)

for tweet in tweets:
	tweet_tokens = tweet.split(" ")
	if tweet_tokens[0] in locations.keys():
		classifier = locations[tweet_tokens[0]]
	else:
		classifier = WordLocationClassifier(tweet_tokens[0])
		locations[tweet_tokens[0]] = classifier
	classifier.parse(" ".join(tweet_tokens[1:]))

totalTweets = len(tweets)

tweets = []
test = open(testFile, 'r')
for line in test:
	line = line.lower()
	tweets.append(line)

correctCount = 0
output = open(outFile, "w+")
for tweet in tweets:
	tweet_tokens = tweet.split(" ")
	tweetLocation = tweet_tokens[0]
	testLocation = classify_tweet(" ".join(tweet_tokens))
	output.write(testLocation + ' ' + tweet)
	if testLocation == tweetLocation:
		correctCount += 1

for location in locations.keys():
	classifier = locations[location]
	locationTop5 = classifier.top_5_words()
	print(location + ": " + str(locationTop5))

print("Accuracy: " + str(correctCount * 100.0 / len(tweets)))