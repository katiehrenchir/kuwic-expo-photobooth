from picamera import PiCamera
from PIL import Image, ImageDraw, ImageFont
from time import sleep
import subprocess

camera = PiCamera()
camera.rotation = 180
camera.resolution = (800, 800)

camera.start_preview()
    


