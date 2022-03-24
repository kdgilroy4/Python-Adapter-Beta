#This should show a live image for a connected camera, or a simulated camera if none connected


import keyboard  #pip install keyboard if necessary
from pyphantom import Phantom, cine, utils
import cv2   #pip install opencv-python if necessary
from Camera_Selector_Fn import camera_selector
ph = Phantom()
cam = camera_selector(ph)                                   #nice function that will make a simulated camera or if you have cameras connected let you choose which to connect to
def see_live_image(cam):
    while(True):
        img = cam.get_live_image()                          #builtin function that gets a live image
        if bool(cam._live_cine.is_color.value):             #convert to color if live cine is color
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)          
        cv2.imshow('live', img)                             #use cv2 library to show the image you saved
        cv2.waitKey(100)                                    #wait 100 ms between loops (this means that we update the live image every 100ms)     
        if keyboard.is_pressed('space') or keyboard.is_pressed('esc') or keyboard.is_pressed('enter'):    #close window and break out of loop by pressing space, esc, or enter 
            cv2.destroyAllWindows
            break

see_live_image(cam) ####NOTE IF YOU CLOSE THE IMAGE TAB BY CLICKING THE X INSTEAD OF SPACE/ESC/ENTER, IT CRASHES AND YOU HAVE TO RESTART THE TERMINAL

cam.close()                                                 #unregister camera object
ph.close()                                                  #unregister phantom() object