import statistics

import numpy as np
from skimage.color import rgb2hsv
from imread import imread
from scipy import ndimage, random
from skimage.filters import gaussian, sobel_h, sobel_v
from skimage.segmentation import find_boundaries
from skimage.morphology import dilation


def discretize(image):
    threshold = 20
    black = image < threshold
    white = image >= threshold
    image[black] = 0
    image[white] = 255
    return image


def edgy(image_name):
    image = imread(image_name, as_grey=True)
    image = gaussian(image, sigma=.97)
    image = custom_sobel(image)
    image = discretize(image)
    return image


def custom_sobel(image):
    edge_horizont = sobel_h(image)
    edge_vertical = sobel_v(image)
    magnitude = np.hypot(edge_horizont, edge_vertical)
    return magnitude


def edgy_color(image_name):
    image = imread(image_name, as_grey=False)
    original = imread(image_name, as_grey=False)

    image = rgb2hsv(image)
    image = image[..., 2]

    objects, objects_count = ndimage.label(image < .5)

    sizes = ndimage.sum(image, objects, range(objects_count + 1))
    mask_size = sizes < 35
    remove_pixel = mask_size[objects]
    objects[remove_pixel] = 0
    labels = np.unique(objects)
    objects = np.searchsorted(labels, objects)

    contours = find_boundaries(objects)
    objects[contours == 0] = 0
    objects = dilation(objects)
    objects = dilation(objects)
    objects = dilation(objects)

    colours = []
    for _ in range(objects_count + 1):
        colours.append([random.randint(256) for _ in range(3)])

    result = [[org if obj == 0 else colours[obj] for org, obj in zip(row_org, row_obj)]
              for row_org, row_obj in zip(original, objects)]
    # fixme combining the 2 images (original & objects)

    centroids = find_centroids(objects)
    # todo if the function is correct, draw white circles centered in the centroids

    return result  # to see the contours alone, return objects


def find_centroids(labels):
    centroids_all = {}
    for i, row in enumerate(labels.tolist()):
        for j, element in enumerate(row):
            if element not in centroids_all:
                centroids_all[element] = {'x': [], 'y': []}
            centroids_all[element]['x'].append(j)
            centroids_all[element]['y'].append(i)
    centroids = []
    for key, value in centroids_all.items():
        centroids.append((statistics.mean(value['x']),
                          statistics.mean(value['y'])))
    return centroids
