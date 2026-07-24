
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
