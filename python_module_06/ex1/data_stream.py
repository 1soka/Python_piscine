#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    name: str = "Data Processor"

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def _store(self, value: str) -> None:
        self._storage.append((self._rank, value))
        self._rank += 1

    def total(self) -> int:
        return self._rank

    def remaining(self) -> int:
        return len(self._storage)

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def is_log(value: Any) -> bool:
    return isinstance(value, dict) and all(
        isinstance(key, str) and isinstance(item, str)
        for key, item in value.items()
    )


class NumericProcessor(DataProcessor):
    name: str = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(is_number(item) for item in data)
        return is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        return None

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break
            if not handled:
                print("DataStream error - Can't process"
                      f" element in stream: {data}")
        return None

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
        for proc in self._processors:
            print(f"{proc.name}: total {proc.total()} items processed"
                  f", remaining {proc.remaining()} on processor")
        return None


class TextProcessor(DataProcessor):
    name: str = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    name: str = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(is_log(item) for item in data)
        return is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            level = item.get("log_level", "")
            message = item.get("log_message", "")
            self._store(f"{level}: {message}")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    stream: DataStream = DataStream()
    stream.print_processors_stats()
    print()

    numeric: NumericProcessor = NumericProcessor()
    text: TextProcessor = TextProcessor()
    log: LogProcessor = LogProcessor()

    print("Registering Numeric Processor")
    stream.register_processor(numeric)
    print()

    data_list: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {data_list}")
    stream.process_stream(data_list)
    stream.print_processors_stats()
    print()

    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(data_list)
    stream.print_processors_stats()
    print()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    stream.print_processors_stats()
    return None


if __name__ == "__main__":
    main()
