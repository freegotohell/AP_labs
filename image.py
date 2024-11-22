import cv2
import matplotlib.pyplot as plt
from histogram import draw_histogram


def process_image(original_path: str, inverted_path: str) -> None:
    """
    reads an image, displays it and its inversion, and saves the inversion
    :param original_path: from terminal
    :param inverted_path: from cmd
    :return:
    """
    img = cv2.imread(original_path, -1)
    draw_histogram(img)
    if img is None:
        raise FileNotFoundError(f"Could not read image from '{original_path}'")

    height, width = img.shape[:2]
    print(f"Image size: {width}x{height}")
    inverted_img = cv2.bitwise_not(img)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('original')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('inverted')
    plt.imshow(cv2.cvtColor(inverted_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.suptitle("magic")
    plt.show()

    if not cv2.imwrite(inverted_path + ".jpg", inverted_img):
        raise OSError(f"Could not save image to '{inverted_path}.jpg'")
