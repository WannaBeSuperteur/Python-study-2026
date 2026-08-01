## 목차

* [1. 파이썬의 기본 철학 및 핵심 격언](#1-파이썬의-기본-철학-및-핵심-격언)
* [2. 컴프리헨션 (Comprehension)](#2-컴프리헨션-comprehension)
  * [2-1. 제너레이터 표현식 사용](#2-1-제너레이터-표현식-사용)

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
