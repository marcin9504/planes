from imread import imread
from skimage import data, io
from skimage.filters import sobel
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

fig = plt.figure()
a=fig.add_subplot()

image = imread("./img/samolot00.jpg", as_grey = True)
image = sobel(image)
io.imshow(image)
plt.axis('off')

plt.show()
