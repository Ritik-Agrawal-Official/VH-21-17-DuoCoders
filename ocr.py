import easyocr 
import cv2
import matplotlib.pyplot as plt
from pylab import rcParams
from IPython.display import Image
from gtts import gTTS
import os 
from translate import Translator

cap = cv2.VideoCapture(0)
ret,frame = cap.read() 

while(True):
    cv2.imshow('bg',frame)
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('bg.png',frame)
        cv2.destroyAllWindows()
        break

rcParams['figure.figsize']=8,16
language = 'en'

cap.release()

def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()
    
image = cv2.imread('bg.png')

reader=easyocr.Reader(['es'])
Image("bg.png")
results=reader.readtext('bg.png')

# loop over the results
for (bbox, text, prob) in results:
	# display the OCR'd text and associated probability
	print("[INFO] {:.4f}: {}".format(prob, text))
	# unpack the bounding box

	(tl, tr, br, bl) = bbox
	tl = (int(tl[0]), int(tl[1]))
	tr = (int(tr[0]), int(tr[1]))
	br = (int(br[0]), int(br[1]))
	bl = (int(bl[0]), int(bl[1]))
	# cleanup the text and draw the box surrounding the text along
	# with the OCR'd text itself
	text=cleanup_text(text)
	cv2.rectangle(image, tl, br, (0, 255, 0), 2)
	cv2.putText(image, text, (tl[0], tl[1] - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)

#SPLIT_TEXT
val=""
for x in results:
    val+=x[1]+" "
text=val.strip()

#TRANSLATION
translator= Translator(from_lang="spanish",to_lang="english")
translation = translator.translate(text)
print(translation)

#TTS
myobj = gTTS(text=translation, lang=language, slow=False)
myobj.save("op.mp3")
os.system("op.mp3")
