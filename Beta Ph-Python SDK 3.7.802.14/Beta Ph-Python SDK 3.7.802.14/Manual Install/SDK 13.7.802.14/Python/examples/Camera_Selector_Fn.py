from pyphantom import Phantom, utils
'''this is a function that will return a camera object in any case of cameras connected
in the case that there are no cameras connected, it will create a simulated camera and connect to it and return that object
in the case that there is 1 camera connected, it will connect to that camera and return that object
in the case that there are 2 or more cameras connected, it will iterate through each camera to ask which one you want to connect to and return the object of'''
def camera_selector(ph):   #ph is a Phantom() object
    cam_count = ph.camera_count
    if cam_count == 0:                    #case no camera is connected, makes simulated camera
        print("No cameras connected, making simulated camera")
        ph.add_simulated_camera()
        cam = ph.Camera(0)
    elif cam_count == 1:                  #case exactly 1 camera is connected, just connects
        print("Connected to only connected camera")
        cam = ph.Camera(0)
    else:                                 #case more than 1 camera is connected, walks through the connected cameras and prompts you to choose the one to connect to                                      
        for i in range(cam_count):
            cam_model = ph.discover()[i][2]    #ph.discover()[i][name, serial number, model, camera number]
            cam_sn = ph.discover()[i][1]
            use_cam = input("Camera %s is a %s with serial number %s, is this the camera you would like to use? y or n? \n" % (i, cam_model, cam_sn))
            try: 
                if use_cam == "y":
                    cam = ph.Camera(i)
                    break
            except: 
                print("That's not a legal input")
    try: 
        cam.get_partition_state(0)          #just testing something innocuous to see if camera selected, if something more innocuous can be used here, should do that
    except:
        print("No camera selected")
    return cam