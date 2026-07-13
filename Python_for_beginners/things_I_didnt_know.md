
## 목차

* [1. 리스트](#1-리스트)
* [2. 인터프리터와 컴파일러](#2-인터프리터와-컴파일러)
* [3. for-else 와 while-else](#3-for-else-와-while-else)
* [4. Python의 LEGB Rule](#4-python의-legb-rule)
* [5. map 함수와 reduce 함수](#5-map-함수와-reduce-함수)
  * [5-1. map 함수](#5-1-map-함수)
  * [5-2. reduce 함수](#5-2-reduce-함수)
* [6. 인자 (매개변수)](#6-인자-매개변수)
* [7. 튜플 관련](#7-튜플-관련)
  * [7-1. 튜플과 리스트의 차이](#7-1-튜플과-리스트의-차이)
  * [7-2. 튜플 관련 참고 사항](#7-2-튜플-관련-참고-사항)
* [8. dict 의 원소 (key, value pair) 출력 방법](#8-dict-의-원소-key-value-pair-출력-방법)
* [9. set 관련 사항](#9-set-관련-사항)
  * [9-1. set 의 교집합, 합집합, 차집합](#9-1-set-의-교집합-합집합-차집합)
  * [9-2. set, list의 membership test (존재 여부)](#9-2-set-list의-membership-test-존재-여부)
* [10. 모듈 (module) 관련](#10-모듈-module-관련)
* [11. string 모듈](#11-string-모듈)
* [12. 날짜/시간 다루기](#12-날짜시간-다루기)
* [13. 텍스트 파일 읽기/쓰기](#13-텍스트-파일-읽기쓰기)
* [14. pickle, glob](#14-pickle-glob)
  * [14-1. pickle](#14-1-pickle)
  * [14-2. glob](#14-2-glob)
* [15. del, repr, add, lt 메서드](#15-del-repr-add-lt-메서드)
* [16. 프로그램 실행 시간 측정하기](#16-프로그램-실행-시간-측정하기)
* [17. 파이썬으로 데이터베이스 다루기](#17-파이썬으로-데이터베이스-다루기)

## 1. 리스트

* [1.3 리스트 (list)](https://wikidocs.net/53)
  * ```list[1:5:2]``` 처럼 간격 (step) 을 줄 수 있다.

```python
>>> list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
>>> list[1:5]
['b', 'c', 'd', 'e']
>>> list[1:5:2]
['b', 'd']
>>> list[1:10]
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
>>> list[1:10:2]
['b', 'd', 'f', 'h', 'j']
>>> list[1:10:3]
['b', 'e', 'h']
```

## 2. 인터프리터와 컴파일러

* [1.4 인터프리터와 컴파일러](https://wikidocs.net/132948)
  * **인터프리트 (interpret) 방식:** 사람이 짠 Python 코드를 한 줄씩 해석하여 작업을 처리하는, Python의 처리 방식
    * **컴파일 (compile)** 은 **코드 전체를 번역한 후 처리** 한다는 점에서 인터프리트 방식과 차이가 있음 
  * **인터프리터 (interpreter):** 사람이 Python으로 작성한 프로그램을 컴퓨터에게 번역 (0과 1로) 하는 Python shell

## 3. for-else 와 while-else

* [2.5 for-else와 while-else](https://wikidocs.net/190098)

| 구분         | 설명                                                              |
|------------|-----------------------------------------------------------------|
| for-else   | 반복문이 모두 실행된 후 ```else``` 아래쪽이 실행됨 (```break``` 를 사용할 시 실행되지 않음) |
| while-else | for-else와 동일하게 작동                                               |

```python
>>> for company in ['qara', 'kaier', 'motov', 'widerplanet']:
	print(f'회사 이름: {company}')
else:
	print(f'현재 재직 중인 회사: {company}')

	
회사 이름: qara
회사 이름: kaier
회사 이름: motov
회사 이름: widerplanet
현재 재직 중인 회사: widerplanet
```

```python
>>> for company in ['qara', 'kaier', 'motov', 'widerplanet']:
	print(f'회사 이름: {company}')
	if company == 'motov':
		print(f'{company} 입사 전 공백기 9개월')
		break
else:
	print(f'현재 재직 중인 회사: {company}')

	
회사 이름: qara
회사 이름: kaier
회사 이름: motov
motov 입사 전 공백기 9개월
```

```python
>>> year = 2020
>>> while year <= 2026:
	print(f'{year}년은 현재 또는 과거입니다.')
	year += 1
else:
	print(f'{year}년은 미래입니다. 희망찬 미래를 꿈꿔 보세요!')

2020년은 현재 또는 과거입니다.
2021년은 현재 또는 과거입니다.
2022년은 현재 또는 과거입니다.
2023년은 현재 또는 과거입니다.
2024년은 현재 또는 과거입니다.
2025년은 현재 또는 과거입니다.
2026년은 현재 또는 과거입니다.
2027년은 미래입니다. 희망찬 미래를 꿈꿔 보세요!
```

## 4. Python의 LEGB Rule

* [3.3. 지역변수, 전역변수](https://wikidocs.net/62)

| 구분            | 설명                                         |
|---------------|--------------------------------------------|
| L (Local)     | **현재 함수 내에서** 정의된 변수                       |
| E (Enclosing) | 함수가 중첩된 경우, 그 **중첩된 함수의 바깥쪽 함수** 에서 정의된 변수 |
| G (Global)    | **모듈 (코드 파일) 전체** 에서 정의된 변수 (전역 변수)        |
| B (Built-in)  | Python 내장 함수 (```len``` 등), 객체             |

* Python에서 변수 이름을 참조할 때, 검색 순서는 **Local - Enclosing - Global - Built-in (LEGB)** 이다.
* 이름 간 충돌이 발생할 시, **위 규칙에 따라 가장 가까운 범위의 이름을 사용** 함 [(참고)](https://velog.io/@cheachea/%ED%8C%8C%EC%9D%B4%EC%8D%AC-LEGB-Rule)

## 5. map 함수와 reduce 함수

### 5-1. map 함수

* [3.4 람다 (lambda)](https://wikidocs.net/64)

람다 함수는 ```map(함수, iterable)``` 과 같이 사용한다.

* 예시

```python
>>> def first_divisor(x):
	divisor = 2
	while divisor <= x:
		if x % divisor == 0:
			return divisor
		divisor += 1
	return x

>>> years = range(2020, 2027)
>>> list(map(first_divisor, years))
[2, 43, 2, 7, 2, 3, 2]
```

### 5-2. reduce 함수

* [3.4 람다 (lambda)](https://wikidocs.net/64)

```python
>>> from functools import reduce
>>> companies = ['qara', 'kaier', 'motov', 'artistcompany']
>>> reduce(lambda x, y: f'{x}, {y}', companies)
'qara, kaier, motov, artistcompany'
>>> reduce(lambda x, y: f'{y}, {x}', companies)
'artistcompany, motov, kaier, qara'
```

* [Kotlin의 reduce 함수](https://github.com/WannaBeSuperteur/2022-Kotlin/blob/main/Kotlin%20Advanced/kotlin_advanced_reduce_fold.md) 와 유사한 컨셉이라고 할 수 있다.

## 6. 인자 (매개변수)

* [4.3 튜플](https://wikidocs.net/71)

다음과 같은 방법으로 함수에 인수 (매개변수) 를 추가할 수 있다. **(실무에서 많이 쓰이는 듯함)**

```python
def function(a, b, *rest):
```

* 예시

```python
>>> def function(a, b, *rest):
	print(a, b)
	print(rest)

	
>>> function(1, 2)
1 2
()
>>> function(1, 2, 3)
1 2
(3,)
>>> function(1, 2, 4, 8, 16, 32)
1 2
(4, 8, 16, 32)
```

위와 같은 경우, ```1, 2``` 다음에 들어오는 각 원소들이 튜플에 저장됨을 알 수 있다.

* ```function(1, 2)``` 의 경우, 빈 튜플 ```()``` 출력
* ```function(1, 2, 3)``` 의 경우, 튜플에 1개의 원소 ```3```이 들어가서 ```(3,)``` 출력
* ```function(1, 2, 4, 8, 16, 32)``` 의 경우, 튜플에 4개의 원소 ```4, 8, 16, 32```가 들어가서 ```(4, 8, 16, 32)``` 출력

## 7. 튜플 관련

### 7-1. 튜플과 리스트의 차이

* [4.3 튜플](https://wikidocs.net/71)

```python
>>> x = (1, 2)
>>> x[1]
2
>>> x[1] = 3
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x[1] = 3
TypeError: 'tuple' object does not support item assignment
```

|            | 튜플 (tuple)                   | 리스트 (list)                          |
|------------|------------------------------|-------------------------------------|
| 변화 가능성     | **변화 (값 변경 등) 불가능**          | **변화 가능**                           |
| 실무상 특징     | 절대로 바뀌지 않아야 하는 값 (설정값) 등에 사용 | 바뀔 수 있는 값에 사용                       |
| 컴퓨터 과학적 특징 | **필요한 양의 메모리** 만 정확히 할당      | **실제 데이터보다 큰 양의 메모리 (변동 가능하므로)** 할당 |

### 7-2. 튜플 관련 참고 사항

* 1개의 값을 튜플로 만들 때는 ```(value)``` **(단일 값으로 인식)** 와 같이 하지 않고 ```(value,)``` **(튜플로 인식)** 와 같이 해야 한다.

```python
>>> a = (10)
>>> a
10
>>> b = (10,)
>>> b
(10,)
```

## 8. dict 의 원소 (key, value pair) 출력 방법

* dict 의 원소를 출력할 때, ```(key, value)``` 형식의 튜플로 출력된다.

```python
>>> career = {'qara': '2022.01 - 2023.12', 'kaier': '2024.01 - 2025.01', 'motov': '2025.10 - 2026.01', 'artistcompany': '2026.03 -'}
>>> career.items()
dict_items([('qara', '2022.01 - 2023.12'), ('kaier', '2024.01 - 2025.01'), ('motov', '2025.10 - 2026.01'), ('artistcompany', '2026.03 -')])
```

## 9. set 관련 사항

### 9-1. set 의 교집합, 합집합, 차집합

| 구분  | 사용법                                                        |
|-----|------------------------------------------------------------|
| 교집합 | ```set1 & set2``` 또는 ```set.intersection(*list_of_sets)``` |
| 합집합 | ```set1 \| set2``` 또는 ```set.union(*list_of_sets)```       |
| 차집합 | ```set1 - set2```                                          |

```python
>>> ai_companies = {'kaier', 'necton', 'motov', 'artistcompany'}
>>> companies_in_resume = {'qara', 'kaier', 'motov', 'artistcompany'}
>>> ai_companies & companies_in_resume
{'artistcompany', 'kaier', 'motov'}
>>> ai_companies | companies_in_resume
{'necton', 'qara', 'artistcompany', 'kaier', 'motov'}
>>> ai_companies - companies_in_resume
{'necton'}
>>> list_of_companies = [ai_companies, companies_in_resume]
>>> set.intersection(*list_of_companies)
{'artistcompany', 'kaier', 'motov'}
>>> set.union(*list_of_companies)
{'necton', 'qara', 'artistcompany', 'kaier', 'motov'}
```

### 9-2. set, list의 membership test (존재 여부)

* 결론
  * set 의 membership test 가 시간이 훨씬 빠르다.
* 이유
  * list 의 membership test는 **list의 각 원소를 일일이 비교** 하기 때문에 $O(N)$ 의 시간이 소요된다.
  * set 의 membership test는 **해시 함수 (해시 테이블)** 방식을 이용하기 때문에 $O(1)$ 의 시간이 소요된다.

## 10. 모듈 (module) 관련

* 모듈 내에 있는 요소 (함수 등) 알아보기

```python
>>> import numpy as np
>>> dir(np)
['ALLOW_THREADS', 'AxisError', 'BUFSIZE', ..., 'who', 'zeros', 'zeros_like']
```

* 모듈 내에 있는 함수 사용법 알아보기

```python
>>> import math
>>> help(math.sqrt)
Help on built-in function sqrt in module math:

sqrt(x, /)
    Return the square root of x.
```

* ```importlib.import_module(name)``` 을 사용한 모듈 import

```python
>>> math.sqrt(2)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    math.sqrt(2)
NameError: name 'math' is not defined
>>> import importlib
>>> math = importlib.import_module('math')
>>> math.sqrt(2)
1.4142135623730951
```

## 11. string 모듈

```string``` 모듈에는 대문자 A-Z, 소문자 a-z, 숫자를 확인할 수 있는 함수가 있다.

```python
>>> import string
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
```

## 12. 날짜/시간 다루기

* 특정 날짜/시간 객체 생성

```python
>>> from datetime import datetime
>>> test = datetime(2026, 1, 2, 12, 45)
>>> test
datetime.datetime(2026, 1, 2, 12, 45)
>>> print(test)
2026-01-02 12:45:00
```

* 두 날짜/시간의 차이 계산

```python
>>> probation_start = datetime(2026, 3, 23, 9, 30)
>>> probation_finished = datetime(2026, 6, 22, 18, 30)
>>> probation_period = probation_finished - probation_start
>>> print(probation_period)
91 days, 9:00:00
```

* 이외에도 날짜/시간 관련해서 다음과 같은 다양한 함수들이 있다.

| 함수                                                               | 설명                                                       |
|------------------------------------------------------------------|----------------------------------------------------------|
| ```datetime.strptime(date_string, format)```                     | ```format```으로 된 ```date_string```을 날짜/시간 객체로 변환         |
| ```datetime_object.strftime(format)```                           | ```datetime_object``` 날짜/시간 객체를 ```format``` 형태의 문자열로 변환 |
| ```pytz.timezone('Asia/Seoul')``` + ```datetime.now(timezone)``` | ```Asia/Seoul``` timezone의 현재 시각 반환                      |
| ```timedelta(days)```                                            | ```days``` 일만큼을 더한 날짜 반환                                 |

## 13. 텍스트 파일 읽기/쓰기

* ```file = open(...)``` + ```file.close()``` 보다 ```with open(...)``` 를 사용해야 하는 이유
  * ```with open(...)``` 는 일종의 **컨텍스트 매니저** 역할로, 다음과 같은 효과가 있음
    * ```with``` 문을 빠져나가는 순간 자동으로 파일이 close 되기 때문에, **예외 상황, ```file.close()``` 를 깜빡하는 상황에서 파일이 제대로 닫히지 않는 것을 방지** 가능
    * 코드 가독성 향상
* 파일 열기 모드
  * write 는 **해당 내용으로 파일을 다시 쓰는 것** 이고, append 는 **해당 내용을 파일의 맨 끝부분에 추가하는 것** 이다. 
  * **바이트 형식** 으로 쓴다는 것은, **바이너리 파일 (텍스트가 아닌, 이미지 등 형식의 파일)** 을 쓰기 위한 저장 모드를 의미한다.  

| 파일 열기 모드                    | read | write          | append | 파일이 없을 때             |
|-----------------------------|------|----------------|--------|----------------------|
| ```open(file_path, 'r')```  | O    |                |        | FileNotFoundError 발생 |
| ```open(file_path, 'r+')``` | O    | O              |        | FileNotFoundError 발생 |
| ```open(file_path, 'w')```  |      | O              |        | 새로운 빈 파일 생성          |
| ```open(file_path, 'wb')``` |      | O **(바이트 형식)** |        | 새로운 빈 파일 생성          |
| ```open(file_path, 'w+')``` | O    | O              |        | 새로운 빈 파일 생성          |
| ```open(file_path, 'a')```  |      |                | O      | 새로운 빈 파일 생성          |
| ```open(file_path, 'a+')``` | O    |                | O      | 새로운 빈 파일 생성          |

## 14. pickle, glob

### 14-1. pickle

pickle 은 dict 등 비교적 복잡한 자료형을 파일 형태로 읽고 쓰기 위한 라이브러리이다.

```python
>>> career = {'qara': '2022.01 - 2023.12', 'kaier': '2024.01 - 2025.01', 'motov': '2025.10 - 2026.01', 'artistcompany': '2026.03 -'}
>>> import pickle
>>> with open('career', 'wb') as f:
	pickle.dump(career, f)

	
>>> import os
>>> os.path.exists('career')
True
>>> with open('career', 'rb') as f:
	print(pickle.load(f))

	
{'qara': '2022.01 - 2023.12', 'kaier': '2024.01 - 2025.01', 'motov': '2025.10 - 2026.01', 'artistcompany': '2026.03 -'}
```

### 14-2. glob

glob 은 파일의 경로명을 이용하여 파일 리스트를 추출하는 데 주로 사용되는 라이브러리이다.

```python
>>> from glob import glob
>>> glob('*.exe')
['python.exe', 'pythonw.exe']
>>> glob('*python*')
['python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe']
>>> glob(r'C:\U*')
['C:\\Users']
```

* 여기서 ```r```은 **원시 문자열 (raw)** 을 나타낸 것이다.
  * 원시 문자열이란, escape 를 위한 백슬래시를 별도로 해석하지 않고 **그대로의 텍스트로 간주** 한다는 것이다.

## 15. del, repr, add, lt 메서드

* 각각의 메서드는 다음과 같은 의미를 갖는다.

| 메서드            | 설명                                                             |
|----------------|----------------------------------------------------------------|
| ```__del__```  | 객체가 소멸될 때 (del) 실행                                             |
| ```__repr__``` | ```print(instance)``` 를 실행할 때, ```instance```에 대한 동작을 나타내는 메서드 |
| ```__add__```  | ```instance1 + instance2``` 를 실행할 때의 결과를 반환하는 메서드              |
| ```__lt__```   | 2개의 객체 간 비교 결과 반환 **(1번째 객체가 2번째 객체보다 '작을' 조건에 대한 논리식)**       |

```python
>>> class Company:
	def __init__(self, name, months):
		self.name = name
		self.months = months
	def __repr__(self):
		return f'회사 이름: {self.name}, 재직 기간: {self.months}개월'
	def __add__(self, other):
		return 30 * self.months + 30 * other.months
	def __lt__(self, other):
		return self.months < other.months

	
>>> kaier = Company(name='Kaier', months=13)
>>> motov = Company(name='MOTOV', months=4)
>>> print(kaier)
회사 이름: Kaier, 재직 기간: 13개월
>>> print(motov)
회사 이름: MOTOV, 재직 기간: 4개월
>>> kaier + motov
510
>>> kaier < motov
False
>>> kaier > motov
True
```

## 16. 프로그램 실행 시간 측정하기

* Python 코드 실행 시, **실제로 걸린 시간 (wall time)** 이 아닌 **컴퓨터의 처리 시간 (process time)** 을 측정해야 할 수 있다.
  * process time은 **CPU가 실제로 동작한 데 걸린 시간** 을 의미한다.

```python
>>> from time import process_time
>>> start = process_time()
>>> a = 0
>>> while a < 1000000:
	a += 1

	
>>> end = process_time()
>>> end - start
0.078125
>>> start
3.5625
>>> end
3.640625
```

* ```time``` 모듈의 ```process_time``` 함수는 **Python 코드의 연산 시간** 만을 측정하는 함수이다.

## 17. 파이썬으로 데이터베이스 다루기

* Python으로 다룰 수 있는 대표적인 데이터베이스 (DB) 는 다음과 같다.

| DB                | 설명           | 특징                  | 적절한 상황                       |
|-------------------|--------------|---------------------|------------------------------|
| SQLite            | 파일형 DB       | 설치 없이 Python 내장     | 모바일 앱, 소규모 프로젝트              |
| PostgreSQL, MySQL | 관계형/서버형 DB   | 백업, 보안, 성능 등 안정적    | 실제 서비스 (production)          |
| MongoDB           | NoSQL 문서형 DB | 테이블 구조 미리 정의 불필요    | 비정형 데이터 (데이터 구조가 자주 바뀔 수 있음) |
| Redis             | key-value 형태 | read/write 속도 매우 빠름 | 채팅, 캐시, 실시간 변동되는 데이터 등       |

* NOSQL은 **Not Only SQL** 로, **관계형이 아닌 테이블 형식의 DB** 를 의미한다.


