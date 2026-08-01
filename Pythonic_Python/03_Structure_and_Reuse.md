
## 목차

* [1. 데이터 클래스 (dataclass) 관련](#1-데이터-클래스-dataclass-관련)
  * [1-1. 데이터 중심 클래스의 필요성](#1-1-데이터-중심-클래스의-필요성)
  * [1-2. 데이터 클래스의 메서드](#1-2-데이터-클래스의-메서드)
  * [1-3. 불변 데이터 클래스](#1-3-불변-데이터-클래스)
* [2. namedtuple](#2-namedtuple)
  * [2-1. 데이터 클래스와의 공통점/차이점](#2-1-데이터-클래스와의-공통점차이점)
* [3. 모듈/패키지 구조 설계](#3-모듈패키지-구조-설계)
* [4. 예외 처리 관련](#4-예외-처리-관련)
* [5. 테스트 코드 작성 관련](#5-테스트-코드-작성-관련)
  * [5-1. Fixture (픽스처)](#5-1-fixture-픽스처)
  * [5-2. 케이스 표 + subTest](#5-2-케이스-표--subtest)
  * [5-3. 단언 (Assertion) 관련 메서드](#5-3-단언-assertion-관련-메서드)
* [6. 타입 힌트와 정적 분석](#6-타입-힌트와-정적-분석)
  * [6-1. Optional, Union 타입](#6-1-optional-union-타입)
  * [6-2. Literal, TypedDict](#6-2-literal-typeddict)
  * [6-3. 제네릭 (Generics)](#6-3-제네릭-generics)
  * [6-4. 기타](#6-4-기타)

## 1. 데이터 클래스 (dataclass) 관련

### 1-1. 데이터 중심 클래스의 필요성

**데이터 중심 클래스** 는 **데이터 저장이 주 목적인 클래스** 를 말한다.

* 따라서 데이터 중심 클래스의 경우, **메서드가 적게 필요하다.**
* 즉, **직접 메서드를 작성하여 코드가 길어지는 것을 방지** 하기 위해 데이터 클래스가 필요하다.

### 1-2. 데이터 클래스의 메서드

```@dataclass``` 를 통해 데이터 클래스임을 명시하면, 다음 메서드들이 자동 생성된다.

| 메서드            | 설명                                 |
|----------------|------------------------------------|
| ```__init__``` | 생성자 (입력받은 값 저장)                    |
| ```__repr__``` | 객체를 보기 좋게 표현                       |
| ```__eq__```   | 객체 간 값이 같으면 True, 서로 다르면 False를 반환 |

```python
>>> @dataclass
class Point:
	x: float
	y: float
	z: float

	
>>> pt1 = Point(3.5, 2.5, 0.0)
>>> pt2 = Point(3.5, 2.5, 0.0)
>>> pt3 = Point(3.5, -1.4, 1.7)
>>> pt1.__repr__()
'Point(x=3.5, y=2.5, z=0.0)'
>>> pt2.__eq__(pt1)
True
>>> pt3.__eq__(pt2)
False
```

### 1-3. 불변 데이터 클래스

* ```@dataclass(frozen=True)``` 를 이용하여 **불변 데이터 클래스** 를 만들 수 있다.

```python
>>> @dataclass(frozen=True)
class Point:
	x: float
	y: float
	z: float
	def __str__(self):
		if any(v is None for v in (self.x, self.y, self.z)):
			return '좌표 밖의 지점'
		else:
			return f'x: {self.x}, y: {self.y}, z: {self.z}'

		
>>> pt = Point(3.0, 4.5, 7.1)
>>> print(pt)
x: 3.0, y: 4.5, z: 7.1
>>> pt.x
3.0
>>> pt.x = -2.5
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pt.x = -2.5
  File "<string>", line 4, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'x'
```

* 위와 같이 데이터 클래스의 **불변 객체** 로 만들었을 때의 장점은 다음과 같다.
  * **안전성** (값을 실수로 변경 불가)
  * **예측 가능성** (한번 지정된 값이 그대로 유지)
  * **해시 가능으로 인한 활용성** (딕셔너리 키, set의 원소 등)

## 2. namedtuple

* **namedtuple** 은 **이름으로도 값에 접근 가능한 특수한 튜플** 이다.
* **namedtuple** 의 특징은 다음과 같다.
  * 불변 (immutable)
  * **순수 데이터 저장/전달** 에 적합
  * **가볍고 빠름**
  * 인덱스, 속성 이름의 2가지 방법으로 접근 가능

```python
>>> from collections import namedtuple
>>> Company = namedtuple("Company", ["name", "months"])
>>> artistcompany = Company("Artist Company", 6)  # Company 인스턴스 생성
>>> 
>>> print(artistcompany)
Company(name='Artist Company', months=6)
>>> print(artistcompany.name)  # 속성 이름으로 접근
Artist Company
>>> print(artistcompany[0])  # 인덱스로 접근 (0 -> name)
Artist Company
>>> print(artistcompany[1])  # 인덱스로 접근 (1 -> months)
6
>>> artistcompany.months = 12  # 불변 객체이므로 수정 불가 (오류)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    artistcompany.months = 12
AttributeError: can't set attribute
```

* namedtuple과 일반 튜플의 차이점은 순서 (index) 뿐만 아니라 **속성 이름으로도 접근** 할 수 있다는 것이다.

### 2-1. 데이터 클래스와의 공통점/차이점

* 데이터 클래스와의 공통점
  * 데이터 중심 클래스를 간단하게 표현한 것 (**데이터 저장 구조체** 역할)
  * 기본 메서드 제공 (```__init__```, ```__repr__```, ```__eq__```)
* 데이터 클래스와의 차이점
  * 아래 용도를 기준으로 **데이터 클래스를 사용할지, namedtuple을 사용할지 적절히 선택** 해야 한다.

| 구분     | 데이터 클래스 (```@dataclass```)        | namedtuple |
|--------|-----------------------------------|------------|
| 가변/불변  | 가변 (```frozen=True``` 시 불변)       | 불변         |
| 메서드 추가 | 가능                                | 불가능        |
| 용도     | 데이터 + 행동 (함수, method) 을 **함께 사용** | 단순한 값 저장   |

## 3. 모듈/패키지 구조 설계

참고: [Python 모듈/패키지 관련](01_Python_Basics.md#3-파이썬-모듈-패키지-관련)

* ```__init__.py``` 의 역할
  * Python이 **이 폴더는 패키지임** 을 인식하도록 함
  * **공개 API 관리** (하위 모듈의 함수를 import 하는 방식으로 해당 모듈을 공개 API로 사용 가능하게 함)
  * **re-export** (재-내보내기) 
    * 예를 들어 ```myapp/__init__.py```, ```myapp/ml_models.py``` 가 있다고 할 때, ```myapp/__init__.py``` 에서 ```from .ml_models import run_one_epoch``` 라고 하면 ```myapp.run_one_epoch``` 로 API로 직접 사용 가능하게 된다.
    * 이때 ```myapp/__init__.py``` 에 ```__all__ = ["run_one_epoch"]``` 와 같이 **외부에 공개할 기능을 제한하여 지정** 할 수 있다.
    * 내부 구현 (예: ```myapp/ml_models.py``` 에 정의된 ```EARLY_STOPPING_PATIENCE = 10```) 등은 숨겨진다.
* 버전 정보 관리
  * 버전 정보는 패키지 디렉토리 내부의 ```version.py``` (예: ```myapp/version.py```) 에 정의한다.
  * 버전 정의 방법은 ```__version__ = "1.2.3"``` 과 같이 한다.
  * 버전 정보를 한 곳에 정리해야 하는 이유는 **관리의 편의성, 유지보수 (버전 변경 시 파일 1개만 바꾸면 됨), 문서화, 배포 도구 연동** 등이다.
* import 모범 사례

| 패키지 내부 코드                                                        | 패키지 외부 사용자                                                                 |
|------------------------------------------------------------------|----------------------------------------------------------------------------|
| **상대** import<br>(예: ```from .ml_models import run_one_epoch```) | **패키지명을 포함** 한 **절대** import<br>(예: ```from myapp import run_one_epoch```) |
 
* 기타
  * ```__init__.py``` 에는 실행 코드를 넣지 않는다. **(부수 효과 예측 어려움)**

## 4. 예외 처리 관련

* Python에서 [EAFP](../Python_Clean_Code_2nd_Edition/03_Good_Code_Characteristics.md#4-개발-지침-약어-및-설명) 를 선호하는 이유
  * 가독성 향상
  * 흐름 단순화 (조건문 중첩 대신 예외 처리)
  * 실제 표준 라이브러리 코드의 트렌드도 EAFP 임
* **예외 계층** ([참고](../Practical_Python_programming/04_Class_and_Object.md#5-커스텀-예외-정의하기)) 이 필요한 이유
  * 프로그램 크기 증가에 따른 **다양한 오류 상황**
  * 모든 예외를 **한번에 관리하기 어려움**
* 예외 변환 (Exception Translation)
  * **예외 변환** 은 저수준 예외를 **의미 있는 커스텀 예외로 변환** 하는 것이다.
    * 이를 통해 **어떤 일이 있었는지 쉽게 추적** 할 수 있다.
  * ```raise NewException from e``` 를 통해, 원래 예외 ```e``` 를 원인으로 한 새로운 예외 ```NewException``` 로 던진다.

```python
>>> class CustomError(Exception):
	def __init__(self, msg: str, expression: str):
		super().__init__(f"error: {msg} (수식: {expression})")

		
>>> def div(a: int, b: int) -> float:
	try:
		return a / b
	except ZeroDivisionError as e:
		raise CustomError(str(e), f'{a} / {b}')

	
>>> div(15, 5 - (3 + 2))
Traceback (most recent call last):
  File "<pyshell#76>", line 3, in div
    return a / b
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    div(15, 5 - (3 + 2))
  File "<pyshell#76>", line 5, in div
    raise CustomError(str(e), f'{a} / {b}')
CustomError: error: division by zero (수식: 15 / 0)
```

* [커스텀 예외](../Practical_Python_programming/04_Class_and_Object.md#5-커스텀-예외-정의하기) 에는 **맥락 정보 (이유 등)** 를 담는 것이 좋다. 그 이유는 다음과 같다.
  * 사용자 친화적 오류 피드백을 통한 **편리한 디버깅**
  * **오류 로그 가독성** 향상
* 예외는 **프로그램의 흐름을 안전하고 예측 가능하게 만드는 도구** 이므로 중요하다.

## 5. 테스트 코드 작성 관련

### 5-1. Fixture (픽스처)

**픽스처 (Fixture)** 는 테스트 전 setup, 테스트 후 teardown (정리) 을 자동화하는 구조이다.

* 이를 통해 **테스트마다 같은 준비 코드, 정리 코드를 반복하지 않아도** 된다.
* 결과적으로 **가독성 향상, 안전성 보장 (teardown 에 의한)** 이 이루어진다.
* Fixture의 함수

| 함수               | 설명                       |
|------------------|--------------------------|
| ```setup()```    | 각 테스트의 **실행 직전** 에 자동 호출 |
| ```tearDown()``` | 각 테스트의 **실행 직후** 에 자동 호출 |

```python
>>> def add_three(a, b, c):
	return a + b + c

>>> import unittest
>>> class TestCalcWithFixture(unittest.TestCase):
	def setUp(self):
		print('setup')
		self.a = 5
		self.b = 8
		self.c = 10
		print(f'setup finished: a={self.a}, b={self.b}, c={self.c}')
	def tearDown(self):
		print('teardown')
	def test_int(self):
		result = add_three(self.a, self.b, self.c)
		self.assertEqual(result, 23)
	def test_float(self):
		result = add_three(self.a / 2.0, self.b / 2.0, self.c / 2.0)
		self.assertEqual(result, 11.5)
	def test_str(self):
		result = add_three(str(self.a), str(self.b), str(self.c))
		self.assertEqual(result, '5810')

		
>>> unittest.main()
setup
setup finished: a=5, b=8, c=10
teardown
.setup
setup finished: a=5, b=8, c=10
teardown
.setup
setup finished: a=5, b=8, c=10
teardown
.
----------------------------------------------------------------------
Ran 3 tests in 0.216s

OK
```

### 5-2. 케이스 표 + subTest

* 문제점
  * 여러 가지 케이스를 한번에 테스트할 때, **테스트 케이스마다 assertEqual 을 넣으면 코드가 지저분해진다.**
* 해결 방법
  * 다음과 같이 **케이스 표 + subTest** 를 이용한다.
  * 장점은 **코드 간결화, 테스트 결과 가독성 향상, 편리한 유지보수 (리스트에 한 줄 추가로 테스트 케이스 1개 추가)** 이다.

| 구분      | 설명                          |
|---------|-----------------------------|
| 케이스 표   | 입력과 기대값을 리스트에 저장, 반복문으로 처리  |
| subTest | 반복문을 돌리면서 **실패한 개별 입력을 표시** |

```python
>>> import unittest
>>> def add_three(a, b, c):
	return a + b + c

>>> class TestCalcSubTest(unittest.TestCase):
	def test_add_three_cases(self):
		cases = [
			(5, 8, 10, 23),
			(2.5, 4.0, 5.0, 11.5),
			(1.25, 3.75, 4.5, 9.5),
			('a', 'b', 'c', 'abc'),
			('d', 'e', 'f', 'def')
		]
		for a, b, c, expected in cases:
			with self.subTest(a=a, b=b, c=c):
				self.assertEqual(add_three(a, b, c), expected)

				
>>> unittest.main()
```

```python
>>> def div_three(a, b, c):
	return (a + b) / c

>>> class TestCalcSubTest2(unittest.TestCase):
	def test_div_three_cases(self):
		cases = [
			(5, 7, 3, 4.0),
			(12, 16, 4, 7.0),
			(1, 1, 8, 0.25),
			(4, 6, 0, 10.0),
			(2, 3, 6, 0.833),
			(2, 4, 4, 1.5)
		]
		for a, b, c, expected in cases:
			with self.subTest(a=a, b=b, c=c):
				self.assertEqual(div_three(a, b, c), expected)

				
>>> unittest.main()
.
======================================================================
ERROR: test_div_three_cases (__main__.TestCalcSubTest2) (a=4, b=6, c=0)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<pyshell#24>", line 13, in test_div_three_cases
  File "<pyshell#22>", line 2, in div_three
ZeroDivisionError: division by zero

======================================================================
FAIL: test_div_three_cases (__main__.TestCalcSubTest2) (a=2, b=3, c=6)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<pyshell#24>", line 13, in test_div_three_cases
AssertionError: 0.8333333333333334 != 0.833

----------------------------------------------------------------------
Ran 2 tests in 0.009s

FAILED (failures=1, errors=1)
```

### 5-3. 단언 (Assertion) 관련 메서드

* Assertion 관련 메서드는 다음과 같다.

| 메서드                           | 설명                                                               |
|-------------------------------|------------------------------------------------------------------|
| ```assertEqual(a, b)```       | 값이 서로 **정확히** 동일한지 판단                                            |
| ```assertAlmostEqual(a, b)``` | 값이 서로 **거의 동일한지**<br>(```float``` 계산 테스트에서는 **부동소수점 오차** 때문에 필요) |
| ```assertTrue(x)```           | 조건이 참인지 판단                                                       |
| ```assertFalse(x)```          | 조건이 거짓인지 판단                                                      |
| ```assertRaises(Exception)``` | 예외/오류 ```Exception``` 발생 여부 판단                                   |

* ```assertAlmostEqual(a, b)``` 대신 ```assertTrue(math.isclise(...))``` 를 사용할 수 있다.

## 6. 타입 힌트와 정적 분석

### 6-1. Optional, Union 타입

| 구분       | 설명                    | 표현                                                |
|----------|-----------------------|---------------------------------------------------|
| Optional | 값이 있을 수도 있고, 없을 수도 있음 | ```Optional[type]``` 또는 ```type \| None```        |
| Union    | 여러 type 중 하나에 해당하는 값  | ```Union[type1, type2]``` 또는 ```type1 \| type2``` |

* **타입 내로잉 (Type Narrowing)** 은 Optional 또는 Union으로 정의된 값에 대해 **```if```, ```isinstance()``` 등으로 실제 타입을 확인 후 사용** 하는 것이다.

### 6-2. Literal, TypedDict

| 구분        | 설명                                                                        | 표현                                 |
|-----------|---------------------------------------------------------------------------|------------------------------------|
| Literal   | 변수에 허용된 값의 종류를 제한<br>- 즉, **허용된 값 범위를 강제**                                | ```Literal[value1, value2, ...]``` |
| TypedDict | **꼭 있어야 하는 key 및 해당 key의 값의 type** 을 미리 정의<br>- 이를 통해 **딕셔너리의 안전한 사용 보장** | ```class OOODict(TypedDict)```     |

```python
>>> from typing import TypedDict, Literal
>>> EmployeeStatus = Literal["수습기간", "수습연장", "정규직", "계약직"]
>>> class Employee(TypedDict):
	employee_id: int
	name: str
	status: EmployeeStatus

	
>>> hskim: Employee = {'employee_id': 1, 'name': 'hskim', 'status': '정규직'}
>>> print(hskim)
{'employee_id': 1, 'name': 'hskim', 'status': '정규직'}
```

### 6-3. 제네릭 (Generics)

**제네릭 (Generics)** 은 **하나의 틀에 여러 타입을 적용** 하기 위한 방법이다.

* 즉, **타입 정보를 유지하면서 재사용 가능** 하게 한다.
* **오버로드 (overload)** 는 함수가 **입력값에 따라 반환값의 타입이 서로 다른** 것을 말한다.

제네릭의 유용성은 다음과 같다.

* 상황에 따라 함수 반환값의 타입이 달라지는 부분을, 타입 검사 도구가 미리 찾아서 잡아준다.
* 협업 시, **함수 입력값에 따라 반환 타입이 명확해진다. (문서화 역할)**

```python
>>> from typing import TypeVar
>>> T = TypeVar('T', int, float)
>>> def is_probation_passed(score: T) -> bool:
	print(f'probation score: {score} / 100')
	return score >= 75

>>> print(is_probation_passed(80))
probation score: 80 / 100
True
>>> print(is_probation_passed(80.0))
probation score: 80.0 / 100
True
```

### 6-4. 기타

* **프로토콜 (Protocol)** 은 어떤 클래스가 **특정 메서드/속성을 가지면 된다** 는 인터페이스 개념으로, **필요한 메서드가 있으면 통과** 를 의미한다.
  * 즉, **형식보다는 기능에 초점** 을 둔다.
  * 같은 메서드를 갖는 여러 클래스가 **계층 구조가 서로 다를 수 있기 때문에** 중요하다.
* **완전성 검사** 는 조건문 등에서 **모든 경우를 빠짐없이 처리했는지 확인** 하는 것을 말한다.
  * 실수로 빠뜨린 경우를 ```mypy``` 라는 검사 도구를 통해 알 수 있다.

