
import time

from _05_example_1 import fill_square_1
# <function fill_square_1 at 0x000002479C74B5B0> 함수 실행 시작

from _05_example_1 import fill_square_2


if __name__ == '__main__':
    print('main start', time.time())
    time.sleep(3)
    print(time.time())

    fill_square_1(1000)
    fill_square_2(1500)
