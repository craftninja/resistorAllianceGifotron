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
        tags=["test", "ResistorAlliance", "gifotron"],
        data="images/test.jpg"
    )
    # print(client.info()) # uncomment for more details on tumblr fails
    print("uploaded")
except Exception as e:
    print(e)
