import easyocr 
import cv2
import matplotlib.pyplot as plt
from pylab import rcParams
from IPython.display import Image
from gtts import gTTS
import os 

rcParams['figure.figsize']=8,16
language = 'en'

reader=easyocr.Reader(['en'])
Image("chi.png")
output=reader.readtext('bg.png')
#print(output)
cord=output[-5][0]
#print(cord)
xmin,ymin=[int(min(idx)) for idx in zip(*cord)]
xmax,ymax=[int(max(idx)) for idx in zip(*cord)]
image=cv2.imread('bg.png')
cv2.rectangle(image,(xmin,ymin),(xmax,ymax),(0,0,255),2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

val=""
for x in output:
    val+=x[1]+" "
text=val.strip()

myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")

