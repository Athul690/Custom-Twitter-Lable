#The name shown on lable on the tweet will be the name you given to the application when you added new project to the twitter development console
#you need to install tweepy before you run this program you can do it buy running 'sudo apt install tweepy'
#This is my first program i made and is far from perfect

import tweepy

consumer_key="CONSUMER KEY HERE"
consumer_secret_key ="CONSUMER KEY SECRET HERE"
access_token="ACCESS TOKEN CODE HERE"
secret_access_token="SECRET ACCESS TOKEN CODE HERE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)

auth.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth)

def simple_tweet() :
    print ('Enter Your Tweet')
    tweet = input(">>>> ")
    api.update_status(status =(tweet))
    
def media_tweet() :
    print ('Enter Your Tweet')
    tweet = input(">>>>")
    print ('Enter media location')
    media_location = input ('>>>>') 
    image = media_location
    api.update_with_media(image, tweet)
def reply_tweet() :
    print ('Enter Your Tweet')
    tweet = input(">>>>")
    print ('Enter Tweet ID')
    tweet_id = input ('>>>>')
    api.update_status(tweet, in_reply_to_status_id = tweet_id)

print ('Select Tweet Type')
print ('1 = Text Only\n2 = Text and Media \n3 = Reply')
tweet_type = input ('>>>>')
if tweet_type=='1':
    simple_tweet()
elif tweet_type =='2':
    media_tweet()
elif tweet_type =='3':
    reply_tweet()
else :
    exit
    
print ("Done!")
