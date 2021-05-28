# max 2331 chars

import qrcode  # pip install qrcode

# import numpy as np  # optional

# import cv2 # optional
img = qrcode.make("This is my secret message that says 'Hello'")

img.save("image.png")


# access img as an array
# img_as_array = np.array(img)
# print(img_as_array)
