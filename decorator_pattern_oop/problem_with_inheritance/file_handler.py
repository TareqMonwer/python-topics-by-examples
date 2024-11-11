from typing import Any, Iterable


class FileHandler:
    def read(self):
        print("Reading file")

    def write(self, data: str | Iterable[Any]):
        print(f"Writing data: {data}")


class LoggingFileHandler(FileHandler):
    def read(self):
        print("Logging: Reading file")
        super().read()

    def write(self, data: str | Iterable[Any]):
        print(f"Logging: Writing data: {data}")
        super().write(data)


class CompressedFileHandler(FileHandler):
    def write(self, data: str | Iterable[Any]):
        print(f"Compressing data: {data}")
        super().write(data)


# what if both logging and compression is needed?
class LoggingCompressedFileHandler(FileHandler):
    # methods for logging and compression goes here...
    pass
