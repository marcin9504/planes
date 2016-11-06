from imread import imread
from skimage.filters import sobel, gaussian
from random import *


def discretize(image):
    threshold = 20
    black = image < threshold
    white = image >= threshold
    image[black] = 0
    image[white] = 255
    return image


def edgy(image_name):
    image = imread(image_name, as_grey=True)
    image = gaussian(image, sigma=0.4)
    image = sobel(image)
    image = discretize(image)
    return image


def edgy_color(image_name):
    image = edgy(image_name)
    image2 = imread(image_name, as_grey=False)
    # random_color = [random.randrange(0, 256, 2) for i in range(3)]
    random_color = [255, 0, 0]
    black = image != 0
    image2[black] = random_color
    # TODO centroid
    return image2
