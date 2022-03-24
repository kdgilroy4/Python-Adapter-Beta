'''This demonstrates how we get metadata from a cine using the cine get properties, also included is a function that is currently not yet in the sdk 
to help get human readable timestamps. '''

import pandas as pd
from pyphantom import Phantom, cine, utils
import time
import numpy as np
from Camera_Selector_Fn import camera_selector
ph = Phantom()
cam = camera_selector(ph)

#making sample recording to save and then look at
def make_simple_test_recording(cam):    
    cam.record()
    time.sleep(.2)
    cam.trigger()
    time.sleep(1)
    return cam

#get cine metadata using gets and sets
def show_cine_metadata(cine):
    print(cine.resolution)                                                        #cine resolution
    print("%s post trigger frames" % (cine.post_trigger_frames))                  #cine post_trigger_frames
    print("%s frames per second" % (cine.frame_rate))                             #cine frame_rate
    print("%s exposure" % (cine.exposure))                                        #cine exposure
    print("%s edr exposure" % (cine.edr_exposure))                                #cine edr_exposure
    print("cine number %s" % (cine.cine_number))                                  #cine number    
    print(cine.range)                                                             #cine frame_range   
    #print(cine.get_timestamps(cine.range))                                       #gets camera internal timestamps, 19 digit number, nonstandard format (seconds since epoch * 2^32)       
    print("first frame at %s" % (pd.Timestamp(cine.get_timestamps(cine.range)[0]/2**32, unit = 's')))  #timestamp first frame (uses pandas library Timestamp function)
    print("last frame at %s" %  (pd.Timestamp(cine.get_timestamps(cine.range)[1]/2**32, unit = 's')))  #timestamp last frame 

    #function to get the human readable timestamp of a given frame
    def Get_Human_Readable_Timestamp(n):                    
        return pd.Timestamp(n/2**32, unit = 's')                                  #note that the cine builtin timestamp is 2^32 times the seconds since the epoch (with more digits)
    x = map(Get_Human_Readable_Timestamp, (cine.get_timestamps(cine.range)))      #every frame made human readable and put into a list
    #print(list(x))                                                               #print human readable timestamp list (spammy)       
show_cine_metadata(make_simple_test_recording(cam).Cine(1))                       #note that I'm just taking .Cine(1) here, the first one on the camera's ram, but this would work from a cine file as well
cam.clear_ram()                                                                   #clear camera ram  
cam.close()                                                                       #unregister camera object
ph.close()                                                                        #unregister phantom() object