from PIL import Image
import os
path = '/home/paperspace/Desktop/ObjectDetection/images/train/'
for file in os.listdir(path):
    extension = file.split('.')[-1]
    filename = file.split('.')[0]
    #print (filename)
    #label = filename +'.xml.xml'
    if extension == 'jpg':
        fileLoc = path+file
        #labelLoc = path+label

        img = Image.open(fileLoc)
        if img.mode != 'RGB':
            #os.remove(fileLoc)
            #os.remove(labelLoc)
            print(file+','+img.mode)
