import pytumblr
from tumblr_keys import *

client = pytumblr.TumblrRestClient(
  consumer_key,
  consumer_token,
  token_key,
  token_secret
)

try:
  client.create_photo(
  'ResistorAlliance',
  state="published",
  tags=["raspberrypi", "picamera"],
  data="images/image01.jpg"
  )
  print(client.info())
  print("uploaded")
except Exception as e:
  print(e)
