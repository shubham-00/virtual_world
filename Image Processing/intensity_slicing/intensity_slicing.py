import cv2  # pip install opencv-python
import numpy as np  # pip install numpy

img = cv2.imread("original_image.jpg")

cv2.imshow("original image", img)

for intensity in [
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1,
    1.5,
    2,
    3,
    5,
    10,
]:

    intensity_corrected = np.array(
        255 * (img / 255) ** intensity, dtype="uint8"
    )

    cv2.imshow(f"{intensity} intensity", intensity_corrected)
    cv2.imwrite(f"{intensity} intensity.jpg", intensity_corrected)

cv2.waitKey(0)  # Press '0' to close all images.
