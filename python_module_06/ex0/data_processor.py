#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
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


class TextProcessor(DataProcessor):
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
    print("=== Code Nexus - Data Processor ===")
    print("Testing Numeric Processor...")
    numeric: NumericProcessor = NumericProcessor()
    print(f" Trying to validate input '42': {numeric.validate(42)}")
    print(f" Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore
    except ValueError as error:
        print(f" Got exception: {error}")
    numbers_list: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {numbers_list}")
    numeric.ingest(numbers_list)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")
    print("Testing Text Processor...")
    text: TextProcessor = TextProcessor()
    print(f" Trying to validate input '42': {text.validate(42)}")
    text_list: list[str] = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_list}")
    text.ingest(text_list)
    print(" Extracting 1 value...")
    for _ in range(1):
        rank, value = text.output()
        print(f" Text value {rank}: {value}")
    print("Testing Log Processor...")
    log: LogProcessor = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    log_dict: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {log_dict}")
    log.ingest(log_dict)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")
    return None


if __name__ == "__main__":
    main()
