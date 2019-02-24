from picamera import PiCamera

camera = PiCamera()
camera.rotation = 180
camera.resolution = (800, 800)

try:
    camera.start_preview()

    
except KeyboardInterrupt:
    camera.stop_preview()
