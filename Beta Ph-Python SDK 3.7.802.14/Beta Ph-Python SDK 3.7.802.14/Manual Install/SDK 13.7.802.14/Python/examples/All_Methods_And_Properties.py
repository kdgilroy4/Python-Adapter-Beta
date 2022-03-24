'''This is a big repository of all of the different public facing methods and properties  available through the phantom python SDK'''


from pyphantom import Phantom, cine, utils

#create Phantom() object. Note there can only be 1 of these
ph = Phantom()                             

#Phantom() properties
en_log = ph.enable_log                #check if log is enabled (1 = enabled)
#Write a log file to help the debugging of issues by the support people from Vision Research Inc. Default file path is C:\ProgramData\Phantom\<SDK version>\PhCon.log
ph.enable_log = 1/0                   #enable log, (1 = enabled)
log2ram = ph.log_to_ram               #check if logging to ram is enabled (1 = enabled)
#To accelerate running the applications with logging enabled you can choose to write the log information in a RAM buffer (lose data on camera crash though)                                                             
ph.log_to_ram = 1/0                   #enable logging to ram (1 = enabled)            
cam_count = ph.camera_count           #number of cameras connected

#Phantom() methods
ph.add_simulated_camera(cameraVersion=7011, sensor_type=utils.SensorTypeEnum.COLOR) 
"""Adds a simulated phantom camera
    Parameters
        cameraVersion : sim camera version number
            default 7011, or VEO 640S
        sensor_type : SensorTypeEnum.MONO or COLOR
            default COLOR
"""      
ph.simulated_camera_dialog()
"""Allow adding simulated cameras and make them persistent over the restart of application
"""
fn = ph.file_select_dialog()                            
"""Display a dialog box to select a cine file to open. If the dialog is terminated by Cancel the string returned will be void
    Returns
        filepath : string
        """
data = ph.discover(print_list = False)                  
"""get the list of all Phantom cameras connected to this computer
    Return
        List of Discovery NamedTuple containing info of available cameras
"""
cam = ph.Camera(cam_count)
"""Instantiate Camera object
    Parameters
        camera_number: int
    Returns
        Camera object
"""
ph.time64_to_string(time64)
"""Utility to convert the image time from the numpy arrays returned by AuxData_np  to a printable string
    Parameters
        time64 : uint64 datetime
    Returns
        datetime : string        
"""
ph.close()  
"""Call this when the execution of your application finishes.
"""

#camera properties that you can both get & set  
part_count = cam.partition_count                          #get partition count                          (returntype int)                      
cam.partition_count = int                                 #set partition count
resolution = cam.resolution                               #get resolution                               (returntype utils.Resolution)
cam.resolution = (int, int) or utils.Resolution           #set resolution
post_trigger_frames = cam.post_trigger_frames             #get post trigger frames                      (returntype int)
cam.post_trigger_frames = int                             #set post trigger frames
frame_rate = cam.frame_rate                               #get frame rate                               (returntype float)
cam.frame_rate = float                                    #set frame rate
exposure = cam.exposure                                   #get exposure                                 (returntype float)                 
cam.exposure = float                                      #set exposure
edr_exposure = cam.edr_exposure                           #get edr exposure                             (returntype float)                           
cam.edr_exposure = float                                  #set edr exposure
img_delay = cam.image_delay                               #get image delay                              (returntype float)                           
cam.image_delay = float                                   #set image delay
sync_mode = cam.sync_mode                                 #get sync mode                                (returntype str)                   
cam.sync_mode = utils.SyncModeEnum                        #set sync mode 
shutter_off = cam.shutter_off                             #get shutter off value                        (returntype bool)
cam.shutter_off = 1/0                                     #set shutter off value (1 = off)
auto_exposure = cam.auto_exposure                         #get auto exposure                            (returntype bool)                    
cam.auto_exposure = 1/0                                   #set auto exposure (1 = on)                    
auto_exposure_level = cam.auto_exposure_level             #get auto exposure level                      (returntype int)                    
cam.auto_exposure_level = int                             #set auto exposure level
cam_name = cam.name                                       #get cam name                                 (returntype str)                          
cam.name = str                                            #set cam name
nvm_auto_save_on = cam.nvm_auto_save                      #get nvm auto save on                         (returntype bool)                
cam.nvm_auto_save = 1/0                                   #set nvm auto save on (1 = on)
auto_csr_on = cam.auto_csr                                #get auto csr on                              (returntype bool)
cam.auto_csr = 1/0                                        #set auto csr on (1 = on)
quiet_mode = cam.quiet                                    #get quiet mode value                         (returntype bool)
cam.quiet = 1/0                                           #set quiet mode (1 = quiet)
enable_auto_trig = cam.enable_auto_trigger                #get auto_trigger                             (returntype bool)
cam.enable_auto_trigger = 1/0                             #set auto_trigger (1 = auto_trigger on)
data_size = cam.range_data_size                           #get range data size                          (returntype int)
cam.range_data_size = 0/16                                #set range data size
daq_digital_channel_count = cam.daq_digital_channel_count #get daq digital channel count                (returntype int)              
cam.daq_digital_channel_count = int                       #set daq digital channel count
daq_analog_channel_count = cam.daq_analog_channel_count   #get daq analog channel count                 (returntype int)
cam.daq_analog_channel_count = int                        #set daq analog channel count     
daq_samples_per_image = cam.daq_samples_per_image         #get daq samples per image                    (returntype int)
cam.daq_samples_per_image = int                           #set daq samples per image    
auto_trig_info = cam.auto_trig_info                       #get auto trigger info                        (returntype utils.AutoTrig)
cam.auto_trig_info = utils.AutoTrig                       #set auto trigger info

