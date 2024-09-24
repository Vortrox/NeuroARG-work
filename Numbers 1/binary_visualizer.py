import base64
import sys
import numpy as np
from PIL import Image
import matplotlib as plt

with open("numbers_video_base64.txt", "rb") as fp:
    numbers_video_description = fp.readline()
base64_bytes = base64.b64encode(numbers_video_description)

binary = bin(int.from_bytes(base64_bytes, byteorder=sys.byteorder))[2:]
binary_array = np.array(list(binary))
block_format = binary_array.reshape((18, 823)).astype(np.uint8) * 255
block_format_3d = binary_array.reshape((3, 6, 823)).astype(np.uint8)

img = Image.fromarray(block_format)
img.save("output.png")

fig = plt.figure(figsize=(8, 10), dpi=80)
ax = fig.add_subplot(projection='3d')
ax.scatter(block_format_3d[:, 0], block_format_3d[:, 1], block_format_3d[:, 2])
pass