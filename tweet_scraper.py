import tweepy
import csv
import re



# Get the screen name from the user  from the user
def get_screen_name_from_user():
    screen_name = input('Enter screen name:\n')
    screen_name_string = screen_name.replace(' ', '+')
    return screen_name


# This is only run once so does not check for duplicates
def write_results_to_masterfile(result,screen_name):
    outfilename = 'Results/' + screen_name + '.txt' 
    if len(results) >= 1:
        for item in range(0, len(results)):
            # Find out what our file number should be
            file_num = item            
            outfile = open(outfilename, 'a', encoding='utf-8')
            outfile.write(results[item])
            outfile.write('\n')
            outfile.close()


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #Twitter API credentials

    keyFile = open('keys.txt', 'r')
    consumer_key = keyFile.readline().rstrip()
    consumer_secret = keyFile.readline().rstrip()
    access_key = keyFile.readline().rstrip()
    access_secret = keyFile.readline().rstrip()

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)
    print(alltweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    
    while len(new_tweets) > 0:
        #print('getting tweets before %s') % str(oldest)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        #print("...%s tweets downloaded so far")% (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [tweet.text for tweet in alltweets]
    tweets = [re.sub('http.*','', x) for x in outtweets]
    tweets = [re.sub('\@.*','', x) for x in tweets]


    #write the csv  
    for x in tweets:
        if len(x) >= 5:
            print(x)
            outfile = open('Results/' + screen_name + '.txt', 'a', encoding='utf-8')
            outfile.write(x)
            outfile.write('\n')
            outfile.close()

    

def command_line_scrape():
    screen_name = get_screen_name_from_user()
    get_all_tweets(screen_name)

if __name__ == '__main__':
    #pass in the username of the account you want to download
    command_line_scrape()