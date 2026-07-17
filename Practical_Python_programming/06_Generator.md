
## 목차

* [1. 제너레이터와 yield 문](#1-제너레이터와-yield-문)
* [2. 제너레이터를 이용한 생산자/소비자 파이프라인](#2-제너레이터를-이용한-생산자소비자-파이프라인)
* [3. 제너레이터를 사용하는 이유](#3-제너레이터를-사용하는-이유)
* [4. itertools 모듈](#4-itertools-모듈)
  * [4-1. itertools.chain 사용 예시](#4-1-itertoolschain-사용-예시)
  * [4-2. itertools.count 사용 예시](#4-2-itertoolscount-사용-예시)
  * [4-3. itertools.groupby 사용 예시](#4-3-itertoolsgroupby-사용-예시)
  * [4-4. itertools.tee 사용 예시](#4-4-itertoolstee-사용-예시)

## 1. 제너레이터와 yield 문

* **제너레이터 (Generator)** 는 일반 함수와 같이 다르게, 다음과 같이 동작한다.

```
1. 제너레이터 함수 호출 시, 제너레이터 객체 생성 (중요: 함수가 즉시 실행되지 않음)
   x = generator_function(arg0, ...) 형태로 제너레이터 객체를 생성한다.
2. 제너레이터 객체에서 __next__() 호출을 하면 함수가 실행된다.
3. 함수에서 'yield {value}' 에 도달하면, {value} 에 해당하는 값을 출력하고 함수가 "일시 정지" 한다.
   다음 __next__() 호출 시 함수가 실행된다.
```

* 참고로 ```__next__()``` 함수에 의해서 yield 되는 값은 ```generator_return = generator.__next__()``` 처럼 할당이 가능하다.

```python
>>> company = ['qara', 'kaier', 'motov', 'artistcompany']
>>> def print_company(company):
	print('=== MY CAREER ===')
	for c in company:
		print('next company:')
		yield c

		
>>> generator_object = print_company(company)
>>> generator_object.__next__()
=== MY CAREER ===
next company:
'qara'
>>> generator_object.__next__()
next company:
'kaier'
>>> generator_object_return = generator_object.__next__()
next company:
>>> print(generator_object_return)
motov
>>> generator_object_return = generator_object.__next__()
next company:
>>> print(generator_object_return)
artistcompany
>>> generator_object.__next__()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    generator_object.__next__()
StopIteration
```

## 2. 제너레이터를 이용한 생산자/소비자 파이프라인

* 제너레이터를 이용하면 **생산자/소비자 파이프라인** 을 만들 수 있다.

```python
>>> def producer():
	value = 0
	while True:
		value += 1
		print(f"producer : {value}")
		yield value

		
>>> def processing(s):
	for item in s:
		item_processed = f"===[ {item} ]==="
		print(f"processing : {item_processed}")
		yield item_processed

		
>>> def consumer(s):
	for item in s:
		print(f"consume: {item}")
```

```python
>>> prod = producer()
>>> proc = processing(prod)
>>> con = consumer(proc)

# con (consumer) 가 proc (processor) 에게 for item in s: 를 통해 값을 요청 (__next__() 역할)
# proc (processor) 가 prod (producer) 에게 for item in s: 를 통해 값을 요청 (__next__() 역할)
# prod (producer) 로 최종 요청이 전달되어, prod 는 값을 yield

producer : 1              # 1 이라는 값을 생산
processing : ===[ 1 ]===  # prod 가 yield한 1이라는 값이 item이 되므로, 이를 process 한 후 yield 함 
consume: ===[ 1 ]===      # proc 가 yield한 '===[ 1 ]==='이라는 값이 item 이 되므로, 이를 출력
producer : 2              # producer 가 while True: 이므로 무한 반복 생산
processing : ===[ 2 ]===
consume: ===[ 2 ]===
producer : 3
processing : ===[ 3 ]===
consume: ===[ 3 ]===
producer : 4
processing : ===[ 4 ]===
```

## 3. 제너레이터를 사용하는 이유

* 필요할 때만 값을 생산할 수 있음
* 메모리를 더 효율적으로 사용할 수 있음
* 스트리밍 (streaming) 데이터를 다루는 등 응용 가능

## 4. itertools 모듈

Python의 ```itertools``` 는 iterator, generator 사용을 보조하는 다양한 함수를 포함하는 모듈이다.

| 함수                                          | 함수 설명                                                      |
|---------------------------------------------|------------------------------------------------------------|
| ```itertools.chain(s1, s2, ...)```          | 여러 개의 리스트를 하나로 합치기                                         |
| ```itertools.count(n)```                    | ```x.__next__()``` 호출 시 ```n```, ```n+1```, ```n+2``` 를 반환 |
| ```itertools.cycle(s)```                    |                                                            |
| ```itertools.dropwhile(predicate, s)```     |                                                            |
| ```itertools.groupby(s)```                  | 특정 key 값을 기준으로 **데이터를 여러 그룹으로 묶기**                         |
| ```itertools.ifilter(predicate, s)```       |                                                            |
| ```itertools.imap(function, s1, ..., sN)``` |                                                            |
| ```itertools.repeat(s, n)```                |                                                            |
| ```itertools.tee(s, ncopies)```             | iterable ```s``` 를 ```ncopies``` 개 생성                      |
| ```itertools.izip(s1, ..., sN)```           |                                                            |

### 4-1. itertools.chain 사용 예시

```python
>>> from itertools import chain
>>> value = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
>>> list(chain(*value))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> value1 = [['a', 'b', 'c', 'd']]
>>> list(chain(*value, *value1))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd']
```

### 4-2. itertools.count 사용 예시

```python
>>> a = itertools.count(100)
>>> a
count(100)
>>> a.__next__()
100
>>> a.__next__()
101
>>> a.__next__()
102
```

### 4-3. itertools.groupby 사용 예시

* groupby 를 사용할 때, **데이터가 반드시 그룹으로 묶을 key 값을 기준으로 정렬** 되어 있어야 한다.
* ```operator.itemgetter``` 는 **dict의 list 에서, dict의 원하는 key 값을 기준으로 함** 을 의미한다.
* ```pprint.pprint``` 를 이용하여 **예쁘게 print** 할 수 있다.

```python
>>> from itertools import groupby
>>> import operator
>>> data = [
	{'name': '김시용', 'months': 3, 'is_probation': True},
	{'name': '김정규', 'months': 4, 'is_probation': False},
	{'name': '김계약', 'months': 1, 'is_probation': False},
	{'name': '이계약', 'months': 12, 'is_probation': False},
	{'name': '박연장', 'months': 6, 'is_probation': True}
]

# itertools.groupby 를 사용하기 위해서는 데이터가 반드시 정렬되어 있어야 함!!
>>> data = sorted(data, key=operator.itemgetter('is_probation'))

>>> import pprint
>>> pprint.pprint(data)
[{'is_probation': False, 'months': 4, 'name': '김정규'},
 {'is_probation': False, 'months': 1, 'name': '김계약'},
 {'is_probation': False, 'months': 12, 'name': '이계약'},
 {'is_probation': True, 'months': 3, 'name': '김시용'},
 {'is_probation': True, 'months': 6, 'name': '박연장'}]

>>> grouped_data = itertools.groupby(data, key=operator.itemgetter('is_probation'))
>>> for key, group_data in grouped_data:
	print(key, list(group_data))

	
False [{'name': '김정규', 'months': 4, 'is_probation': False}, {'name': '김계약', 'months': 1, 'is_probation': False}, {'name': '이계약', 'months': 12, 'is_probation': False}]
True [{'name': '김시용', 'months': 3, 'is_probation': True}, {'name': '박연장', 'months': 6, 'is_probation': True}]
```

### 4-4. itertools.tee 사용 예시

```python
from itertools import tee
>>> a, b, c = tee([1, 4, 9, 16], 3)
>>> a
<itertools._tee object at 0x0000020798B5DDC0>
>>> b
<itertools._tee object at 0x0000020798B5B200>
>>> c
<itertools._tee object at 0x0000020798B54180>
>>> list(a)
[1, 4, 9, 16]
>>> list(b)
[1, 4, 9, 16]
>>> list(c)
[1, 4, 9, 16]
```

