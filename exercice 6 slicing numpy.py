from scipy import misc 
import matplotlib.pyplot as plt 
face = misc.face(gray=True)

def grey_print(file) :
    plt.imshow(file, cmap=plt.cm.gray)
    plt.show()


def zoom(image) :
    (axe1, axe2) = image.shape
    image_Zoom = image[int(0.25*axe1):int(0.75*axe1),int(0.25*axe2):int(0.75*axe2)]
    image_Zoom[image_Zoom > 225] = 255 #augmenter le contraste 
    image_Zoom[image_Zoom < 25] = 0
    return image_Zoom


