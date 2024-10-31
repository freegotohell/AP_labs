import csv


class Iterator:
    def __init__(self, annotation: str) -> None:
        self.annotation = annotation
        self.opener = None
        self.reader = None

    def __iter__(self) -> 'Iterator':
        self.opener = open(self.annotation, 'r')
        self.reader = csv.reader(self.opener)
        return self

    def __next__(self) -> str:
        if self.reader is None:
            raise StopIteration
        try:
            return next(self.reader)
        except StopIteration:
            raise StopIteration
