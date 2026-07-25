
import time
from functools import wraps

import numpy as np


def time_tracer_1(func):
    print(f'{func} 함수 실행 시작')
    start_at = time.time()

    @wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_at
        print(f'{func} 함수 실행 결과: {result}, 실행 시간: {elapsed_time} seconds')
        return result
    return wrapped


@time_tracer_1
def fill_square_1(side_length: int):
    square = [[0 for _ in range(side_length)] for _ in range(side_length)]
    for i in range(side_length):
        for j in range(side_length):
            square[i][j] = 1
    return np.sum(np.array(square))


def time_tracer_2(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(f'{func} 함수 실행 시작')
        start_at = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_at
        print(f'{func} 함수 실행 결과: {result}, 실행 시간: {elapsed_time} seconds')
        return result

    return wrapped


@time_tracer_2
def fill_square_2(side_length: int):
    square = [[0 for _ in range(side_length)] for _ in range(side_length)]
    for i in range(side_length):
        for j in range(side_length):
            square[i][j] = 1
    return np.sum(np.array(square))

