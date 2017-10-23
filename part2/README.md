## Design Decisions:

We are removing lists of the below

- punctuations & numbers - ~`1234567890!@$#$%^&*()_+|}{:"?><,./;'[]\
- nltk stop words used from reference https://gist.github.com/sebleier/554280 & https://piazza.com/class/j6lbw30o3z35cw?cid=233

We have tried stemming er, ing, e, ed and s but it did not improve the accruacy so we have excluded the code.

The probability approach that we have used is from reference - https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/

We have also discussed this strategy with sahk-skpanick-cgalani group.

To calculate the probability:

We have used laplace smooting - added 1 to the total word count.

To calculate the probability of the 

- word given location: divided the word count by the total frequency of words in all tweet per location.

- location: divided number of tweets from the particular location to the total number of tweets.

- location given word: multiplied the probability of word given location by location
