import argparse

from image import *
from histogram import draw_histogram


def parse() -> tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("original_path", type=str, help="path to original image")
    parser.add_argument("inverted_path", type=str, help="path to save inverted image")
    args = parser.parse_args()
    return args.original_path, args.inverted_path


def main() -> None:
    original_path, inverted_path = parse()

    try:
        img = read_image(original_path)

        width, height = get_image_dimensions(img)
        print(f"Image size: {width}x{height}")

        draw_histogram(img)

        inverted_img = invert_image(img)
        display_images(img, inverted_img)

        save_image(inverted_img)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
