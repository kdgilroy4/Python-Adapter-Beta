'''
This takes a folder with a tiffstack in it, and creates a matrix[image#][height][width][rgb] with all the .tif files in the folder
'''

#############################
import PIL
from PIL import Image
import os, os.path
import numpy as np
from matplotlib.image import imread



# Method 1 -- using imread()
# ------------------------------------
our_matrix = []
file_location = os.path.expanduser('~')+'\Desktop\Recordings\Tiff Tests\Test1\TiffStackHolder'    #put your folder holding tiffstack here, os.path.expanduser skips C:/users/username/ for you
tiffs = os.listdir(file_location)                                                                 #gives us a list of all the files in a directory
#loop through whole directory, appending files that have the right extension
for f in tiffs:                                                                                     
    ext = os.path.splitext(f)[-1]                                                                 #get file extension, splitpath splits path from extension and gives a list of it, 
    if ext == ".tif":
        our_matrix.append(imread(file_location + "\\" + f))
#print(len(our_matrix)) 
print(len(our_matrix[0]))
print(len(our_matrix[0][0]))
print(len(our_matrix[0][0][0]))
print(our_matrix[0][0][0][0])

# Method 2 -- using getdata()
# ------------------------------------
# NOT IMPLEMENTED YET
'''
an_image = PIL.Image.open("C:/Users/rfeinstein/Desktop/Test1/SDK Test/Test1/Sim_11_1_1315.tif") 
image_sequence = an_image.getdata()                                            #getdata() extract pix values from an_image
image_array = np.array(image_sequence)
print(image_array)
print(len(image_array))
x = np.reshape(image_array, (128, 1024, 3))
print(x)
'''

#an_image3 = imread("C:/Users/rfeinstein/Desktop/Test1/SDK Test/Test1/Sim_11_1_1315.tif") #imread puts image into matrix                                                                    #Linear Array of all the pixel values
#print(len(an_image3))
