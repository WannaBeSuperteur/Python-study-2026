
## 목차

* [1. 데이터 클래스 (dataclass) 관련](#1-데이터-클래스-dataclass-관련)
  * [1-1. 데이터 중심 클래스의 필요성](#1-1-데이터-중심-클래스의-필요성)
  * [1-2. 데이터 클래스의 메서드](#1-2-데이터-클래스의-메서드)
  * [1-3. 불변 데이터 클래스](#1-3-불변-데이터-클래스)
* [2. namedtuple](#2-namedtuple)
  * [2-1. 데이터 클래스와의 공통점/차이점](#2-1-데이터-클래스와의-공통점차이점)
* [3. 모듈/패키지 구조 설계](#3-모듈패키지-구조-설계)

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
