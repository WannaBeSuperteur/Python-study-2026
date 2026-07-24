
## 목차

* [1. 파이썬의 데코레이터](#1-파이썬의-데코레이터)
* [2. 파이썬 데코레이터의 종류](#2-파이썬-데코레이터의-종류)
* [3. 고급 데코레이터](#3-고급-데코레이터)
  * [3-1. 데코레이터 객체 예시](#3-1-데코레이터-객체-예시) 

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

