# README

### Stuff you need

1. Raspberry Pi - we are using the RPi 3 Model B
1. Raspberry Pi Camera - we are using Camera Module V2
1. Breadboard and breadboard wires to prototype connections
1. LEDs for lighting up your beautiful face - we will be using 24x 10mm white leds in a ring ~14" across
    * We prototyped with one LED
1. [Arcade Button with LED](https://www.adafruit.com/product/3490)
1. Optional assembly:
    * laser cut the file in [svgs_for_housing](./svgs_for_housing)
      * If I were to cut this out again, I would move the large button cutout up about an inch to allow the RPi to rest on the 2x4 (5" cut)
    * cut a 2x4 to 5" and drill holes all the way through the same distance apart as the two holes below the button hole
    * one threaded insert to mount 2x4 piece onto a tripod, 1/4"-20 Internal Threads
    * 2 bolts, nuts, and 4 washers to bolt the 2x4 piece to the back piece
    * 4 bolts, nuts and spacers for the 4 holes binding the two pieces together

### Setup:

1. copy `keys_tumblr_example.py` to `keys_tumblr_.py`
1. copy `keys_twitter_example.py` to `keys_twitter.py`
1. log into a tumbler account and get the required keys listed in the example file
1. log into a twitter account and get the required keys listed in the example file
1. install necessary python libs

    ```
    sudo apt-get update
    sudo apt-get install imagemagick
    sudo apt-get install mpg321 -y
    sudo apt-get install python-RPi.gpio python3-RPi.gpio
    sudo pip install pytumblr
    sudo pip install python-twitter
    ```

1. testing stuff
  1. test camera:
      * gently and firmly push the camera cable into the camera slot on the RPi board (blue side towards audio out port)
      * `python testFiles/camera.py`
  1. test tumblr integration:
      * the module with the tumblr keys and the test file using those keys need to be in the same directory 😔 so:
      * move the test file to root and `python testTumblr.py`
      * and move it back to declutter root 🤷🏽‍♀️
  1. test twitter integration:
      * the module with the twitter keys and the test file using those keys need to be in the same directory 😔 so:
      * move the test file to root and `python testTwitter.py`
      * and move it back to declutter root 🤷🏽‍♀️
1. connect hardware as follows:
    * button switch - one lead to 3.3 volts, one lead to GPIO 18
    * button led - ground lead to ground, positive lead to resistor to GPIO 17
    * lightRing (to be constructed, right now one led) - cathode to ground, anode to resistor to GPIO 27

### How can I modify this?

1. You can use both Twitter and Tumblr integration, or just one of them. Or you can use no social media integration, and grab that animation.gif after each "session"
1. Add a scary, or magical, or themed photo to your gif! The photo should be 640x480 (default size in app), stored in the `images` folder, and be named `images*.jpg`. Remember that the session will create images named `image1.jpg` to `image6.jpg` (default 6 images in app), so don't name it something that will be overwritten!
1. Change the length of time for each photo in the gif
1. Change the number of photos taken for the gif
1. Change the sounds for the camera click and the uploaded notification sound


### Created by the amazing team of:
  * Amy Bertken
  * Emily Platzer
  * Nathan Jantz
