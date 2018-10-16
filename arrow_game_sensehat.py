from sense_hat import SenseHat
import time
import random
sense=SenseHat()

r=(255,0,0)
y=(0,255,0)
b=(0,0,255)


while True:
  y=(0,255,0)
  
  rotation=random.randint(0,3)*90
  sense.set_rotation(rotation)
  image_pixels = [b, b, b, b, b, b, b, b,
                  b, b, b, y, b, b, b, b,
                  b, b, y, y, y, b, b, b,
                  b, y, b, y, b, y, b, b,
                  b, b, b, y, b, b, b, b,
                  b, b, b, y, b, b, b, b, 
                  b, b, b, y, b, b, b, b, 
                  b, b, b, b, b, b, b, b]
  sense.set_pixels(image_pixels)
   
  time.sleep(10)
  yaw = sense.get_orientation()['yaw'] 
  if rotation==0:
    if not 89<=yaw<=91:
      y=r
      
  if rotation==90:
    if not (0<=yaw<=1 or 359<=yaw<=360):
      y=r
      
  if rotation==180:
    if not 269<=yaw<=271:
      y=r
      
    
  if rotation==270:
    if not 179<=yaw<=181:
      y=r
  if y==r:
    image_pixels = [b, b, b, b, b, b, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, y, y, y, b, b, b,
                    b, y, b, y, b, y, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, b, y, b, b, b, b, 
                    b, b, b, y, b, b, b, b, 
                    b, b, b, b, b, b, b, b]
    sense.set_pixels(image_pixels)
    break
  
