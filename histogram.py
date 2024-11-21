import cv2
import numpy as np
import matplotlib.pyplot as plt


def draw_histogram(img: np.ndarray) -> None:
    plt.figure(figsize=(10, 5))
    colors = ('blue', 'green', 'red')

    for i, col in enumerate(colors):
        histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histogram, color=col)

    plt.title('histogram')
    plt.xlabel('intensity')
    plt.ylabel('frequency')
    plt.xlim([0, 256])
    plt.legend(colors)
    plt.show()
