#How to look at the specific pixel values from a cine

from pyphantom import Phantom, utils, cine
from Camera_Selector_Fn import camera_selector
import time
import numpy as np
ph = Phantom()
#adding simulated cameras to fake record with
ph.add_simulated_camera(sensor_type=utils.SensorTypeEnum.COLOR)                     #color sim camera      
cam_Color = ph.Camera(ph.camera_count-1)

ph.add_simulated_camera(sensor_type=utils.SensorTypeEnum.MONO)                      #mono sim camera
cam_Mono = ph.Camera(ph.camera_count-1) 

def make_simple_test_recording(cam1):                                               #extremely simple test recording function
    cam1.resolution = (1024, 128)                                                   #set resolution so that we can cross reference later with array lengths
    cam1.record()
    time.sleep(.2)                                                                  #record for .2 seconds
    cam1.trigger()
    time.sleep(1)                       
    return cam1

make_simple_test_recording(cam_Color)
make_simple_test_recording(cam_Mono)

c1_Color = cam_Color.Cine(1)                                                        #get the cine we just recorded 

test_range = utils.FrameRange(c1_Color.range.last_image-100, c1_Color.range.last_image-100)  #set range, utils.FrameRange(int, int), this is how we create a FrameRange
image1 = c1_Color.get_images(test_range)                                            #get_images(Framerange), returns 4d array for color or 3d array for monochrome
print("%s color images" % (len(image1)))                                            #number of images
print("color image height is %s" % (len(image1[0])))                                #image height
print("color image width is %s" % (len(image1[0][0])))                              #image width
print("here are the rgb values of a particular pixel: %s" % (image1[0][10][0]))     #rgb pixel values, chose 10 arbitrarily so that pixel values aren't 0
image1[0][10][0][0] += 1                                                            #changing red value by one for demonstration
print("here is that same pixel with its red value incremented: %s" % (image1[0][10][0]))



#Doing the exact same thing as above except in monochrome, only difference being 3d array instead of 4d since only 1 value to record per pixel
c1_Mono  = cam_Mono.Cine(1)

test_range2 = utils.FrameRange(c1_Mono.range.last_image-100, c1_Mono.range.last_image-100)  #set range
image2 = c1_Mono.get_images(test_range2)                                            #get_images(Framerange), returns 4d array for color or 3d array for monochrome
print("mono image height is %s" % (len(image2[0])))                                 #image height
print("mono image width is %s" % (len(image2[0][0])))                               #image width
print("here is the value of a specific pixel: %s" % (image2[0][10][0]))             #specific pixel value, chose 10 arbitrarily so that value would not be 0                                                                                  
image2[0][10][0] += 1                                                               #changing pixel value by one for demonstration
print("here is that same pixel incremented: %s" % (image2[0][10][0]))

#You can also do this exact same thing with a saved recording (this example assumes color images)

fn = ph.file_select_dialog()                                                        #open file select dialog to choose a cine
c1_Saved = cine.Cine.from_filepath(fn)                                              #access that file we just chose
test_range3 = utils.FrameRange(c1_Saved.range.last_image-1, c1_Saved.range.last_image)#set range, for some reason this was breaking at 4 or more frames passed in
image3 = c1_Saved.get_images(test_range3)                                           #get_images(Framerange), gives us a 4d array for color or 3d array for monochrome
print("color image height is %s" % (len(image3[0])))                                #image height
print("color image width is %s" % (len(image3[0][0])))                              #image width
print("here are the rgb values of a particular pixel: %s" % (image3[0][10][0]))     #rgb pixel values, chose 10 arbitrarily
image3[0][10][0][0] += 1                                                            #changing red value by one for demonstration
print("here is that same pixel with its red value incremented: %s" % (image3[0][10][0]))

cam_Color.close()                                                                   #unregister camera objects
cam_Mono.close()                                                                    
ph.close()                                                                          #unregister phantom() objects