class Iterator:

    def __init__(self, annotation: str) -> None:
        self.annotation = annotation
        self.file = open(annotation, 'r', encoding='utf-8')
        next(self.file)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline().strip()
        if line:
            part = line.split(', ')
            return part[1]
        else:
            raise StopIteration
