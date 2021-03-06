from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()
camera.rotation = 180
camera.resolution = (800, 800)

ffmpeg_command = "ffmpeg -framerate 3 -f image2 -i /home/pi/Desktop/kuwic-expo-photobooth/tmp/image%03d.jpg /home/pi/Desktop/kuwic-expo-photobooth/dest/$(date +\"%Y_%m_%d_%I_%M_%p\")_KUWIC_PhotoBooth.gif"
clear_dir_command = "rm -r /home/pi/Desktop/kuwic-expo-photobooth/tmp/*"

    
def countdown():
    print("1...")
    sleep(1)
    print("2...")
    sleep(1)
    print("pose!")
    sleep(1)

try:
    camera.start_preview()
    
    # Camera will capture 4 photos
    for x in range(1,5):
        countdown()
        camera.capture('/home/pi/Desktop/kuwic-expo-photobooth/tmp/image%03d.jpg' % x)
        print("Captured photo " + str(x) + "\n\n")

    camera.stop_preview()

    # Compile everything currently in tmp into a gif in a destination directory
    # New gif filename will start with the exact time the gif was compiled
    subprocess.call(ffmpeg_command, shell=True)

    # Remove the photos in tmp for the next run
    #subprocess.call(clear_dir_command, shell=True)
    
except KeyboardInterrupt:
    camera.stop_preview()

    # Remove the photos in tmp
    # Note to self - should the terminal ask the user if they want this?
    subprocess.call(clear_dir_command, shell=True)
    

