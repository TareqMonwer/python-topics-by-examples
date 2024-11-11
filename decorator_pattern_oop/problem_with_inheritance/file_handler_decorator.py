from abc import ABC, abstractmethod
from typing import Any, Iterable


class FileHandlerAbc(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: str | Iterable[Any]):
        pass


# Concrete file handler (maybe for .txt)
class BasicFileHandler(FileHandlerAbc):
    def read(self):
        print("Reading file")

    def write(self, data: str | Iterable[Any]):
        print(f"Writing data: {data}")


# Concrete file handler for csv files
class CsvFileHandler(FileHandlerAbc):
    def read(self):
        print("Reading CSV file")

    def write(self, data: str | Iterable[Any]):
        print(f"Writing CSV row data: {data}")


# Concrete file handler for sql files
class SqlFileHandler(FileHandlerAbc):
    def read(self):
        print("SQL file reading")

    def write(self, data: str | Iterable[Any]):
        print(f"Writing data as SQL: {data}")


# Base decorator class
class FileHandlerDecorator(FileHandlerAbc):
    def __init__(self, file_handler: FileHandlerAbc):
        self._file_handler: FileHandlerAbc = file_handler

    def read(self):
        self._file_handler.read()

    def write(self, data: str | Iterable[Any]):
        self._file_handler.write(data)


# Concrete decorator for logging
class LoggingFileHandler(FileHandlerDecorator):
    def read(self):
        print("LOG::READ:: Reading file")
        super().read()

    def write(self, data: str | Iterable[Any]):
        print(f"LOG::WRITE:: {data}")
        super().write(data)


# Concrete decorator for compression
class CompressedFileHandler(FileHandlerDecorator):
    def write(self, data: str | Iterable[Any]):
        print(f"Compressing data: {data}")
        super().write(data)


# Using decorators
file_handler = BasicFileHandler()
csv_handler = CsvFileHandler()
sql_handler = SqlFileHandler()

logging_file_handler = LoggingFileHandler(file_handler)
compressed_logging_file_handler = CompressedFileHandler(logging_file_handler)

# Perform operations
compressed_logging_file_handler.write("Hello, world!")

# Compress log csv file
compress_logging_csv_fh = CompressedFileHandler(csv_handler)
compress_logging_csv_fh.write('name, email, status')
