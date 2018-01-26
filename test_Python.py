import cv2
#import cv2.cv as cv
import numpy as np
import os
import time
import sys, time

def get_images(path, size):
    '''
    path: path to a folder which contains subfolders of for each subject/person
        which in turn cotains pictures of subjects/persons.

    size: a tuple to resize images.
        Ex- (256, 256)
    '''
    sub= 0
    images, labels= [], []
    people= []

    for subdir in os.listdir(path):
    	print('for 1')
        #if os.path.isdir(subdir):
        for image in os.listdir(path+ "/"+ subdir):
            print(subdir, images)
            img= cv2.imread(path+os.path.sep+subdir+os.path.sep+image, cv2.IMREAD_GRAYSCALE)
            img= cv2.resize(img, size)

            images.append(np.asarray(img, dtype= np.uint8))
            labels.append(sub)

                #cv2.imshow("win", img)
                #cv2.waitKey(10)

        people.append(subdir)
        sub+= 1

    return [images, labels, people]

'''
color_img= cv2.imread("input_images/1.jpg")
print(color_img)
print("===================================")
gray_img= cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
print(gray_img)
'''

'''
for subdir in os.listdir('/Users/realz/Desktop/FaceRecognizer/sorted_output_images/'):
    print(subdir)
'''

[images, labels, people] = get_images('/Users/realz/Desktop/FaceRecognizer/sorted_output_images', (256, 256))
print([images, labels , people]) 



#labels= np.asarray(labels, dtype= np.int32)
# initializing eigen_model and training
#print("Initializing eigen FaceRecognizer and training...")
#sttime= time.clock()
#eigen_model= cv2.face.createEigenFaceRecognizer()
#eigen_model.train(images, labels)