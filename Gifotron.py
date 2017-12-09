#import modules
import RPi.GPIO as GPIO
from time import sleep
import os
import picamera
import pytumblr
import twitter
from fractions import Fraction
from keys_tumblr import *
from keys_twitter import *

#create variables to hold commands
makeVid = "convert -delay 50 images/image*.jpg images/animation.gif"
meow2 = "mpg321 sounds/meow2.mp3"
cameraClick = "mpg321 sounds/camera-shutter-click-01.mp3"

#create variables to hold pin numbers
buttonLight = 17
lightRing = 27
buttonSwitch = 18

# AuthenticateS via OAuth, copy from https://api.tumblr.com/console/calls/user/info
tumblr = pytumblr.TumblrRestClient(
    tum_consumer_key,
    tum_consumer_token,
    tum_token_key,
    tum_token_secret
)

twit = twitter.Api(
    consumer_key = twit_consumer_key,
    consumer_secret = twit_consumer_secret,
    access_token_key = twit_token_key,
    access_token_secret = twit_token_secret
)

#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonLight, GPIO.OUT)
GPIO.setup(lightRing, GPIO.OUT)

camera = picamera.PiCamera() #initiate picamera module and class
camera.resolution = (640, 480) #set resolution of picture here
camera.brightness = 60 #set brightness settings to help with dark photos
camera.annotate_foreground = picamera.Color(y=0.2, u=0, v=0) #set color of annotation


try:
    #read button
    while True:
        input_state = GPIO.input(buttonSwitch)
        if input_state == True:
            print('Button Pressed')
            GPIO.output(buttonLight, True)
            sleep(0.5)
            GPIO.output(buttonLight, False)
            sleep(0.25)
            for i in range(3):
                GPIO.output(buttonLight, True)
                sleep(.25)
                GPIO.output(buttonLight, False)
                sleep(.25)

            #start camera preview
            camera.start_preview()

            GPIO.output(lightRing, True)
            sleep(2)
            #take 6 photos
            for i, filename in enumerate(camera.capture_continuous('images/image{counter:02d}.jpg')):
                os.system(cameraClick)
                GPIO.output(lightRing, False)
                if i == 5:
                    break
                sleep(.25)
                GPIO.output(lightRing, True)
                sleep(.75)
            camera.stop_preview() #stop preview
            GPIO.output(lightRing, False)
            os.system(makeVid) #send command to convert images to GIF
            print('uploading') #let us know photo is about to start uploading

            #upload photo to Tumblr

            tumblr.create_photo(
                tum_user_name,
                state="published",
                tags=["ResistorAlliance", "gifotron", "testing"],
                data="images/animation.gif"
            )
            twit.PostMedia(
                '#ResistorAlliance #gifotron  #testing',
                'images/animation.gif'
            )

            print("uploaded") #let us know GIF has been uploaded

            #turn on uploaded LED and play meow samples
            GPIO.output(lightRing, True)
            sleep(0.2)
            GPIO.output(lightRing, False)
            os.system(meow2)

#hit Ctrl + C to stop program
except KeyboardInterrupt:
    GPIO.cleanup() #cleanup GPIO channels
    print ('program stopped')
