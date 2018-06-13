from PIL import Image
import os
path = '/home/paperspace/Desktop/ObjectDetection/images/test/'
for file in os.listdir(path):
    extension = file.split('.')[-1]
    filename = file.split('.')[0]
    #print (filename)
    label = filename +'.xml.xml'
    if extension != 'jpg' and extension !='xml':
        fileLoc = path+file
        labelLoc = path+label


        #os.remove(fileLoc)
        #os.remove(labelLoc)
        print(file)
    if extension == 'jpeg' or extension =='png' or extension == 'JPG' or extension == 'gif':
        fileLoc = path+file
        labelLoc = path+label


        os.remove(fileLoc)
        os.remove(labelLoc)
        print(file)
