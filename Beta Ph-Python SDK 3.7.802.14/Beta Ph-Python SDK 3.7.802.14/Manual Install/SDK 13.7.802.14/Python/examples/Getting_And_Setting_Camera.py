'''Connecting to a camera, and then getting and setting the most obvious features, like partition count, resolution, frame rate, exposure, etc.'''

from pyphantom import Phantom, phantom, utils, cine 
from Camera_Selector_Fn import camera_selector
#camera selector function
ph = Phantom()
ph.add_simulated_camera()                                           #add simulated camera to pool
cam = ph.Camera(ph.camera_count-1)                                  #connecting to that simulated camera
#cam = camera_selector(ph)                                          #can use this function instead to connect to specific camera if you have multiple connected
#get and set some basic settings
def getting_and_setting_test(cam):
    cam.partition_count = 1                                         #partition count set
    cam.resolution = (9999, 9999)                                   #resolution set
    cam.frame_rate = 100                                            #frame rate set
    cam.exposure = 100                                              #exposure set
    cam.edr_exposure = 0                                            #edr exposure set
    cam.quiet = 0                                                   #quiet mode set (1 = quiet mode on)
    #cam.record(cine = 1, delete_all = False)                       #capture mode (parameters optional, defaults shown)                                                    

    print("%s partition(s)" % (cam.partition_count))                #partition count get
    print("%s fps" % (cam.frame_rate))                              #frame rate get    
    print(cam.resolution)                                           #resolution get
    print("Exposure is %s" % (cam.exposure))                        #exposure get
    print("Edr exposure is %s" % (cam.edr_exposure))                #edr exposure get
    print(cam.quiet)                                                #quiet mode get (True = quiet)
getting_and_setting_test(cam)
cam.clear_ram()                                                     #clear camera ram
cam.close()                                                         #unregister camera object
ph.close()                                                          #unregister phantom() object