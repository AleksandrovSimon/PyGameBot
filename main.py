import cv2
from screenRec import screen_record
from imgComp import image_comapre


# coordX = 900
# coordY = 900
coordX = 925 #GOOD SAMPLE LOW
coordY = 495

Xoffset = coordX+69 #default value 69, second value 130
Yoffset = coordY+71 #default value 71, second value 115

upArray = [r'.\bin\arrow_up.png', r'.\bin\UPSCALEarrow_up.png']
downArray = [r'.\bin\arrow_down.png', r'.\bin\UPSCALEarrow_down.png']
leftArray = [r'.\bin\arrow_left.png', r'.\bin\UPSCALEarrow_left.png']
rightArray = [r'.\bin\arrow_right.png', r'.\bin\UPSCALEarrow_right.png']
blankArray = [r'.\bin\blank.png', r'.\bin\UPSCALEblank.png']

indexChoose = 0


while True:

    pic = screen_record(coordX,coordY,Xoffset,Yoffset)
    image_comapre(upArray[indexChoose], downArray[indexChoose], leftArray[indexChoose], rightArray[indexChoose], blankArray[indexChoose], pic)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break