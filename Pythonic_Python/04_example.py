from __future__ import annotations

import json
import operator

from pathlib import Path
from typing import Callable, Iterable, Iterator
from contextlib import contextmanager, ExitStack

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
            log_type = line.split(']')[0].split('[')[-1]

            if log_type in show_filter:
                json_data = json.loads(' '.join(line.split(' ')[1:]))
                score_value = json_data.get('score', 0)
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


def compute_final_score_pythonic(path: Path, show_filter: list[str]) -> int:
    print("==== Computing Final Score ====")


if __name__ == '__main__':
    path = Path("04_example.txt")
    show_filter = ["INIT", "ADD", "SUB"]

    print(compute_final_score(path, show_filter))
    print(compute_final_score_pythonic(path, show_filter))
