
## 목차

* [1. ```unittest``` 모듈 사용법](#1-unittest-모듈-사용법)
* [2. ```logging``` 모듈](#2-logging-모듈)
* [3. 디버깅 시 print 대신 repr 함수 사용](#3-디버깅-시-print-대신-repr-함수-사용)
* [4. 디버거에서 실행하기](#4-디버거에서-실행하기)

## 1. ```unittest``` 모듈 사용법

* ```unittest``` 모듈을 사용하여 **테스트 케이스를 만들고 테스트를 실시** 할 수 있다.
  * 여기서 메서드 이름은 **반드시 ```test``` 로 시작해야 한다.** 

```python
>>> def add_three(a, b, c):
	return a + b + c

>>> import unittest
>>> class TestAdd(unittest.TestCase):
	def test_int(self):
		result = add_three(5, 8, 10)
		self.assertEqual(result, 23)
	def test_float(self):
		result = add_three(3.25, 4.5, 7.0)
		self.assertEqual(result, 14.75)
	def test_str(self):
		result = add_three('a', 'b', 'c')
		self.assertEqual(result, 'abc')


>>> unittest.main()
...
----------------------------------------------------------------------
Ran 3 tests in 0.054s

OK
```

* ```unittest``` 의 테스트 케이스 테스트용 함수는 다음과 같다.

| 함수                                      | 함수 설명                                                     |
|-----------------------------------------|-----------------------------------------------------------|
| ```self.assertTrue(expression)```       | ```expression``` 의 결과값이 ```True``` 인지 검사                  |
| ```self.assertEqual(x, y)```            | ```x == y``` 인지 검사                                        |
| ```self.assertNotEqual(x, y)```         | ```x != y``` 인지 검사                                        |
| ```self.assertAlmostEqual(x, y, 자릿수)``` | ```x```와 ```y```를 소수점 이하 ```자릿수``` 자리만큼 반올림한 값이 서로 같은지 검사 |

## 2. ```logging``` 모듈

```logging``` 모듈은 **logging (진단 정보 기록)** 을 위한 라이브러리이다.

* ```logging``` 모듈의 심각도 (severity) 수준을 높은 순서대로 정렬하면 다음과 같다.
  * ```logger.critical()```
  * ```logger.error()```
  * ```logger.warning()```
  * ```logger.info()```
* 디버깅 목적의 메시지는 다음과 같이 출력한다.
  * ```logger.debug()```

## 3. 디버깅 시 print 대신 repr 함수 사용

* print 함수는 **값 그 자체** 만을 출력하지만, repr 함수는 **값의 표현 (representation)** 를 출력한다.

```python
>>> repr('abcd')
"'abcd'"
>>> repr(1234)
'1234'
>>> repr(0.5)
'0.5'
>>> from decimal import Decimal
>>> x = Decimal(123.456)
>>> print(x)
123.4560000000000030695446184836328029632568359375
>>> repr(x)
"Decimal('123.4560000000000030695446184836328029632568359375')"
```

## 4. 디버거에서 실행하기

* 다음과 같이 ```breakpoint()``` 함수를 호출하면 해당 부분붜 **Python 디버거가 실행된다.** (단, Python3.7+)
* [example.py](example.py)

```python
import math

def is_prime(n):
    breakpoint()  # start debugger (Python 3.7+)
    if n <= 1:
        return False

    sqn = int(math.sqrt(n))
    for d in range(2, sqn):  # sqn + 1 is correct, sqn is wrong
        if n % d == 0:
            return False

    return True


if __name__ == '__main__':
    print(is_prime(2023))
    print(is_prime(49))
```
