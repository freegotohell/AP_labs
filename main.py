import argparse
import csv
import os

from icrawler.builtin import GoogleImageCrawler


def parse() -> tuple[str, str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="what are we looking for?")
    parser.add_argument("directory", type=str, help="download to")
    parser.add_argument("annotation", type=str, help="create annotation in")
    args = parser.parse_args()
    return args.keyword, args.directory, args.annotation


class Crawler:
    def __init__(self, keyword: str, directory: str, limit: int) -> None:
        self.keyword = keyword
        self.directory = directory
        self.limit = limit
        self.crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': directory}
        )

    def download(self) -> None:
        self.crawler.crawl(keyword=self.keyword, max_num=self.limit)

    def annotation(self, directory: str) -> str:
        with open('annotation.cvs', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(["absolute path", "relative path"])
            pics = os.listdir(directory)
            for i in pics:
                d = os.path.abspath(os.path.join(self.directory, i))
                f = os.path.relpath(os.path.join(self.directory, i), start=".")
                writer.writerows([d, f])
            return file.name


def main() -> None:
    keyword, directory, annotation = parse()


if __name__ == "__main__":
    main()