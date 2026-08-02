
## 목차

* [1. 컴프리헨션/제너레이터 표현식 적용 리팩토링](#1-컴프리헨션제너레이터-표현식-적용-리팩토링)
  * [1-1. 중첩 컴프리헨션](#1-1-중첩-컴프리헨션)
* [2. 튜플 언패킹](#2-튜플-언패킹)
* [3. 중복된 로직의 제거](#3-중복된-로직의-제거)
* [4. 조건문 블록 단순화](#4-조건문-블록-단순화)
* [5. ```match-case``` 문을 사용한 리팩토링](#5-match-case-문을-사용한-리팩토링)
* [6. 긴 함수의 분리 (제너레이터, 컨텍스트 매니저)](#6-긴-함수의-분리-제너레이터-컨텍스트-매니저)
* [7. 기타](#7-기타)

## 1. 컴프리헨션/제너레이터 표현식 적용 리팩토링

* 소수 중에서 일의 자리가 7인 것의 합 구하기 (제너레이터 표현식 적용)

```python
# old (not Pythonic)
>>> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
>>> def old_sum_sevens(primes: list) -> list:
	result = 0
	for p in primes:
		if p % 10 == 7:
			result += p
	return result

# new (Pythonic)
>>> def new_sum_sevens(primes: list) -> list:
	return sum(p for p in primes if p % 10 == 7)

>>> print(old_sum_sevens(primes))
61
>>> print(new_sum_sevens(primes))
61
```

* 소수 중에서 일의 자리가 7인 것의 제곱의 리스트 구하기 (list comprehension 적용)

```python
>>> def old_square_sevens(primes: list) -> list:
	result = []
	for p in primes:
		if p % 10 == 7:
			result.append(p * p)
	return result

>>> def new_square_sevens(primes: list) -> list:
	return [p * p for p in primes if p % 10 == 7]

>>> print(old_square_sevens(primes))
[49, 289, 1369]
>>> print(new_square_sevens(primes))
[49, 289, 1369]
```

* 회사 이름에 'n' 포함 여부를 mapping 시키는 딕셔너리 만들기 (dict comprehension 적용)

```python
>>> companies = ['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> def old_is_n_map(names: list) -> dict:
	result: dict = {}
	for name in names:
		result[name] = 'n' in name
	return result

>>> def new_is_n_map(names: list) -> dict:
	return {name: 'n' in name for name in names}

>>> print(old_is_n_map(companies))
{'qara': False, 'kaier': False, 'motov': False, 'artistcompany': True, 'rainbow8': True}
>>> print(new_is_n_map(companies))
{'qara': False, 'kaier': False, 'motov': False, 'artistcompany': True, 'rainbow8': True}
```

### 1-1. 중첩 컴프리헨션

* 모든 ```소수```월 ```소수```일 구하기 (단, ```일```은 28일까지만 있음)

```python
>>> def old_prime_md(months: list, days: list) -> list:
	mds: list = []
	for m in months:
		for d in days:
			if m <= 12 and d <= 28:
				mds.append((m, d))
	return mds

>>> def new_prime_md(months: list, days: list) -> list:
	return [(m, d) for m in months for d in days
		if m <= 12 and d <= 28]

>>> print(old_prime_md(months=primes, days=primes))
[(2, 2), (2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (2, 19), (2, 23), (3, 2), (3, 3), (3, 5), (3, 7), (3, 11), (3, 13), (3, 17), (3, 19), (3, 23), (5, 2), (5, 3), (5, 5), (5, 7), (5, 11), (5, 13), (5, 17), (5, 19), (5, 23), (7, 2), (7, 3), (7, 5), (7, 7), (7, 11), (7, 13), (7, 17), (7, 19), (7, 23), (11, 2), (11, 3), (11, 5), (11, 7), (11, 11), (11, 13), (11, 17), (11, 19), (11, 23)]
>>> print(new_prime_md(months=primes, days=primes))
[(2, 2), (2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (2, 19), (2, 23), (3, 2), (3, 3), (3, 5), (3, 7), (3, 11), (3, 13), (3, 17), (3, 19), (3, 23), (5, 2), (5, 3), (5, 5), (5, 7), (5, 11), (5, 13), (5, 17), (5, 19), (5, 23), (7, 2), (7, 3), (7, 5), (7, 7), (7, 11), (7, 13), (7, 17), (7, 19), (7, 23), (11, 2), (11, 3), (11, 5), (11, 7), (11, 11), (11, 13), (11, 17), (11, 19), (11, 23)]
```

## 2. 튜플 언패킹

* 각 회사의 재직 개월 수 출력

```python
>>> career = [{'qara': 24}, {'kaier': 12}, {'motov': 3}, {'artistcompany': 6}, {'rainbow8': 2}]
>>> career = [('qara', 24), ('kaier', 12), ('motov', 3), ('artistcompany', 6), ('rainbow8', 2)]
>>> def old_unpack(career: list):
	for c in career:
		name = c[0]
		months = c[1]
		print(f'{name} ({months} 개월 재직)')

		
>>> def new_unpack(career: list):
	for name, months in career:
		print(f'{name} ({months} 개월 재직)')

		
>>> old_unpack(career)
qara (24 개월 재직)
kaier (12 개월 재직)
motov (3 개월 재직)
artistcompany (6 개월 재직)
rainbow8 (2 개월 재직)
>>> new_unpack(career)
qara (24 개월 재직)
kaier (12 개월 재직)
motov (3 개월 재직)
artistcompany (6 개월 재직)
rainbow8 (2 개월 재직)
```

## 3. 중복된 로직의 제거

* 중복되는 로직 (공통부분) 의 경우 **따로 함수로 추출** 해야 한다.
  * 전처리, 검증 등
* 고차 함수 (HOF) 를 이용한 전략 주입
  * 로직의 공통되는 부분을 한 곳으로 모으고, **차이가 있는 부분을 따로 정책 함수로 주입** 한다.
  * ```partial``` 을 활용하면 **인자를 미리 고정한 '준비된 함수'** 를 생성할 수 있다.

```python
# NOT Pythonic

>>> def compute_formula_1(x: float, y: float) -> float:
	return x + y * (y + 1.0) * (y + 2.0) / 6.0

>>> def compute_formula_2(x: float, y: float) -> float:
	return x + y * (y + 4.0) * (y - 5.0) / 6.0

>>> print(compute_formula_1(4.5, 3))
14.5
>>> print(compute_formula_2(5, 4))
-0.33333333333333304
```

```python
# Pythonic !!

>>> from typing import Callable
>>> from functools import partial

# 정책 함수 정의
>>> PolicyFunction = Callable[[float], float]

# 공통 계산 로직을 모으고, 차이가 있는 부분만 convert 함수를 사용 (고차 함수)
>>> def compute_formula(x: float, y: float, convert: PolicyFunction) -> float:
	return x + y * convert(y) / 6.0

>>> def convert(a: float, b: float) -> PolicyFunction:
	return lambda y: (y + a) * (y + b)

# 정책 함수 convert 의 구체적 구현
# convert_formula_1: lambda y: (y + 1.0) * (y + 2.0)
# convert_formula_2: lambda y: (y + 4.0) * (y - 5.0)
>>> convert_formula_1 = convert(a=1.0, b=2.0)
>>> convert_formula_2 = convert(a=4.0, b=-5.0)

# partial 을 이용해 인자를 미리 고정한 "준비된 함수" 생성
>>> compute_formula_1_new = partial(compute_formula, convert=convert_formula_1)
>>> compute_formula_2_new = partial(compute_formula, convert=convert_formula_2)

# 함수 실행 (리팩토링 이전과 결과 동일)
>>> print(compute_formula_1_new(4.5, 3))
14.5
>>> print(compute_formula_2_new(5, 4))
-0.33333333333333304
```

## 4. 조건문 블록 단순화

* 숫자 연산 블럭을 ```if-elif-else``` 구조에서 dict 를 이용하여 보다 단순화할 수 있다.
* **Callable** 은 **함수에 대한 Type** 으로, 다음과 같이 구성된다.
  * ```Callable[[arg1 type, arg2 type, ...], return type]``` 

```python
>>> from __future__ import annotations

# NOT Pythonic
>>> def aggr_if(op: str, xs: list[float]) -> float:
	if op == 'sum':
		return sum(xs)
	elif op == 'avg':
		return sum(xs) / len(xs)
	elif op == 'cnt':
		return len(xs)
	elif op == 'maxmmin':
		return max(xs) - min(xs)
	else:
		return None

## Pythonic !!
>>> from typing import Callable
>>> def aggr_map(op: str, xs: list[float]) -> float:
	ops: dict[str, Callable[[float], float]] = {
		"sum": lambda xs: sum(xs),
		"avg": lambda xs: sum(xs) / len(xs),
		"cnt": lambda xs: len(xs),
		"maxmmin": lambda xs: max(xs) - min(xs),
	}
	return ops.get(op, lambda *_: None)(xs)

>>> aggr_if('avg', [3, 2, 5])
3.3333333333333335
>>> aggr_map('avg', [3, 2, 5])
3.3333333333333335
```

* 함수를 dictionary 형태로 매핑하기

```python
>>> import os
>>> def cmd_listdir() -> str:
	return str(os.listdir())

>>> def cmd_test() -> str:
	return "test successful"

>>> def cmd_version() -> str:
	return "v1.2.6"

>>> COMMANDS: dict[str, Callable[[], str]] = {
	"listdir": cmd_listdir,
	"test": cmd_test,
	"version": cmd_version
}
>>> def dispatch_command(cmd: str) -> str:
	return COMMANDS.get(cmd, lambda: f"unknown command: {cmd}")()
```

```python
>>> dispatch_command("listdir")
"['career', 'dddd', 'DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']"
>>> dispatch_command("test")
'test successful'
>>> dispatch_command("version")
'v1.2.6'
```

* 팩토리 패턴

```python
>>> from dataclasses import dataclass
>>> @dataclass
class Hero:
	kind: str
	name: str
	gender: Literal["male", "female"]
	height: float

	
>>> def make_superman(height: float) -> Hero:
	return Hero("person", "Superman", "male", height)

>>> def make_candy_girl(name: str, height: float) -> Hero:
	return Hero("candy", name, "female", height)

>>> FACTORY: dict[str, Callable[..., Hero]] = {
	"superman": make_superman,
	"candy_girl": make_candy_girl,
}
>>> def create_hero(kind: str, *args) -> Hero:
	if kind not in FACTORY:
		raise ValueError("this kind of hero is not supported")
	return FACTORY[kind](*args)
```

```python
>>> s = create_hero("superman", 4.45)
>>> print(s)
Hero(kind='person', name='Superman', gender='male', height=4.45)
>>> c = create_hero("candy_girl", "Lumi", 0.15)
>>> print(c)
Hero(kind='candy', name='Lumi', gender='female', height=0.15)
```

## 5. ```match-case``` 문을 사용한 리팩토링

```match-case``` 는 **Python 3.10+** 에서 제공하는 문법으로, **튜플, 딕셔너리, 클래스 구조 분기** 에 유용하다.

* 문법은 다음과 같다.
  * ```value``` 가 각각의 ```condition_{c}``` 을 만족시키면 해당 부분이 실행된다.

```python
match (value)
    case (condition_1):  # value 가 condition 인 경우
        blahblah ...
    case (condition_2):
        blahblah ...
...
```

## 6. 긴 함수의 분리 (제너레이터, 컨텍스트 매니저)

* 기존 함수의 문제점
  * **너무 긴 함수**, 흐름을 한눈에 이해하기가 어려움
    * **단일 책임 원칙** 준수 미비 
  * 컨텍스트 매니저 (```with```) 미 사용으로, **파일, 자원 등의 수명이 안전하게 관리되지 않음**
* 해결 방법
  * **제너레이터 파이프라인** 이용 (파일 처리의 각 단계를 ```yield``` 를 이용한 반환으로 변경)
  * ```ExitStack``` 을 통해 파일을 한번에 관리



## 7. 기타

* FSM (상태 기계) 패턴의 경우에는, **```if-elif-else``` 구조 대신 전이 테이블을 이용한다.**
  * 이때 전이 테이블은 ```dict[tuple[State, Event], State]``` 형태로 만들 수 있다.
