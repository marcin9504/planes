from imread import imread
from skimage import data, io, morphology
from skimage.filters import sobel, canny
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

fig = plt.figure(figsize = (18, 16))
for i in range(0, 6):
    a=fig.add_subplot(2, 3, i + 1)
    image = imread("./img/samolot0" + str(i) +".jpg", as_grey = True)
    image = sobel(image)
    threshold = 20
    black = image < threshold
    white = image >= threshold
    image[black] = 0
    image[white] = 255
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    #
    # img = cv2.imread('./img/samolot00.jpg', 0)
    # edges = cv2.Canny(img, 100, 200)
    #
    # plt.subplot(121), plt.imshow(img, cmap='gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(edges, cmap='gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
