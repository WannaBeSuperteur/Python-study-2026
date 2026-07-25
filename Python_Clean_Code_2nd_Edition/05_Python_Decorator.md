
## 목차

* [1. 파이썬의 데코레이터](#1-파이썬의-데코레이터)
* [2. 파이썬 데코레이터의 종류](#2-파이썬-데코레이터의-종류)
* [3. 고급 데코레이터](#3-고급-데코레이터)
  * [3-1. 데코레이터 객체 예시](#3-1-데코레이터-객체-예시)
  * [3-2. 기본값을 가진 데코레이터](#3-2-기본값을-가진-데코레이터)
  * [3-3. 기타 참고 사항](#3-3-기타-참고-사항)

## 1. 파이썬의 데코레이터

파이썬에서 데코레이터를 사용하는 이유는 다음과 같다.

* **가독성 향상** (함수의 전체 정의를 한 곳에서 찾을 수 있도록 도와줌)
* 사전 조건 검사, 파라미터의 유효성 검사 등
* 원래 함수의 결과를 캐시 처리

## 2. 파이썬 데코레이터의 종류

파이썬의 데코레이터는 **어떤 객체를 감싸는지 (함수, 클래스 등)** 에 따라 다음과 같이 분류한다.

| 분류        | 설명                                                                                                                                |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| 함수 데코레이터  | 함수를 데코레이터를 사용하여 감싸서 **함수의 기능을 변경** 할 수 있다.<br>- ```@retry``` 데코레이터의 경우 **파라미터가 불필요** 하므로 **다양한 함수에 쉽게 적용 가능**                     |
| 클래스 데코레이터 | - 함수 데코레이터와 유사<br>- 래퍼 (wrapper) 가 **함수가 아닌 클래스** 라는 점이 유일한 차이점<br>- 여러 클래스가 특정 인터페이스를 따르게 하거나, 여러 클래스에 공통으로 적용할 검사를 통합하는 등 활용 가능 |
| 기타        | - 제너레이터, 코루틴 등에 데코레이터 적용 가능<br>- 이미 데코레이팅된 객체 역시 추가 데코레이트 가능                                                                      |

```python
>>> def convert_to_percent(field: float) -> str:
	return f'{field * 100.0}%'

>>> def convert_to_score(score: float) -> str:
	return f'{score}점'

>>> def show_original(field):
	return field

>>> class SerializerTest:
	def __init__(self, fields: dict):
		self.fields = fields
	def serialize_test(self, info) -> dict:
		return {
			field: transform(getattr(info, field))
			for field, transform
			in self.fields.items()
		}

	
>>> class Serialization:
	def __init__(self, **transforms):
		self.serializer = SerializerTest(transforms)
	def __call__(self, info_class):
		def serialize(info_instance):
			return self.serializer.serialize_test(info_instance)
		info_class.serialize_test = serialize
		return info_class
```

```python
>>> from dataclasses import dataclass
>>> @Serialization(
	gpa=convert_to_score,
	job_matched=convert_to_percent,
	age=show_original
	)
@dataclass
class TestInfo:
	gpa: float
	job_matched: float
	age: int

	
>>> test_info = TestInfo(gpa=3.37, job_matched=0.825, age=30)
```

```python
>>> formatted_data = test_info.serialize_test()
>>> print(formatted_data)
{'gpa': '3.37점', 'job_matched': '82.5%', 'age': 30}
```

* ```@Serialization``` 에 의해 ```TestInfo``` 클래스에 ```serialize_test``` 메서드가 추가된다.
* ```serialize_test``` 함수가 호출되어 ```transform```에 해당하는 함수가 호출된다.
* 위와 같이 ```gpa``` 에는 ```convert_to_score``` 함수가, ```job_matched``` 에는 ```convert_to_percent``` 함수가 적용되어 변환된다는 것을 쉽게 알 수 있다.

## 3. 고급 데코레이터

고급 데코레이터를 만드는 방법은 다음과 같다.

| 방법           | 설명                                                              |
|--------------|-----------------------------------------------------------------|
| 데코레이터에 인자 전달 | 파라미터 전달을 통한 로직 추상화<br>- **데코레이터를 위한 클래스** 를 만드는 방법이 가독성이 비교적 좋음 |
| 중첩 함수 사용     | 오류 없이 작동하지만, **새로운 함수 추가 시 들여쓰기로 인해 중첩 함수가 과도하게 많아질** 수 있음      |
| 데코레이터 객체     | 중첩 함수 사용 대신, **클래스를 통해 데코레이터 정의** 가능                            |

### 3-1. 데코레이터 객체 예시

```python
>>> from time import perf_counter
>>> class TimeLogger:
	def __init__(self, goal_seconds: float):
		self.time_log = []
		self.goal_seconds = goal_seconds
	def __call__(self, func):
		def wrapper(*args, **kwargs):
			print(f'자, {func.__name__} 함수를 실행해 볼까요?')
			start_at = perf_counter()
			result = func(*args, **kwargs)
			elapsed_time = perf_counter() - start_at
			print(f'{func.__name__} 함수 실행 종료! 걸린 시간은 {elapsed_time} / {self.goal_seconds} 초입니다.')
			if elapsed_time <= self.goal_seconds:
				print(f'목표 달성 (차이: {self.goal_seconds - elapsed_time} 초)')
			else:
				print(f'목표 달성 실패 (차이: {elapsed_time - self.goal_seconds} 초)')
			return result
		return wrapper

	
>>> @TimeLogger(goal_seconds=5.0)
def test_func():
	for i in range(10_000_000):
		pass

	
>>> test_func()
자, test_func 함수를 실행해 볼까요?
test_func 함수 실행 종료! 걸린 시간은 0.173464999999851 / 5.0 초입니다.
목표 달성 (차이: 4.826535000000149 초)
>>> @TimeLogger(goal_seconds=0.45)
def test_func2():
	for i in range(30_000_000):
		pass

	
>>> test_func2()
자, test_func2 함수를 실행해 볼까요?
test_func2 함수 실행 종료! 걸린 시간은 0.6348676000002342 / 0.45 초입니다.
목표 달성 실패 (차이: 0.18486760000023422 초)
```

### 3-2. 기본값을 가진 데코레이터

* 데코레이터에 괄호가 **없는** 경우의 첫 번째 파라미터는 **함수** 이다.
* 데코레이터에 괄호가 **있는** 경우의 첫 번째 파라미터는 ```None``` 이다.

```python
>>> def execution_timer(func):
	def wrapper(*args, **kwargs):
		print(f'자, {func.__name__} 함수를 실행해 볼까요?')
		start_at = perf_counter()
		result = func(*args, **kwargs)
		elapsed_time = perf_counter() - start_at
		print(f'{func.__name__} 함수 실행 종료! 걸린 시간은 {elapsed_time} 초입니다.')
		return result
	return wrapper

>>> @execution_timer
def test_func3():
	i = 0
	while i < 20260725:
		i += 1
	return i

>>> test_func3()
자, test_func3 함수를 실행해 볼까요?
test_func3 함수 실행 종료! 걸린 시간은 0.7295540000000074 초입니다.
20260725
>>> @execution_timer()
def test_func4():
	i = 0
	while i < 20260725:
		i += 1
	return i

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    @execution_timer()
TypeError: execution_timer() missing 1 required positional argument: 'func'
```

* 데코레이터에 기본값이 있는 경우, **함수의 인자를 지정하지 않아도 호출 가능** 하다.

```python
>>> from functools import wraps
>>> def test_decorator(func=None, *, probation: int, score: int):
	def decorated(func):
		@wraps(func)
		def wrapped():
			print('==== probation evaluation start ====')
			result = func(probation, score)
			print('==== probation evaluation end ====')
			return result
		return wrapped
	return decorated

>>> @test_decorator(probation=90, score=70)
def evaluate_probation(probation, score):
	print(f'수습 기간 경과일: {probation}, 수습 평가 점수: {score}')
	if probation < 90:
		print('수습 기간 종료 이전입니다.')
	elif score >= 80:
		print('수습 합격')
	elif score >= 60:
		print('수습 연장')
	else:
		print('수습 탈락')

		
>>> evaluate_probation()
==== probation evaluation start ====
수습 기간 경과일: 90, 수습 평가 점수: 70
수습 연장
==== probation evaluation end ====
```

### 3-3. 기타 참고 사항

* 코루틴 함수에 대해 데코레이터를 만들 수 있다. 이때는 다음과 같이 한다.
  * 함수를 ```def``` 대신 ```async def``` 로 정의한다.
  * wrapping 된 부분에 대해서는 ```await``` 을 사용해야 한다.

## 4. 데코레이터를 사용하기 적합한 경우

* 데코레이터를 사용하기에 적합한 경우는 다음과 같다.

| 적합한 경우            | 설명                                                                                                   |
|-------------------|------------------------------------------------------------------------------------------------------|
| 파라미터 변환           | 파라미터 처리의 세부 로직을 숨기면서 함수의 서명을 변경하는 경우 (주의 필요)<br>- 기존의 복잡한 함수에 대해 **데코레이터를 이용하여 좋은 서명을 제공하는 경우** 에 적합 |
| 코드 추적             | 함수 실행 경로의 로깅                                                                                         |
| 파라미터 유효성 검사       | 파라미터 값, 데이터 타입 등의 유효성 검사 ('계약에 의한 디자인'과 관련)                                                          |
| 재시도 (retry) 로직 구현 |                                                                                                      |
| 반복 작업에 대한 클래스 단순화 | DRY 원칙 (중복 코드 금지) 관련                                                                                 |

## 5. 데코레이터 사용 시의 실수

데코레이터를 사용할 때 발생할 수 있는 실수는 다음과 같다.

* 원본 함수의 일부 속성을 유지하지 않는 경우 (부작용 유발)
  * 아래와 같이 하는 경우, **함수명과 docstring이 변경되는 부작용이 유발** 된다.
  * 해결 방법은 **wrapped 함수에 ```@wraps``` 데코레이터를 적용** 하는 것이다.

```python
>>> def tracer(func):
	def wrapped(*args, **kwargs):
		result = func(*args, **kwargs)
		print(f'{func.__qualname__} 실행 결과: {result}')
		return result
	return wrapped

>>> @tracer
def add(x, y):
	"""Add x and y."""
	result = x + y
	print(f'x: {x}, y: {y}, x+y: {result}')
	return result

>>> help(add)
Help on function wrapped in module __main__:

wrapped(*args, **kwargs)

>>> add.__qualname__
'tracer.<locals>.wrapped'
>>> add.__annotations__
{}
```

```python
# 해결 적용 후 (@wraps 데코레이터 적용 결과 -> 실제로는 func 함수를 wrapping 한 것임을 알려준다.)

>>> def tracer(func):
	@wraps(func)
	def wrapped(*args, **kwargs):
		result = func(*args, **kwargs)
		print(f'{func.__qualname__} 실행 결과: {result}')
		return result
	return wrapped

>>> @tracer
def add(x, y):
	"""Add x and y."""
	result = x + y
	print(f'x: {x}, y: {y}, x+y: {result}')
	return result

>>> help(add)
Help on function add in module __main__:

add(x, y)
    Add x and y.

>>> add.__qualname__
'add'
```

* 함수를 import 만 했는데 데코레이터 함수가 실행되는 경우
  * 이 경우는 **코드를 래핑된 함수 내부로 이동** 시키면 된다.
  * [_05_example_2.py](_05_example_2.py) 실행 결과는 다음과 같다. (함수 정의: [_05_example_1.py](_05_example_1.py))

```python
# _05_example_2.py

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
```

```python
# import 만 했는데 함수 실행이 시작됨
<function fill_square_1 at 0x00000290741E9F30> 함수 실행 시작
main start 1784940499.416715
1784940502.4283757

# start_at 이 이미 실행 시작되어, sleep time인 3초가 불필요하게 추가됨
<function fill_square_1 at 0x00000290741E9F30> 함수 실행 결과: 1000000, 실행 시간: 3.1859989166259766 seconds

# 래핑된 함수 내부로 코드를 이동 (fill_square_2 함수) 하면 간단히 해결됨
<function fill_square_2 at 0x00000290741EA0E0> 함수 실행 시작
<function fill_square_2 at 0x00000290741EA0E0> 함수 실행 결과: 2250000, 실행 시간: 0.34823036193847656 seconds
```
