#pip3 install imutils
import cv2 
import imutils
from gtts import gTTS 
import os 

# Initializing the HOG person 
# detector 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 

# Reading the Image 
imgval = input("Enter image file name to be analyzed: ")
image = cv2.imread(imgval) 

# Resizing the Image 
image = imutils.resize(image, 
					width=min(400, image.shape[1])) 

# Detecting all the regions in the 
# Image that has a pedestrians inside it 
(regions, _) = hog.detectMultiScale(image, 
									winStride=(4, 4), 
									padding=(4, 4), 
									scale=1.05) 
len1 = (len(regions))
# Drawing the regions in the Image 
for (x, y, w, h) in regions: 
	cv2.rectangle(image, (x, y), 
				(x + w, y + h), 
				(0, 0, 255), 2) 

# Showing the output Image 
cv2.imshow("Image", image) 
cv2.waitKey(1500) 

cv2.destroyAllWindows()
print('No.of people identified:',len1)
if(int(len1)>3):
  mytext = str(len1) + 'people are identified'
  language = 'en'
  myobj = gTTS(text=mytext, lang=language, slow=False)
  myobj.save("more.mp3")
  os.system("start more.mp3")
