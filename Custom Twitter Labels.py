import tweepy

auth = tweepy.OAuthHandler("CONSUMER KEY HERE", "CONSUMER KEY SECRET HERE")

auth.set_access_token("ACCESS TOKEN HERE", "ACCESS TOKEN SECRET HERE")

api = tweepy.API(auth)

def simple_tweet :
    print ('Enter Your Tweet')
    tweet = input(">>>> ")
    api.update_status(status =(tweet))
    
def media_tweet :
    print ('Enter Your Tweet')
    tweet = input(">>>>")
    print ('Enter media location')
    media_location = input ('>>>>') 
    image = media_location
    api.update_with_media(image, tweet)
def reply_tweet :
    print ('Enter Your Tweet')
    tweet = input(">>>>")
    print ('Enter Tweet ID')
    tweet_id = input ('>>>>')
    api.update_status(tweet, in_reply_to_status_id = tweet_id)


print ("Done!")
