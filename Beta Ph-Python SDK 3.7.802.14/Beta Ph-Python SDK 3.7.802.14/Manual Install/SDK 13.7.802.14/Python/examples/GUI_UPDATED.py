'''
This takes a mono cine file and turns it into a matrix[image#][height][width]
It then displays it with a simple gui that lets you go left or right to change the image, or space/esc to close it
It will also display the (x,y) coordinates of a pixel you put your mouse over, and that pixel's value
You can also press p to look at a specific pixel's value, or press c to change a specific pixel's value
'''

#############################
import keyboard #if you need this, do pip install keyboard
import cv2      #if you need this, do pip install opencv-python
import os, os.path
import numpy as np
from pyphantom import cine, Phantom, utils  #this is the phantom sdk
import copy
ph = Phantom()


# Method 1 -- using cine.get_images()
# ------------------------------------
#setup matrix and cine object
our_matrix = []
file_path = ph.file_select_dialog()   #put your cine path here, os.path.expanduser skips C:\users\username for you                                                            
our_cine = cine.Cine.from_filepath(file_path)                                         #make a cine object from our cine file

#loop through cine 1 frame at a time to create matrix, this gets around limitations of get_images() function crashing with too many frames called at once
for i in range(our_cine.range[0], our_cine.range[1]+1):                               #range is [first, last+1) so we get the whole range                               
    our_matrix.append(our_cine.get_images(utils.FrameRange(i,i)))                     #append get_images() of a frame range 1 image long to our matrix
#doing append of get_images() creates a useless dimension because get_images creates a dimension for the framerange, but we only do 1 frame per framerange here, so we np.squeeze the matrix to remove that.
our_matrix = np.squeeze(our_matrix)      

print("Number of images: " + str(len(our_matrix)))                                                           #number of images
print("Image heights " + str(len(our_matrix[0])) )                                                           #image height
print("Image widths " + str(len(our_matrix[0][0])))                                                          #image width

#creating a function that will act as a gui, letting us view and modify images

def view_multi_image_matrix(matrix):
    print("Type p if you would like to get a specific pixel's value")
    print("Type c if you would like to change a specific pixel's value")
    #setting all the text settings
    black = (255,255,255)
    font = cv2.FONT_HERSHEY_TRIPLEX
    font_size = 1.1
    font_color = black
    font_thickness = 2
    tx1,ty1 = 10, 50            #text x,y
    tx2,ty2 = 10, 100           #text2 x,y
    ix,iy = 0,0
    img_num = 0
    text = "frame number:" + str(img_num+1)
    text2 = "(" + str(ix) + ", " +  str(iy) + "): " + str(matrix[img_num][iy][ix])
    img = matrix[img_num]           #setting our original image here

    #setting text, we use copy.deepcopy() because cv2.putText changes the original image, but we want to keep the original data as well
    img_w_frames = cv2.putText(copy.deepcopy(img), text, (tx1,ty1), font, font_size, font_color, font_thickness, cv2.LINE_AA)
    img_w_xy = cv2.putText(copy.deepcopy(img_w_frames), text2, (tx2,ty2), font, font_size, font_color, font_thickness, cv2.LINE_AA)


    #mouse callback function
    def show_xy(event, x, y, flags, param):
        nonlocal ix,iy,text2,img_w_xy,img_w_frames
        #if we move the mouse to a place, we want to update the x and y values shown
        if event == cv2.EVENT_MOUSEMOVE: 
            ix,iy = x,y
            text2 = "(" + str(ix) + ", " +  str(iy) + "): " + str(matrix[img_num][iy][ix])
            img_w_frames = cv2.putText(copy.deepcopy(img), text, (tx1,ty1), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            img_w_xy = cv2.putText(copy.deepcopy(img_w_frames), text2, (tx2,ty2), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            cv2.imshow("image", img_w_xy)
    
    #naming cv2 window, and binding our mouse callback function to that window 
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', show_xy)

    while(True):
        cv2.imshow("image", img_w_xy)                                      #show original image
        cv2.waitKey(100)                                                   #refresh every 100 ms
        #if they press right arrow, add one to image
        if keyboard.is_pressed('right'):                                        
            if img_num == len(matrix)-1:
                img_num = 0
            else: 
                img_num += 1
            text = "frame number:" + str(img_num+1)
            #re-show image after changes
            img = matrix[img_num]
            text2 = "(" + str(ix) + ", " +  str(iy) + "): " + str(matrix[img_num][iy][ix])
            img_w_frames = cv2.putText(copy.deepcopy(img), text, (tx1,ty1), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            img_w_xy = cv2.putText(copy.deepcopy(img_w_frames), text2, (tx2,ty2), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            cv2.imshow("image", img_w_xy)

        #if they press left arrow, subtract one from image
        elif keyboard.is_pressed('left'):
            if img_num == 0:
                img_num = len(matrix)-1
            else: 
                img_num -= 1
            text = "frame number:" + str(img_num+1)
            #re-show image after changes
            img = matrix[img_num]
            text2 = "(" + str(ix) + ", " +  str(iy) + "): " + str(matrix[img_num][iy][ix])
            img_w_frames = cv2.putText(copy.deepcopy(img), text, (tx1,ty1), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            img_w_xy = cv2.putText(copy.deepcopy(img_w_frames), text2, (tx2,ty2), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            cv2.imshow("image", img_w_xy)

        #get the value of a specific pixel by inputting frame, y value, and x value    
        elif keyboard.is_pressed('p'):
            fnum = input("Input frame number: ")
            try:
                fnum = int(fnum)
            except:
                print("Not a legal input")
            xnum = input("Input pixel x value: ")
            try:
                xnum = int(xnum)
            except:
                print("Not a legal input")
            ynum = input("Input pixel y value: ")
            try:
                ynum = int(ynum)
            except:
                print("Not a legal input")
            print("Pixel value is " + str(matrix[fnum-1][ynum][xnum]))

        #set a new value for a specific pixel by inputting frame, y value, x value, and new pixel value
        elif keyboard.is_pressed('c'):
            fnum = input("Input frame number: ")
            try:
                fnum = int(fnum)
            except:
                print("Not a legal input")
            xnum = input("Input pixel x value: ")
            try:
                xnum = int(xnum)
            except:
                print("Not a legal input")
            ynum = input("Input pixel y value: ")
            try:
                ynum = int(ynum)
            except:
                print("Not a legal input")
            print("Old pixel value was: " + str(matrix[fnum-1][ynum][xnum]))
            newVal = input("Input new pixel value: ")
            try:
                newVal = int(newVal)
            except: 
                print(("Not a legal input"))
            if newVal > 256 or newVal < 0:
                Exception("Not a legal input")
            matrix[fnum-1][ynum][xnum] = newVal
            print("Pixel value changed to " + str(newVal))
            #re-show image after changes
            img_w_frames = cv2.putText(copy.deepcopy(img), text, (tx1,ty1), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            img_w_xy = cv2.putText(copy.deepcopy(img_w_frames), text2, (tx2,ty2), font, font_size, font_color, font_thickness, cv2.LINE_AA)
            cv2.imshow("image", img_w_xy)

        #close window and break out of loop by pressing space, esc, or enter
        elif keyboard.is_pressed('space') or keyboard.is_pressed('esc'):    
            cv2.destroyAllWindows
            break
view_multi_image_matrix(our_matrix)
                                    

ph.close()