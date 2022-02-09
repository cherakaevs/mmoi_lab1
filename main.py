import skimage.exposure
from matplotlib import pyplot as plt
from skimage.exposure import histogram
from skimage.io import imshow, show, imread, imsave

def create_hyst(img):
    hist_red, bins_red = histogram(img[:, :, 2])
    hist_green, bins_green = histogram(img[:, :, 1])
    hist_blue, bins_blue = histogram(img[:, :, 0])
    plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
    plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
    plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)

g1 = float(input("Введите значение гаммы: "))
g2 = float(input("Введите значение множителя: "))
path = 'pathofexilebota.jpg'
img_prev = imread(path)
fig = plt.figure()
fig.add_subplot(2, 2, 1)
imshow(img_prev)
img_sec = skimage.exposure.adjust_gamma(img_prev, gamma=g1, gain=g2)
fig.add_subplot(2, 2, 2)
imshow(img_sec)
imsave('pic2.png', img_sec)
fig.add_subplot(2,2,3)
create_hyst(img_prev)
fig.add_subplot(2,2,4)
create_hyst(img_sec)
show()
fig.savefig('result')