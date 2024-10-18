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


def main() -> None:
    keyword, directory, annotation = parse()
