import cv2
import sys

# Read the image
img = cv2.imread("sheep.png", cv2.IMREAD_ANYCOLOR)

# Display the image
while True:
cv2.imshow("Sheep", img)
cv2.waitKey(0)
sys.exit()

cv2.destroyAllWindows()