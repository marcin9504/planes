from skimage import data, io, morphology
from skimage.filters import sobel, canny, median, gaussian
from skimage.morphology import disk
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def discretize(image):
    threshold = 20
    black = image < threshold
    white = image >= threshold
    image[black] = 0
    image[white] = 255
    return image

def edgy(image):
    image = gaussian(image, sigma=0.4)
    image = sobel(image)
    image = discretize(image)
    return image