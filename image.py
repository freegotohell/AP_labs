import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_image(image_name: str) -> np.ndarray:
    img = cv2.imread(image_name, -1)

    if img is None:
        raise FileNotFoundError(f"could not read image from '{image_name}'")
    return img


def get_image_dimensions(img: np.ndarray) -> tuple[int, int]:
    return img.shape[:2]


def invert_image(img: np.ndarray) -> np.ndarray:
    return cv2.bitwise_not(img)


def display_images(img: np.ndarray, inverted_img: np.ndarray) -> None:
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('original')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('inverted')
    plt.imshow(cv2.cvtColor(inverted_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.suptitle("maaagic")
    plt.show()


def save_image(save_path: str, img: np.ndarray) -> None:
    if not cv2.imwrite(save_path+".jpg", img):
        raise OSError(f"could not save image to '{save_path}")
        
