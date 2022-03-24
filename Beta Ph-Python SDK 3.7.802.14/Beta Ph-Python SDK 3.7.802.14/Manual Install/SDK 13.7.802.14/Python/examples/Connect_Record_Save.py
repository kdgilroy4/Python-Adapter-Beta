'''A very straightforward file, demonstrating how to simply connect to a camera, record with it, and then the different ways to save what you recorded'''


from pyphantom import Phantom, utils, cine
from Camera_Selector_Fn import camera_selector
import time
import numpy as np
import os

#CONNECT
ph = Phantom()
ph.add_simulated_camera()                           #adding simulated camera to queue
#ph.discover(print_list=True)                       #in case you want to know which camera to connect to
cam = ph.Camera(0)                                  #setting cam to a camera object, the nth (indexed by 0) camera connected, if none connected it will connect to sim camera we just added

#RECORD
cam.resolution = (1024, 128)                        #setting resolution
cam.frame_rate = 100                                #setting framerate
cam.post_trigger_frames = 0                         #setting post trigger frames
cam.partition_count = 1                             #setting partition count 
cam.record()                                        #start recording
time.sleep(.2)                                      #wait recording time
cam.trigger()                                       #trigger 

#SAVE
cine1 = cam.Cine(1)                                 #make cine object for cine in ram we just recorded
cine1.save_nvm()                                    #save from camera RAM to camera NonVolatileMemory
cine1.save_dialog()                                 #save cine using the save dialog window

#SAVE ALTERNATES
#Instead of using the save_dialog, we can use cine1.save() and give the path, format, and range we want to save.
cine1.save_name = os.path.expanduser('~')+'\Desktop\Test1\TestFile'                     #set cine save name (in this case saved to a folder on your desktop named Test1 as "TestFile") 
cine1.save_type = utils.FileTypeEnum(0)                                                 #set save type (see utils.FileTypeEnum to see possible saving formats, in this case its a cineraw)
cine1.save_range = utils.FrameRange(cine1.range.last_image-99, cine1.range.last_image)  #set save range, use utils.FrameRange(int, int) to set a range, (in this case its the last 100 frames)
#note that if you save the filepath as an extension, like TestFile.cine, it will override the save_type value. 
#If you save only a filename, and not a full path, it will save it to your console's local directory
cine1.save()                                        #use normal save with the specified name, type, and range.

#These values can also be set within the save() function as parameters 
cine1.save(filename = os.path.expanduser('~')+'\Desktop\Test1\TestFile', format = utils.FileTypeEnum(0), range = utils.FrameRange(cine1.range.last_image-99, cine1.range.last_image)) 
cine1.save_non_blocking()                           #can also save non blocking to save but return control to the caller immediately, doing save in a separate thread

cam.close()                                         #unregister camera object
ph.close()                                          #unregister phantom() object