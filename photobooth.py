from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()
camera.rotation = 180
camera.resolution = (600, 600)

camera.start_preview()

while True:
    try:
        # Countdown process
        for x in range(1,4):
            camera.capture('/home/pi/Desktop/PhotoBooth/tmp/image%03d.jpg' % x)
            # Add display of previous image (image00(x-1))
            # Sleep 3 ish seconds - display countdown, or too busy?

        # Compile everything currently in tmp into a gif in a destination directory
        # New gif filename will start with the exact time the gif was compiled
        subprocess.run("ffmpeg -framerate 5 -f image2 -i /home/pi/Desktop/PhotoBooth/tmp/image%03d.jpg ../dest/$(date +\"%Y_%m_%d_%I_%M_%p\")_KUWIC_PhotoBooth.gif")

        # Remove the photos in tmp for the next run
        subprocess.run("rm -r /home/pi/Desktop/PhotoBooth/tmp/*")
        
    except KeyboardInterrupt:
        camera.stop_preview()

        # Remove the photos in tmp
        # Note to self - should the terminal ask the user if they want this?
        subprocess.run("rm -r /home/pi/Desktop/PhotoBooth/tmp/*")
        break
