import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('watchgrey.png', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

