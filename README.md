## Twitter Scraper

This is a scraper for the most recent 3240 from a single twitter user. 


## Setup

First install the requirements.
```pip install -r requirements.txt```
(In this case it's just tweepy, but more things might happen down the line...)

Next, you have to set up your consumer key, consumer secret, access key and access secret. 
To get the consumer key and consumer secret, register a client application with Twitter [here.](https://apps.twitter.com/)

Then for the access key/secret, follow [these instructions.](http://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html)

When you're all done with that, open up that keys.txt file and put those codes in where the text tells you to. 


## Use

Just run tweet_scraper.py. You'll be prompted for the username you want to use and the results will be saved in the Results folder! (I left dog_rates.txt in there for fun...)