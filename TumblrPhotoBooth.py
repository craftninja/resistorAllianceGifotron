#import modules
import RPi.GPIO as GPIO
from time import sleep
import os
import picamera
import pytumblr
from fractions import Fraction
from tumblr_keys import *

#create variables to hold commands
makeVid = "convert -delay 50 images/image*.jpg images/animation.gif"
meow2 = "mpg321 sounds/meow2.mp3"
cameraClick = "mpg321 sounds/camera-shutter-click-01.mp3"

#create variables to hold pin numbers
buttonLight = 17
lightRing = 27
button = 18

# AuthenticateS via OAuth, copy from https://api.tumblr.com/console/calls/user/info
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_token,
    token_key,
    token_secret
)

#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonLight, GPIO.OUT)
GPIO.setup(lightRing, GPIO.OUT)

camera = picamera.PiCamera() #initiate picamera module and class
camera.resolution = (640, 480) #set resolution of picture here
camera.brightness = 60 #set brightness settings to help with dark photos
camera.annotate_foreground = picamera.Color(y=0.2, u=0, v=0) #set color of annotation


try:
    #read button
    while True:
        input_state = GPIO.input(button)
        if input_state == True:
            print('Button Pressed')
            GPIO.output(buttonLight, True)
            sleep(0.5)
            GPIO.output(buttonLight, False)
            sleep(0.2)
            #if pressed blink button LED at two speeds
            for i in range(3):
                GPIO.output(buttonLight, True)
                sleep(1)
                GPIO.output(buttonLight, False)
                sleep(1)
            for i in range(3):
                GPIO.output(buttonLight, True)
                sleep(.25)
                GPIO.output(buttonLight, False)
                sleep(.25)

            #start camera preview
            camera.start_preview()

            #display text over preview screen
            GPIO.output(lightRing, True)
            camera.annotate_text = 'Get Ready!'
            camera.annotate_text = ''
            #take 6 photos
            for i, filename in enumerate(camera.capture_continuous('images/image{counter:02d}.jpg')):
                os.system(cameraClick)
                if i == 5:
                    break
                sleep(2)
            camera.stop_preview() #stop preview
            GPIO.output(lightRing, False)
            os.system(makeVid) #send command to convert images to GIF
            print('uploading') #let us know photo is about to start uploading

            #upload photo to Tumblr
            client.create_photo(
		'ResistorAlliance',	#update to your username
		state="published",
		tags=["ResistorAlliance", "gifotron"],
		data="images/animation.gif")
            print("uploaded") #let us know GIF has been uploaded
            #turn on uploaded LED and play meow samples
            GPIO.output(lightRing, True)
            sleep(0.2)
            GPIO.output(lightRing, False)
            os.system(meow2)
            os.system(meow2)

    GPIO.cleanup() #cleanup GPIO channels

#hit Ctrl + C to stop program
except KeyboardInterrupt:
    print ('program stopped')
