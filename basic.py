from imread import imread
import matplotlib.pyplot as plt
from utilities import edgy

images = ["./img/samolot" + str(i // 10) + str(i % 10) +".jpg" for i in range(0, 21)]
fig = plt.figure(figsize = (18, 16))

for i in range(0, 6):
    a=fig.add_subplot(2, 3, i + 1)
    image = imread(images[i], as_grey = True)
    image = edgy(image)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
plt.savefig('basic.pdf')
