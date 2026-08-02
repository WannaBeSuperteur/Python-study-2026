from __future__ import annotations

import json
import operator

from pathlib import Path
from typing import Callable, Iterable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass

log_type_to_score: dict[str, Callable[[int, int], int]] = {
    "INIT": lambda x, y: y,
    "ADD": operator.add,  # lambda x, y: x + y 와 동일
    "SUB": operator.sub,  # lambda x, y: x - y 와 동일
}


# ======== NON-PYTHONIC CODE ========


def compute_final_score(path: Path, show_filter: list[str]) -> int:
    print("==== Computing Final Score ====")
    score = 0

    try:
        f = path.open("r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if not line:
                continue
            log_type = line.split("]")[0].split("[")[-1]

            if log_type in show_filter:
                json_data = json.loads(" ".join(line.split(" ")[1:]))
                score_value = json_data.get("score", 0)
                score = log_type_to_score[log_type](score, score_value)
                print(f"score updated: {score}")

                if score < 0:
                    print("You are fired!")
                    return score
    finally:
        if f:
            f.close()

    return score


# ======== PYTHONIC CODE ========


@dataclass(slots=True)
class LogRecord:
    log_type: str
    json_data: dict


@contextmanager
def open_text_file(path: Path) -> Iterator[Iterable[str]]:
    with path.open("r", encoding="utf-8") as f:
        yield f


def parse_lines(lines: Iterable[str]) -> Iterator[str]:
    for raw_str in lines:
        line = raw_str.strip()
        if not line:
            continue
        yield line


def filter_line_by_log_type(
    lines: Iterable[str], show_filter: list[str]
) -> Iterator[LogRecord]:
    for line in lines:
        log_type = line.split("]")[0].split("[")[-1]

        if log_type in show_filter:
            json_data = json.loads(" ".join(line.split(" ")[1:]))
            log_record = LogRecord(log_type=log_type, json_data=json_data)
            yield log_record


def get_updated_score(
    records: Iterable[LogRecord], current_score: int
) -> Iterator[int]:
    for record in records:
        score_value = record.json_data.get("score", 0)
        current_score = log_type_to_score[record.log_type](current_score, score_value)
        print(f"score updated: {current_score}")
        yield current_score


def compute_final_score_pythonic(path: Path, show_filter: list[str]) -> Iterator[int]:
    print("==== Computing Final Score (Pythonic) ====")
    current_score = 0

    with open_text_file(path) as lines:
        parsed_lines = parse_lines(lines)
        log_records = filter_line_by_log_type(parsed_lines, show_filter)

        for new_score in get_updated_score(log_records, current_score):
            yield new_score

            if new_score < 0:
                print("You are fired!")
                return


if __name__ == "__main__":
    path = Path("04_example.txt")
    show_filter = ["INIT", "ADD", "SUB"]

    # NOT Pythonic
    print(compute_final_score(path, show_filter))

    # Pythonic
    final_score = 0
    for score in compute_final_score_pythonic(path, show_filter):
        final_score = score
    print(final_score)
