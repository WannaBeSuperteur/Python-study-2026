## 목차

* [1. 파이썬의 기본 철학 및 핵심 격언](#1-파이썬의-기본-철학-및-핵심-격언)
* [2. 컴프리헨션 (Comprehension)](#2-컴프리헨션-comprehension)
  * [2-1. 제너레이터 표현식 사용](#2-1-제너레이터-표현식-사용)
  * [2-2. 리스트 컴프리헨션 vs. 제너레이터 표현식](#2-2-리스트-컴프리헨션-vs-제너레이터-표현식)
* [3. any(), all() 함수 (조건문 중첩 대신)](#3-any-all-함수-조건문-중첩-대신)
* [4. zip(seq1, seq2, ...) 관련](#4-zipseq1-seq2--관련)
* [5. 언패킹](#5-언패킹)
  * [5-1. 기본 언패킹](#5-1-기본-언패킹) 
  * [5-2. 별표 (*) 언패킹](#5-2-별표--언패킹) 
* [6. 컨텍스트 매니저 관련](#6-컨텍스트-매니저-관련)
* [7. 기타](#7-기타)

## 1. 파이썬의 기본 철학 및 핵심 격언

* Python의 기본 철학 및 핵심 격언은 다음과 같다.

| 철학/격언                   | 적용 예시                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------|
| **아름다움** 이 추함보다 낫다      | 문자열 연결 대신 **f-string** 사용                                                                                    |
| **단순함** 이 복잡함보다 낫다      | 중첩 if문 대신 **dict** 사용                                                                                        |
| 오류는 **숨기지 말라**          | **예외 처리 방식 (EAFP)** 의 채택                                                                                     |
| **오직 한 가지의 명확한** 방법     | 포맷팅 방식 등은 **1가지로 통일**                                                                                        |
| **성긴 (sparse 한)** 것이 낫다 | [제너레이터 형식 포맷](../Python_Clean_Code_2nd_Edition/07_Generator_Iterator_Async.md##1-2-제너레이터-표현식), 줄 바꿈 등 적절히 활용 |
| **설명 가능한** 구현           | 명확한 **변수명, 흐름, 함수 분리** 등                                                                                     |

## 2. 컴프리헨션 (Comprehension)

**컴프리헨션 (Comprehension)** 은 [컬렉션 자료형 중 리스트, 딕셔너리, 세트](01_Python_Basics.md#1-리스트-튜플-딕셔너리-세트) 에 대해 **for 반복문을 간소화** 하기 위한 것이다.

| 컴프리헨션 형태                                  | 설명                                                                                      |
|-------------------------------------------|-----------------------------------------------------------------------------------------|
| ```[func for x in xs]```                  | 컬렉션 자료형 ```xs``` 의 각 원소 ```x``` 에 대해 ```func``` 를 적용한 결과                                |
| ```[func for x in xs if condition]```     | 컬렉션 자료형 ```xs``` 의 각 원소 ```x``` 에 대해 ```func``` 를 적용한 결과 **(단, ```condition``` 조건 만족)** |
| ```[A if condition else B for x in xs]``` | 컬렉션 자료형 ```xs``` 의 각 원소 ```x``` 에 대해 **조건 분기를 적용**                                      |

```python
>>> companies = ['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> [company[0] for company in companies]
['q', 'k', 'm', 'a', 'r']
>>> [company[0] for company in companies if 'n' in company]
['a', 'r']
>>> ['N' if 'n' in company else 'not N' for company in companies]
['not N', 'not N', 'not N', 'N', 'N']
```

### 2-1. 제너레이터 표현식 사용

* 다음과 같이 **제너레이터 표현식** 을 사용하면 **메모리를 절약** 할 수 있다.

```python
>>> primes = [2, 3, 5, 7, 11, 13, 17, 19]
>>> sum(p for p in primes if p >= 10)
60
>>> max(p for p in primes if p % 3 == 2)
17
>>> min(p for p in primes if p % 3 == 1)
7
>>> all(p % 2 == 1 for p in primes)
False
>>> any(p % 2 == 1 for p in primes)
True

# 참고:
#>>> [p % 2 == 1 for p in primes]
#[False, True, True, True, True, True, True, True]
```

```python
# anti-pattern
# 제너레이터 표현식 미 사용 -> 깔끔하지 못하고 메모리 절약 안됨

>>> sum([p for p in primes if p >= 10])
60
>>> max([p for p in primes if p % 3 == 2])
17
>>> min([p for p in primes if p % 3 == 1])
7
>>> all([p % 2 == 1 for p in primes])
False
>>> any([p % 2 == 1 for p in primes])
True
```

### 2-2. 리스트 컴프리헨션 vs. 제너레이터 표현식

| 구분     | 리스트 컴프리헨션              | 제너레이터 표현식            |
|--------|------------------------|----------------------|
| 메모리 저장 | 처음부터 **모든 값을 메모리에 저장** | 값을 **필요할 때 즉석에서 생성** |
| 메모리 절약 | X                      | O                    |

* 제너레이터는 **대규모 데이터, 반복이 중간에 멈추기 쉬운 경우** 등에 사용하는 것이 좋다.

## 3. any(), all() 함수 (조건문 중첩 대신)

* 함수 설명

| 함수 및 기타 사용법                 | 설명                                                         |
|-----------------------------|------------------------------------------------------------|
| ```any(iterable)```         | ```iterable``` 의 논리식 중 1개라도 True이면 ```True```를 반환 **(OR)** |
| ```all(iterable)```         | ```iterable``` 의 논리식이 모두 True이면 ```True```를 반환 **(AND)**   |
| ```A if condition else B``` | 삼항 연산자 **보다 Pythonic 한 표현**                                |

```python
>>> def get_probation_result(performance: int, competency: int, attitude: int) -> bool:
	avg = (performance + competency + attitude) / 3
	if avg < 60:
		return False
	elif attitude < 40:
		return False
	elif competency < 60 and attitude < 60:
		return False
	else:
		return True

	
>>> def get_probation_result_new(performance: int, competency: int, attitude: int) -> bool:
	avg = (performance + competency + attitude) / 3
	return not any((   # must be '((' and '))', not '(' and ')'
		avg < 60,
		attitude < 40,
		competency < 60 and attitude < 60
	))
```

```python
>>> x, y = 10, 12
>>> all([x % 3 == 0, y % 2 == 0])
False
>>> any([x % 3 == 0, y % 2 == 0])
True
```

## 4. zip(seq1, seq2, ...) 관련

```itertools.zip_longest``` 는 **길이가 서로 다른 iterable을 끝까지 처리** 하기 위한 방법이다.

| 구분  | 설명                                                                                                                                                         |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 사용법 | ```zip_longest(iter1, iter2, ..., fillvalue=fillvalue)```                                                                                                  |
| 기능  | ```iter1```, ```iter2``` 중 **가장 긴 (원소 개수가 가장 많은) iterable** 에 맞춰서, 나머지 iterable에 해당하는 부분을 ```fillvalue``` 로 채운다.<br>- ```fillvalue``` 의 기본값은 ```None```이다. |

```python
>>> companies = ['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> months = [24, 12, 3]
>>> for c, m in zip(companies, months):
	print(c, m)

	
qara 24
kaier 12
motov 3
```

```python
>>> for c, m in zip_longest(companies, months):
	print(c, m)

	
qara 24
kaier 12
motov 3
artistcompany None
rainbow8 None
```

## 5. 언패킹

* iterable 데이터를 풀 때는 **언패킹을 이용하는 것이 파이써닉** 하다.

### 5-1. 기본 언패킹

```python
# NOT pythonic

>>> companies = ['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> first_company = companies[0]
>>> second_company = companies[1]
>>> first_company
'qara'
>>> second_company
'kaier'
```

```python
# Pythonic !!

>>> first_company, second_company = companies[:2]
>>> first_company
'qara'
>>> second_company
'kaier'
```

### 5-2. 별표 (*) 언패킹

* 별표 ```*``` 를 이용하여 **나머지 전부를 언패킹** 할 수 있다.

```python
>>> companies = ['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> first, *rest = companies
>>> first
'qara'
>>> rest
['kaier', 'motov', 'artistcompany', 'rainbow8']
```

## 6. 컨텍스트 매니저 관련

* ```with open(...)``` 과 같이 **컨텍스트 매니저** 를 사용하면, 블록 종료 시 자동으로 ```close()``` 가 호출되므로 **예외 발생 시에도 안전하게 정리** 된다.
* 컨텍스트 매니저 관련 라이브러리 ```contextlib``` 의 함수

| 함수                         | 설명                                                     |
|----------------------------|--------------------------------------------------------|
| ```contextlib.suppress```  | ```with supress(OOOException):``` 과 같이 하여 **특정 예외 무시** |
| ```contextlib.ExitStack``` | ```with``` 로 표현된 **여러 개의 자원을 한번에 관리**                  |

```python
>>> from contextlib import suppress
>>> with suppress(ZeroDivisionError):
	test = 1 / 0

	
>>> 
```

## 7. 기타

* 가독성 향상을 위해 **조건을 집합처럼 사용** 하는 것이 좋다.

```python
>>> eval_metric = 'accuracy'
>>> if eval_metric in {'accuracy', 'precision', 'recall', 'f1', 'auroc', 'prauc'}:
	print(f'{eval_metric} is a valid metric.')

	
accuracy is a valid metric.
```

* 위치 전용 인자
  * 함수 정의 시 ```def func(a: int, /, ...)``` 와 같이 하면 ```a```는 **키워드로 넣으면 안 되고, 위치로만 넣어야** 한다.

```python
>>> def square(num: int, /):
	return num * num

>>> square(5)
25
>>> square(num=5)
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    square(num=5)
TypeError: square() got some positional-only arguments passed as keyword arguments: 'num'
```
