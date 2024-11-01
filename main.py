import argparse

import crawler
import iterator


def parse() -> tuple[str, str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="what are we looking for?")
    parser.add_argument("directory", type=str, help="download to")
    parser.add_argument("annotation", type=str, help="create annotation in")
    args = parser.parse_args()
    return args.keyword, args.directory, args.annotation


def main() -> None:
    keyword, directory, annotation = parse()
    try:
        class_obj = crawler.Crawler(keyword, directory, 100)
        class_obj.download()
        annotation = class_obj.create_annotation(directory)
        iterator_obj = iterator.Iterator(annotation)
        for img in iterator_obj:
            print(img)

    except Exception as e:
        print(f"An error occurred while accessing the directory: {e} ")


if __name__ == "__main__":
    main()
