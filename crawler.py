import os
import csv

from icrawler.builtin import GoogleImageCrawler


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

    def create_annotation(self, directory: str) -> str:
        with open('annotation.cvs', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['absolute path', ' relative path'])
            pics = os.listdir(directory)
            for i in pics:
                d = os.path.abspath(os.path.join(self.directory, i))
                f = os.path.relpath(os.path.join(self.directory, i), start=".")
                writer.writerow([d, f])
            return file.name