#camera get only properties
offline = cam.offline                                     #get whether camera offline                   (returntype bool)
active_partition = cam.active_partition                   #get active partition                         (returntype int 0 indexed)
active_partition_stored = cam.active_partition_stored     #get whether active partition stored          (returntype bool)
capacity = cam.partition_capacity                         #get get camera partition capactiy            (returntype int)
has_mechanical_shutter = cam.has_mechanical_shutter       #get whether camera has mechanical shutter    (returntype bool)
serial = cam.serial                                       #get camera serial number                     (returntype int)
hardware_version = cam.hardware_version                   #get camera hardware version                  (returntype int)
model = cam.model                                         #get camera model                             (returntype str)
nvm_cine_range = cam.nvm_cine_range                       #get cam nvm cine range                       (returntype (int, int))
nvm_size = cam.nvm_size                                   #get cam nvm size                             (returntype int)
nvm_free = cam.nvm_free                                   #get cam nvm free                             (returntype int)
nvm_available = cam.nvm_available                         #get whether cam nvm available                (returntype bool)
resolution_usual = cam.resolution_usual                   #get usual resolutions                        (returntype list of utils.Resolution)  
resolution_mmi = cam.resolution_mmi                       #get cam resolution mmi                       (returntype utils.MMI)
period_mmi = cam.period_mmi                               #get cam period mmi                           (returntype utils.MMI)
exposure_mmi = cam.exposure_mmi                           #get cam exposure mmi                         (returntype utils.MMI)
edr_exposure_mmi = cam.edr_exposure_mmi                   #get cam edr exposure mmi                     (returntype utils.MMI)
frame_rate_mmi = cam.frame_rate_mmi                       #get cam framerate mmi                        (returntype utils.MMI)
image_delay_mmi = cam.image_delay_mmi                     #get cam image delay mmi                      (returntype utils.MMI)

#camera public methods
cam.record(cine=1, delete_all=False)
"""Abort current recording and start a new recoding in partition specified.
    Parameters
        cine: int
            cine number, default 1
        delete_all: boolean
            delete all recordings before record, default False
"""
cam.trigger()
"""Send a software trigger. Camera will record PostTriggerFrames and will continue the recording in the next free partition.
"""
cam.delete(cine=1, nvm=False)
"""Delete the recording in the specified partition.
    If cine is in the range of the cines from NVM, the NVM will be fully erased. Warn user before such an operation.
    Parameters
        cine: int
            cine number, default 1
        nvm: boolean
            if true, cine number is in NVM range. if false, cine number is in RAM range.
"""
cam.clear_ram()
"""Delete all cines in camera memory
"""
cam.csr()
"""CurrentSessionReference for camera sensor calibration.
    May require manual cover of lens if the camera does not have mechanical shutter.
"""
cam.signal_setup_dialog()
"""Display a dialog to configure the range data and signal acquisition (AuxData)
"""
cam.Cine(1)
"""Instantiate Cine object using camera object's camera_number
    Parameters
        cine: int
            cine number, default 1

    Returns
        Cine object
"""
cam.partition_recorded(1)
""" Specified partition has a cine recorded.
    Returns
        Boolean
            True = recorded, False = not recorded
"""
cam.get_live_image()
"""get single live image from the camera
    Returns
        image data : numpy array
"""
cam.get_partition_state(1)
"""Gets the current state of the partition
    Parameters
        partition : int
            partition index, default = -1, get all partition state
    Returns
        Partition State : tuple (cine number, PartitionStateEnum)
            if -1, returns a list of tuples
"""
cam.close()

#cine object instantiation methods
cine1 = cine.Cine.from_camera(cam, cine_number)         #instantiate cine object from camera cine
cine2 = cine.Cine.from_filepath(filepath)               #instantiate cine object from filepath

#cine properties you can both get & set
description = cine1.description                         #get cine description                   (returntype str) 
cine1.description = str                                 #set cine description                   
bright = cine1.bright                                   #get cine brightness                    (returntype float)
cine1.bright = float                                    #set cine brightness, [-0.1, 0.1]
contrast = cine1.contrast                               #get cine constrast                     (returntype float)
cine1.contrast = float                                  #set cine contrast, [0.1, 10.0]
gamma = cine1.gamma                                     #get cine gamma                         (returntype float)
cine1.gamma = float                                     #set cine gamma, [0.1, 10.0]
white_balance = cine1.white_balance                     #get cine white balance                 (returntype utils.WhiteBalance)       
cine1.white_balance = (float, float)                    #set cine white balance
save_name = cine1.save_name                             #get cine save name                     (returntype str)
cine1.save_name = str                                   #set cine save name
save_range = cine1.save_range                           #get cine save range                    (returntype utils.FrameRange)            
cine1.save_range = utils.FrameRange                     #set cine save range        
save_type = cine1.save_type                             #get cine save type                     (returntype str)
cine1.save_type = utils.FileTypeEnum                    #set cine save type
progress_callback = cine1.progress_callback             #get cine progress callback             (returntype function?)
cine1.progress_callback = function#?                    #set cine progress callback

