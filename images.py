import matplotlib.pyplot as plt
from utilities import edgy, edgy_color

images = ["./img/samolot" + str(i // 10) + str(i % 10) + ".jpg" for i in range(0, 21)]

fig = plt.figure(figsize=(18, 16))

for i in range(21):
    # todo select 6 best
    print("basic " + str(i + 1) + "/6")
    a = fig.add_subplot(7, 3, i + 1)
    image = edgy(images[i])
    plt.imshow(image, cmap='gray')
    plt.axis('off')
plt.savefig('basic.pdf')

fig2 = plt.figure(figsize=(18, 16))

for i in range(21):
    # todo select 18 best
    print("advanced " + str(i + 1) + "/18")
    b = fig2.add_subplot(7, 3, i + 1)
    image = edgy_color(images[i])
    plt.imshow(image)
    plt.axis('off')
plt.savefig('advanced.pdf')
