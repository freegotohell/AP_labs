import argparse

from image import process_image


def parse() -> tuple[str, str]:
    """
    Parse arguments from terminal
    :return:Tuple of parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("original_path", type=str, help="path to original image")
    parser.add_argument("inverted_path", type=str, help="path to save inverted image")
    args = parser.parse_args()
    return args.original_path, args.inverted_path


def main() -> None:
    original_path, inverted_path = parse()

    try:
        process_image(original_path, inverted_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