#cine get only properties
cine_number = cine1.cine_number                         #get cine number                        (returntype int)
resolution = cine1.resolution                           #get cine resolution                    (returntype utils.Resolution)         
post_trigger_frames = cine1.post_trigger_frames         #get cine post trigger frames           (returntype int)
frame_rate = cine1.frame_rate                           #get cine framerate                     (returntype float)           
exposure = cine1.exposure                               #get cine exposure                      (returntype float)          
edr_exposure = cine1.edr_exposure                       #get cine edr exposure                  (returntype float)
image_delay = cine1.image_delay                         #get cine image delay                   (returntype float)          
sync_mode = cine1.sync_mode                             #get cine sync mode value               (returntype str (utils.SyncModeEnum))              
shutter_off = cine1.shutter_off                         #get whether cine shutter off           (returntype bool)
auto_exposure = cine1.auto_exposure                     #get whether cine auto exposure on      (returntype bool)    
auto_exposure_level = cine1.auto_exposure_level         #get cine auto exposure level           (returntype int)
bits_per_pixel = cine1.bits_per_pixel                   #get cine bits per pixel                (returntype int)
is_color = cine1.is_color                               #get whether cine is color              (returntype utils.SensorTypeEnum)
black_white_levels = cine1.black_white_levels           #get cine white black levels            (returntype utils.BlackWhiteLevels)
recorded_range = cine1.recorded_range                   #get cine recorded range                (returntype utils.FrameRange)
cine_range = cine1.range                                #get cine range                         (returntype utils.FrameRange)
save_percentage = cine1.save_percentage                 #get cine save percentage               (returntype int)

#cine public methods
cine1.measure_white_balance(measure_wb_info) 
"""Camera measures white balance from a ROI of a set of live images. Requires gray surronding the ROI.
    Parameter
        measure_wb_info : NamedTuple MeasureWhiteBalance (x , y, frame_count)
    Returns
        NamedTuple WhiteBalance : the compensating White Balance gains for the red and blue colors
"""
cine1.get_images(framerange)
"""Get a range of images from cine as a numpy array of pixels – 3d for monochrome, 4d for color.
    Note: a request for too many frames may result in an exception, depending on system resources.
    Parameters
        framerange: NamedTuple FrameRange (first frame number, last frame number)
    Returns
        numpy array, 3d for monochrome, 4d for color.
"""
cine1.get_timestamps(framerange)
"""Get auxiliary time recorded with images at framerange
    Parameters
        framerange: NamedTuple FrameRange (first frame number, last frame number)
    Returns
        numpy array of idiosynchratic time64
"""
cine1.get_timestamps_readable(framerange)   #not implemented yet
cine1.get_exposures(framerange)
"""Get auxiliary exposure recorded with images at framerange
    Parameters
        framerange: NamedTuple FrameRange (first frame number, last frame number)
    Returns
        numpy array of exposures(us)
"""
cine1.get_digital_signals(framerange)
"""Get auxiliary digital(binary) signals recorded with images at framerange
    Parameters
        framerange: NamedTuple FrameRange (first frame number, last frame number)
    Returns
        numpy array of signals
"""
cine1.get_analog_signals(framerange)
"""Get auxiliary analog signals recorded with images at framerange
    Parameters
        framerange: NamedTuple FrameRange (first frame number, last frame number)    
    Returns
        numpy array of signals
"""
cine1.save(filename='', format='', range='')
"""Save cine from camera to file or convert a cine file to another format.
    Save options like file name, format, range have to be set in cine before this call.
    This call can update filename, format and/or range if defined.
    This call will return when save is complete.
    Parameter
        filename : string                   if empty, use current save_name value
        format : utils.FileTypeEnum         if empty, use current save_type value
        range : utils.FrameRange            if empty, use current save_range value
"""    
cine1.save_non_blocking()
"""Similar to Save but the control returns to caller immediately and the save operation is done in a separate thread.
"""        
cine1.save_nvm()
"""Save a cine recorded in the camera RAM memory to camera NonVolatileMemory.
"""
cine1.save_dialog()
""" Open from Phantom SDK the dialog box for setting the name of the file to save.
    If the dialog is terminated by Cancel function will return 0 and the application may skip the save operation.
    This call will return when save is complete.
    Returns
        Boolean
            OK was pressed = True, cancel = False
"""
cine1.close()
"""Close the cine, free the memory allocated for it in computer memory.
    The recording itself remains available from camera memory or from file.
"""