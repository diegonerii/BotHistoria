import os
import tweepy
from dotenv import load_dotenv

class Tweets:
  """
    This class will get key values from twitter developer (https://developer.twitter.com/) 
    and will call a method which shows the user who tweeted: "a história vai cobrar". After that, the method
    "__tweeting", using self.api.update_status, will answer with the follow phrase: 
    " A história não cobra nada! Ustra morreu de velho."

    Tokens will not show for security reasons.

    ...
    Methods
    -------
    No methods available.
  """
  
  def __init__(self, searching_phrase: str, tweets_count: int):
    
    load_dotenv()
    
    consumer_key = os.getenv('consumer_key')
    consumer_secret_key = os.getenv('consumer_secret_key')
    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    # consumer_key, consumer_secret
    # Auth step. You can take both keys in https://developer.twitter.com/, "API Key" e "API Key Secret"

    auth.set_access_token(access_token, access_token_secret)
    #key, secret

    self.api = tweepy.API(auth, wait_on_rate_limit=True)
    # This line will be executed after tweet limit is reached

    self.searching_phrase = searching_phrase
    self.tweets_count = tweets_count

    self.__tweeting()

  def __tweeting(self):
    for tweet in tweepy.Cursor(self.api.search_tweets, self.searching_phrase).items(self.tweets_count):
      try:
        print("Username: @", tweet.user.screen_name)
        self.api.update_status(
          status='@' + tweet.user.screen_name + " A história não cobra nada! Ustra morreu de velho."
        )
        print('Tweet was sent')
      except tweepy.TweepError as error:
        print(error.reason)
      except StopIteration:
        break

if __name__ == '__main__':
  Tweets('A história vai cobrar', 1)
