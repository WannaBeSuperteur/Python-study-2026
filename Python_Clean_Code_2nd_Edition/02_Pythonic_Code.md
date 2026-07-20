
## 목차

* [1. 컨텍스트 관리자 (Context Manager)](#1-컨텍스트-관리자-context-manager)
* [2. 컴프리헨션 (Comprehension) 및 할당 표현식](#2-컴프리헨션-comprehension-및-할당-표현식)
  * [2-1. 컴프리헨션 및 할당 표현식을 사용하는 이유](#2-1-컴프리헨션-및-할당-표현식을-사용하는-이유)
* [3. 클래스의 속성 (attribute) 과 메서드 (method)](#3-클래스의-속성-attribute-과-메서드-method)
  * [3-1. 명령-쿼리 분리 원칙](#3-1-명령-쿼리-분리-원칙) 
* [4. dataclasses 모듈을 이용하여 클래스 만들기](#4-dataclasses-모듈을-이용하여-클래스-만들기)
* [5. 각종 객체 만들기](#5-각종-객체-만들기)
  * [5-1. 이터러블 객체 만들기](#5-1-이터러블-객체-만들기)
  * [5-2. 컨테이너 객체 만들기](#5-2-컨테이너-객체-만들기)
  * [5-3. 객체의 속성이 동적일 때](#5-3-객체의-속성이-동적일-때)
  * [5-4. 호출형 객체](#5-4-호출형-객체)

## 1. 컨텍스트 관리자 (Context Manager)

**컨텍스트 관리자 (Context Manager)** 는 **사전 조건 및 사후 조건이 중요한** 코드를 실행하는 상황에서 유용한 도구이다.

* 컨텍스트 관리자가 사용되는 대표적인 상황은 다음과 같다.
  * 리소스 관리 (파일 열기/닫기)
  * 서비스/소켓에 대한 연결 및 연결 해제

컨텍스트 관리자의 magic method 는 다음과 같다.

| 매직 메서드          | 설명                                                                                                                   |
|-----------------|----------------------------------------------------------------------------------------------------------------------|
| ```__enter__``` | 컨텍스트 진입 (다른 Python 코드 실행이 가능한)                                                                                       |
| ```__exit__```  | 컨텍스트 종료<br>- 컨텍스트 블록 내에서 Exception이 발생한 경우, 해당 Exception을 파라미터로 받음<br>- **```__exit__``` 에서 True를 반환할 때는 명확한 이유 필요** |

컨텍스트 관리자와 관련된 데코레이터 및 클래스는 다음과 같다.

| 데코레이터, 클래스                        | 설명                                                                                 |
|-----------------------------------|------------------------------------------------------------------------------------|
| ```@contextlib.contextmanager```  | 해당 데코레이터가 적용된 함수는 **컨텍스트 매니저로 변환**                                                 |
| ```contextlib.ContextDecorator``` | - 컨텍스트 관리자 안에서 실행되는 함수에 데코레이터 적용하는 로직 제공<br>- 믹스인 클래스 (Mixin Class, 메서드만을 제공하는 형태) |

## 2. 컴프리헨션 (Comprehension) 및 할당 표현식

* Python 3.8 에서 도입된 **할당 표현식 (assignment expression)** 을 통해 **조건식을 조금 더 간단히 표현** 할 수 있다.
* [참고: 02_example.py](02_example.py)

**1. 기존 코드**

```python
interest_set = set()

for person in PERSON_INFO:
    interest = person.get('interest', None)
    if interest is not None:
        interest_set = interest_set.union(interest)
```

**2. 할당 표현식을 사용한 코드**

```python
interest_set = set()

for person in PERSON_INFO:
    if (interest := person.get('interest')) is not None:
        interest_set = interest_set.union(interest)
```

**3. 할당 표현식 + set comprehension 을 사용한 코드**

```python
interest_set = {  # used set comprehension
    item
    for person in PERSON_INFO
    if (interest := person.get('interest')) is not None
    for item in interest
}
```

* 참고로, **더 짧은 코드가 항상 더 좋은 코드는 아니다. (정답은 없다?)**
  * 단, 한 줄 코드는 **이해하기 쉬운 코드가 아니라면 권장하지 않는다.**

### 2-1. 컴프리헨션 및 할당 표현식을 사용하는 이유

* 더 적은 라인으로 동일한 기능 구현 가능 (코드 간소화) + 코드 가독성 향상
* 변환 작업 등이 필요 이상으로 호출되지 않는 **성능 향상** 효과

## 3. 클래스의 속성 (attribute) 과 메서드 (method)

* 클래스 객체의 모든 속성은 **public (접근 가능)** 이다.
  * 속성과 함수 (메서드) 이름 앞에 ```_``` 를 붙이는 것은 **private (접근 불가능)** 이기를 기대하지만, **실제로는 접근이 가능하다.**
  * 다른 개발자와의 협업을 위해, **객체의 인터페이스 공개용이 아닌 속성, 메서드에는 접두사로 ```_``` 사용을 권장** 한다.
* 하나의 클래스에 속성과 메서드가 너무 많으면 **단일 책임 원칙을 위배할 우려** 가 있는 것이다.
* 속성을 private로 정의할 때는 ```__{attribute_name}``` 이 아닌 ```_{attribute_name}``` 식으로 해야 한다.

### 3-1. 명령-쿼리 분리 원칙

**명령-쿼리 분리 원칙 (command and query seperation - CC08)** 은 다음 원칙을 의미한다.

* 객체의 method는 다음 중 하나여야 하고, **둘 다 동시에 수행하면 안 된다.**
  * 무엇인가의 **상태를 변경** 하는 command
  * 무엇인가의 **값을 반환** 하는 query

이와 관련된 것으로, **1개의 method에서는 1가지를 초과하는 일을 하지 말아야** 한다. (일종의 단일 책임 원칙)

## 4. dataclasses 모듈을 이용하여 클래스 만들기

Python3.7+ 에서 제공하는 ```dataclasses``` 모듈을 이용하여, 클래스 생성을 간소화할 수 있다.

**1. 일반적인 클래스 생성 방법**

```python
>>> class Company:
	def __init__(self, name: str, is_startup: bool, is_ai_related: bool):
		self.name = name
		self.is_startup = is_startup
		self.is_ai_related = is_ai_related
	def __repr__(self) -> str:
		ai_related_str = 'AI와 관련된' if self.is_ai_related else 'AI 분야는 아닌'
		startup_str = '스타트업입니다.' if self.is_startup else '스타트업이 아닙니다.'
		return f'{self.name} 은(는) {ai_related_str} 회사이며, {startup_str}'

	
>>> motov = Company('모토브', is_startup=True, is_ai_related=True)
>>> print(motov)
모토브 은(는) AI와 관련된 회사이며, 스타트업입니다.
```

**2. dataclasses 모듈을 이용한 클래스 생성 방법**

* 초기화 후 후처리 및 검사를 위해 ```__post_init__()``` 함수를 사용한다.

```python
>>> from dataclasses import dataclass
>>> @dataclass
class Company2:
	name: str
	is_startup: bool
	is_ai_related: bool
	def __post_init__(self):
		if not self.name:
			raise ValueError('이름은 빈 값이 될 수 없습니다.')

		
>>> ghost_company = Company2(name='', is_startup=False, is_ai_related=False)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ghost_company = Company2(name='', is_startup=False, is_ai_related=False)
  File "<string>", line 6, in __init__
  File "<pyshell#37>", line 8, in __post_init__
    raise ValueError('이름은 빈 값이 될 수 없습니다.')
ValueError: 이름은 빈 값이 될 수 없습니다.

>>> artist_company = Company('아티스트컴퍼니(와이더플래닛)', is_startup=False, is_ai_related=True)
>>> artist_company
아티스트컴퍼니(와이더플래닛) 은(는) AI와 관련된 회사이며, 스타트업이 아닙니다.

# Company2 에는 아직 __repr__ 메서드가 정의되어 있지 않음
>>> artist_company = Company2('아티스트컴퍼니(와이더플래닛)', is_startup=False, is_ai_related=True)
>>> print(artist_company)
Company2(name='아티스트컴퍼니(와이더플래닛)', is_startup=False, is_ai_related=True)
```

## 5. 각종 객체 만들기

| 구분                  | 관련 메서드                         |
|---------------------|--------------------------------|
| 이터러블 (iterable) 객체  | ```__iter__```, ```__next__``` |
| 컨테이너 (container) 객체 | ```__contains__```             |
| 객체의 속성을 동적으로 할 때    | ```__getattr__```              |
| 호출형 객체              | ```__call__```                 |

## 5-1. 이터러블 객체 만들기

* 이터러블 (iterable) 객체를 만들기 위해서는 다음과 같이 ```__iter__(self)```, ```__next__(self)``` 메서드를 사용한다.

```python
>>> class Doubler():
	def __init__(self, initial_value: int = 1, limit: int = 1000):
		self.current_value = initial_value
		self.limit = limit
	def __iter__(self):
		return self  # self 를 반환하면 객체 자신이 iterable 임을 나타냄
	def __next__(self):
		if self.current_value > self.limit:
			raise StopIteration()  # iteration 중단을 위한 오류
		cur_value = self.current_value
		self.current_value *= 2
		return cur_value

	
>>> doubler = Doubler(initial_value=5, limit=100)
>>> next(doubler)
5
>>> next(doubler)
10
>>> for number in doubler:
	print(number)

	
20
40
80
>>> next(doubler)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    next(doubler)
  File "<pyshell#61>", line 9, in __next__
    raise StopIteration()  # iteration 중단을 위한 오류
StopIteration
```

## 5-2. 컨테이너 객체 만들기

* 컨테이너 (container) 객체는 ```__contains__``` 메서드가 포함된 객체로, 이 메서드는 ```in``` 키워드 호출 시의 boolean 값을 반환한다.

```python
>>> class Career():
	def __init__(self, company_name: str, start_year: int, start_month: int, end_year: int, end_month: int):
		self.company_name = company_name
		self.start_year = start_year
		self.start_month = start_month
		self.end_year = end_year
		self.end_month = end_month
	def __contains__(self, year_and_month: dict):
		year = year_and_month.get('year')
		month = year_and_month.get('month')
		if year < self.start_year:
			return False
		if year > self.end_year:
			return False
		if year == self.start_year and month < self.start_month:
			return False
		if year == self.end_year and month > self.end_month:
			return False
		return True

	
>>> motov = Career(company_name='motov', start_year=2025, start_month=10, end_year=2026, end_month=1)
>>> {'year': 2024, 'month': 1} in motov
False
>>> {'year': 2025, 'month': 9} in motov
False
>>> {'year': 2025, 'month': 10} in motov
True
>>> {'year': 2026, 'month': 1} in motov
True
>>> {'year': 2026, 'month': 2} in motov
False
>>> {'year': 2026, 'month': 7} in motov
False
```

* 코드 가독성을 향상시키기 위해, **Class 분리 + 협력 객체** 를 이용할 수도 있다.

## 5-3. 객체의 속성이 동적일 때

* 객체의 속성이 동적일 때는 ```__getattr__``` 메서드를 사용할 수 있다.

```python
>>> class Company():
	def __init__(self, name: str, employee: int):
		self.name = name
		self.employee = employee
	def __getattr__(self, attr):
		if attr.endswith('_count'):
			name = attr.replace('_count', '')
			return f'appropriate attribute name: {name}'

		
>>> kaier = Company(name='kaier', employee=7)
>>> kaier.name
'kaier'
>>> kaier.employee
7
>>> kaier.employee_count
'appropriate attribute name: employee'
```

* ```__getattr__``` 메서드의 가능한 역할은 다음과 같다.
  * 다른 객체에 대한 프록시 (proxy), 즉 **기존 객체의 메서드를 복사하는 대신, 내부적으로 같은 이름의 메서드 호출**
  * 동적으로 계산되는 속성에 사용

## 5-4. 호출형 객체

호출형 객체는 **객체를 일반 함수처럼 호출 시 ```__call__``` 메서드를 호출** 하는 것을 말한다.

```python
>>> class Doubler():
	def __init__(self, initial_value: int = 1):
		self.value = initial_value
	def __call__(self, double_count: int):
		self.value *= (2 ** double_count)

		
>>> doubler = Doubler()
>>> doubler.value
1
>>> doubler(3)
>>> doubler.value
8
>>> doubler(5)
>>> doubler.value
256
```
