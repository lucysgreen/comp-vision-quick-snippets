
import cv2
from matplotlib import pyplot as plt

# Get Image 
def getImage(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img, gray 

def drawBoxes(faces, img):
    for(x,y,w,h) in faces:
        img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), -1)
        roi_colour = img[y:y+h, x:x+w]
    return img

def collectFaces(img, gray):
    # Make cascade and classify faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    return face_cascade.detectMultiScale(
        gray, scaleFactor=2.1, minNeighbors=5, minSize=(40, 40)
    )

# Main 
path = "./images/test.png"
img, gray = getImage(path)
faces = collectFaces(img,gray)
censored_img = drawBoxes(faces, img)
plt.imshow(img)
plt.show()


