import cv2
import numpy as np

# Load the image
image = cv2.imread('test.png')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# Define range of blue color in HSV
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([140, 255, 255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

# Perform morphological operations (erosion and dilation) to remove noise
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.dilate(mask, kernel, iterations=1)

# Apply closing operation
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Invert the mask to get blue regions
blue_regions = cv2.bitwise_not(mask)

# Remove blue regions from original image
image_no_blue = cv2.bitwise_and(image_rgb, image_rgb, mask=blue_regions)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image_no_blue, cv2.COLOR_RGB2GRAY)

# Apply median filtering to further reduce noise
gray_image = cv2.medianBlur(gray_image, 5)

# Save the processed image
cv2.imwrite('processed_image.png', gray_image)
