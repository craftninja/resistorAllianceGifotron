# README

### Setup:

1. copy `tumblr_keys_example.py` to `tumblr_keys.py`
1. log into a tumbler account and get the required keys listed in the example file
1. install necessary python libs

  ```
  sudo apt-get update
  sudo apt-get install imagemagick
  sudo apt-get install mpg321 -y
  sudo apt-get install python-RPi.gpio python3-RPi.gpio
  sudo pip install pytumblr
  ```

1. testing stuff
  1. test camera:
    * gently and firmly push the camera cable into the camera slot on the RPi board (blue side towards audio out port)
    * `python testFiles/camera.py`
  1. test tumblr integration:
    * the module with the tumblr keys and the test file using those keys need to be in the same directory 😔 so:
    * move the test file to root and `python testPyTumblr.py`
    * and move it back to declutter root 🤷🏽‍♀️
1. connect hardware as follows:
  * button switch - one lead to ground, one lead to GPIO 18
  * button led - ground lead to ground, positive lead to resistor to GPIO 17
  * lightRing (to be constructed, right now one led) - cathode to ground, anode to resistor to GPIO 27

### How did this get made?

1. Followed instructions in instructables to setup pi and create a Tumbler API client with some edits
  * [Raspberry Pi Tumblr Gif Photo Booth](http://www.instructables.com/id/Raspberry-Pi-Tumblr-GIF-Photo-Booth/)


### Created by the amazing team of:
  * Amy Bertken
  * Emily Platzer
  * Nathan Jantz
