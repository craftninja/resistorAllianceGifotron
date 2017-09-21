import twitter
from keys_twitter import *

api = twitter.Api(
    consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token_key = token_key,
    access_token_secret = token_secret
)

api.PostMedia(
    'testing Gifotron',
    'images/test.jpg'
)
