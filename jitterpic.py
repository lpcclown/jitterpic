import cv2
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import image

img = cv2.imread(r'C:/test/1.png')
img = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)  # cv2 defaul color code is BGR
h,w,c = img.shape # (768, 1024, 3)
noise = np.random.randint(0,50,(h, w)) # design jitter/noise here
zitter = np.zeros_like(img)
zitter[:,:,1] = noise
noise_added = cv2.add(img, zitter)

# combined = np.vstack((img[:h,:,:], noise_added[h:,:,:]))
# combined = np.vstack((img[:h/2,:,:], noise_added[h/2:,:,:]))
# combined = np.vstack((img[:h/3,:,:], noise_added[h/3:,:,:]))

combined = np.vstack((img[:h/4,:,:], noise_added[h/4:,:,:]))
# imshow(combined, interpolation='none')

# this code is used to remove white frame in the pic
fig = plt.figure(frameon=False)
fig.set_size_inches(0.73,0.7)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(combined, aspect='auto')
# save the pic
fig.savefig(r'C:/test/2.png')

