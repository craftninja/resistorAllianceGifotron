import twitter
from keys_twitter import *

twit = twitter.Api(
    consumer_key = twit_consumer_key,
    consumer_secret = twit_consumer_secret,
    access_token_key = twit_token_key,
    access_token_secret = twit_token_secret
)

try:
    twit.PostMedia(
        'testing Gifotron',
        'images/test.jpg'
    )
    print("uploaded")
except Exception as e:
    print(e)
