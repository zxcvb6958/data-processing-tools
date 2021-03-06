# encoding: utf-8
"""
@author: Cheng Wang
@date: 2019/10/17
@last modified: 2019/10/17
"""

import cv2
import numpy as np


def bilinear(img, m, n):
    height, width, channels = img.shape
    emptyImage = np.zeros((m, n, channels), np.uint8)
    value = [0, 0, 0]
    sh = m / height
    sw = n / width

    for i in range(m):
        for j in range(n):
            x = i / sh
            y = j / sw
            p = (i + 0.0) / sh - x
            q = (j + 0.0) / sw - y
            x = int(x) - 1
            y = int(y) - 1
            for k in range(3):
                if x + 1 < m and y + 1 < n:
                    value[k] = int(
                        img[x, y][k] * (1 - p) * (1 - q) + img[x, y + 1][k] * q * (1 - p) + img[x + 1, y][k] * (
                                    1 - q) * p + img[x + 1, y + 1][k] * p * q)
            emptyImage[i, j] = (value[0], value[1], value[2])

    return emptyImage


img = cv2.imread("2.jpg")
# print(img.shape)
if img.shape[0] < img.shape[1] < 256:
    target1 = 256
    target2 = img.shape[1] / img.shape[0] * 256
    target2 = int(target2)

    print('warning: image with size ({0}, {1}) is too small!'.format(img.shape[0], img.shape[1]))
elif img.shape[1] <= img.shape[0] < 256:
    target2 = 256
    target1 = img.shape[0] / img.shape[1] * 256
    target1 = int(target1)
    print('warning: image with size ({0}, {1}) is too small!'.format(img.shape[0], img.shape[1]))

result = bilinear(img, target1, target2)
cv2.imwrite('256.jpg', result)
