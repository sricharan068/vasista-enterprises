import matplotlib.pyplot as plt
from PIL import Image
import io

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

buf = io.BytesIO()
fig.savefig(buf, format='png')

buf.seek(0)
img = Image.open(buf)

img.save('pil_image_save.png')
plt.show()
