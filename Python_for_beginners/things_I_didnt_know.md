
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
