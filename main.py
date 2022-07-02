import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure as ex
import imageio
import sys
from PIL import Image,ImageEnhance
import cv2

def he(img):
    if(len(img.shape)==2):      #gray
        outImg = ex.equalize_hist(img[:,:])*255 
    elif(len(img.shape)==3):    #RGB
        outImg = np.zeros((img.shape[0],img.shape[1],3))
        for channel in range(img.shape[2]):
            outImg[:, :, channel] = ex.equalize_hist(img[:, :, channel])*255

    outImg[outImg>255] = 255
    outImg[outImg<0] = 0
    return outImg.astype(np.uint8)


def thresh(img):
    img = cv2.imread(img,1)
    # using normal thresholding (rather than inverse thresholding)
    (T, thresh) = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
    ab = cv2.resize(thresh,(750,550))
    print(ab.shape)
    cv2.imshow("Threshold Binary", ab)


def brightness(img):
    img = cv2.imread(img, 1)
    image_data = np.ones(img.shape, np.uint8) * 40
    bright = cv2.add(img, image_data)
    low = cv2.subtract(img, image_data)

    bc = cv2.resize(bright,(750,550))
    cd = cv2.resize(low,(750,550))

    cv2.imshow("Brightness", bc)
    cv2.imshow("Low Brightness", cd)


def sharpen(img):
    img = cv2.imread(img, 1)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen = cv2.filter2D(img, -1, kernel)
    cd = cv2.resize(sharpen,(750,550))
    cv2.imshow("Sharpen", cd)



def main_1():
    img_name = sys.argv[1]
    img = imageio.imread(img_name)
    d1 = thresh(img_name)
    d2 = brightness(img_name)
    d2 = sharpen(img_name)
    result = he(img)
    plt.title("Luminosity Based Enhancement")
    plt.imshow(result)
    plt.show()


if __name__ == '__main__':
    main_1()


def contra(img):
    img_name = sys.argv[1]
    img=Image.open(img_name)
    img_contr_obj=ImageEnhance.Contrast(img)
    factor=6
    e_img=img_contr_obj.enhance(factor)
    return e_img


def main_2():
    img_name = sys.argv[1]
    img = imageio.imread(img_name)
    resultt = contra(img)
    plt.title("Contrast Based Enhancement")
    plt.imshow(resultt)
    plt.show()


if __name__ == '__main__':
    main_2()
