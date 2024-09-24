import base64
import sys
import numpy as np
from PIL import Image

with open("numbers_video_base64.txt", "rb") as fp:
    numbers_video_description = fp.readline()
base64_bytes = base64.b64encode(numbers_video_description)

binary = bin(int.from_bytes(base64_bytes, byteorder=sys.byteorder))[2:]
binary_array = np.array(list(binary))
block_format = binary_array.reshape((823, 18)).astype(np.uint8) * 255

img = Image.fromarray(block_format)
img.save("output.bmp")
pass
