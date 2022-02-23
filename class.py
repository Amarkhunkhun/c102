import cv2
import dropbox
import time
import random

startTime = time.time()
def capture():
    number = random.randint(0,100)
    cam = cv2.VideoCapture(0)
    result = True 
    while(result):
        ret,frame = cam.read()
        imageName = "image" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        startTime = time.time
        result = False
    return imageName 
    print("snapshot taken")
    cam.release()
    cv2.destroyAllWindows()

def upload(image):
    accesToken = "azGKZgpquRUAAAAAAAAAARc1TSahqT3P2yVXplReiEnErL1Q9nh2I2NEdakr59MX"
    fileFrom = image
    fileTo = "/c102/"+(image)
    dbx = dropbox.Dropbox(accesToken)
    with open(fileFrom, "rb") as file:
        dbx.files_upload(file.read(), fileTo, mod = dropbox.files.WriteMode.overwrite)
        print("file upload")

def main():
    while(True):
        if((time.time()-startTime) >= 10):
            img = capture()
            upload(img)

main()
