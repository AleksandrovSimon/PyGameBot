import numpy as np
from PIL import ImageGrab
from skimage.metrics import structural_similarity as compare_ssim
import cv2
import time

def screen_record(coordX, coordY, Xoffset, Yoffset):

    last_time = time.time()

    printscreen = np.array(ImageGrab.grab(bbox=(coordX,coordY,Xoffset,Yoffset)))
    #print('loop took {} seconds'.format(time.time()-last_time))
    cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
    return printscreen

