import pytumblr
from keys_tumblr import *

client = pytumblr.TumblrRestClient(
    tum_consumer_key,
    tum_consumer_token,
    tum_token_key,
    tum_token_secret
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
