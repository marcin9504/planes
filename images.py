import matplotlib.pyplot as plt
from imread import imread
from utilities import edgy, edgy_color

images = ["./img/samolot" + str(i // 10) + str(i % 10) + ".jpg" for i in range(0, 21)]

basic_images = ["./img/samolot" + str(i // 10) + str(i % 10) + ".jpg" for i in (0,1,3,4,5,7)]

fig = plt.figure(figsize=(60, 40))
fig.set_facecolor('black')
plt.subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=1.0,
                    wspace=0.0, hspace=0.0)
for i in range(6):
    print("basic " + str(i + 1) + "/6")
    a = fig.add_subplot(2, 3, i + 1)
    image = edgy(basic_images[i])
    plt.imshow(image, cmap='gray')
    plt.axis('off')
plt.savefig('basic.pdf', facecolor=fig.get_facecolor())

fig2 = plt.figure(figsize=(60, 35))

for i in range(18):
    # todo select 18 best
    print("advanced " + str(i + 1) + "/18")
    original = imread(images[i], as_grey=False)
    b = fig2.add_subplot(6, 3, i + 1)
    image = edgy_color(images[i])
    plt.imshow(original)
    plt.imshow(image)
    plt.axis('off')
plt.savefig('advanced.pdf')
