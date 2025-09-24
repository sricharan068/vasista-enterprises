import matplotlib.pyplot as plt
import numpy as np

img = np.random.rand(100, 100)

plt.imsave('sample_image.png', img, cmap='gray')
plt.show()
