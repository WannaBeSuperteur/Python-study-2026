## 목차

* [1. 튜플 관련](#1-튜플-관련)
* [2. 포매팅 된 string (f-string)](#2-포매팅-된-string-f-string)
* [3. 주의 사항: for, len, range 동시 사용한 Pythonic 하지 않은 코드](#3-주의-사항-for-len-range-동시-사용한-pythonic-하지-않은-코드)
* [4. Collections 모듈](#4-collections-모듈)
  * [4-1. Counter](#4-1-counter)
  * [4-2. DefaultDict](#4-2-defaultdict)
* [5. 리스트 컴프리헨션 (list comprehension)](#5-리스트-컴프리헨션-list-comprehension)
* [6. 객체와 복사](#6-객체와-복사)
  * [6-1. 객체 ID와 레퍼런스](#6-1-객체-id와-레퍼런스)
  * [6-2. 얕은 복사 (shallow copy) 와 깊은 복사 (deep copy)](#6-2-얕은-복사-shallow-copy-와-깊은-복사-deep-copy)

## 1. 튜플 관련

* 튜플을 만들 때는 기본적으로 ```()``` 를 쓰지만, 이 괄호를 **생략할 때도 있음**

```python
>>> company = 'artist', 'company'
>>> company
('artist', 'company')
```

* 빈 튜플, 항목이 1개 있는 튜플 만들기

| 빈 튜플                   | 항목이 1개 있는 튜플                          |
|------------------------|---------------------------------------|
| ```empty_tuple = ()``` | ```only_one_item_tuple = ('item',)``` |

## 2. 포매팅 된 string (f-string)

* Python의 f-string의 포맷 코드에서 **필드 폭과 정밀도를 조정** 하기 위해서는 다음과 같이 한다.

| 수정자           | 설명                                             |
|---------------|------------------------------------------------|
| ```:>{n}d```  | 정수 (```d```) 를 ```{n}``` 자리 필드 기준으로 **오른쪽 정렬** |
| ```:<{n}d```  | 정수 (```d```) 를 ```{n}``` 자리 필드 기준으로 **왼쪽 정렬**  |
| ```:^{n}d```  | 정수 (```d```) 를 ```{n}``` 자리 필드 기준으로 **가운데 정렬** |
| ```:0.{n}f``` | 부동 소수점 소수 (```f```) 를 ```{n}``` 저리 정밀도로 나타냄    |

* format 메서드 사용 방법: **인자, 키워드 인자 등 포매팅 가능**

```python
>>> '{test:4d} {test2:6d} {test3:0.2f}'.format(test=1, test2=234, test3=56)
'   1    234 56.00'
```

* C언어 스타일로도 포매팅할 수 있다.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %05d' % (100, 234)
'  100 00234'
>>> '<<<%0.2f>>>' % 3.14159
'<<<3.14>>>'
```

## 3. 주의 사항: for, len, range 동시 사용한 Pythonic 하지 않은 코드

* NOT GOOD

```python
>>> company = ['qara', 'kaier', 'motov', 'artistcompany']
>>> for i in range(len(company)):
	print(company[i])

	
qara
kaier
motov
artistcompany
```

* index가 꼭 필요할 때는 다음과 같이 사용

```python
>>> for i, c in enumerate(company):
	print(c)

	
qara
kaier
motov
artistcompany
```

* index가 불필요할 때

```python
>>> for c in company:
	print(c)

	
qara
kaier
motov
artistcompany
```

## 4. Collections 모듈

### 4-1. Counter

* import 방법

```python
from collections import Counter
```

* 사용 방법
  * Counter 를 이용하면, **hashable item (해시 테이블의 key로 사용 가능한 형태의 item)** 들에 대한 값을 dict 형태로 저장할 수 있다. 

```python
>>> portfolio = [
	{'name': 'qara', 'months': 24, 'type': 'full-time'},
	{'name': 'kaier', 'months': 13, 'type': 'full-time'},
	{'name': 'oh-lora', 'months': 15, 'type': 'personal project'},
	{'name': 'necton', 'months': 2, 'type': 'freelancer'},
	{'name': 'motov', 'months': 4, 'type': 'full-time'},
	{'name': 'artistcompany', 'months': 5, 'type': 'full-time'}
]
>>> from collections import Counter
>>> total_months = Counter()
>>> for item in portfolio:
	total_months[item.get('type')] += item.get('months', 0)
	print(total_months)

	
Counter({'full-time': 24})
Counter({'full-time': 37})
Counter({'full-time': 37, 'personal project': 15})
Counter({'full-time': 37, 'personal project': 15, 'freelancer': 2})
Counter({'full-time': 41, 'personal project': 15, 'freelancer': 2})
Counter({'full-time': 46, 'personal project': 15, 'freelancer': 2})
```

<details><summary>Counter 공식 도움말 [ 펼치기 / 접기 ]</summary>

```python
class Counter(builtins.dict)
 |  Counter(iterable=None, /, **kwds)
 |  
 |  Dict subclass for counting hashable items.  Sometimes called a bag
 |  or multiset.  Elements are stored as dictionary keys and their counts
 |  are stored as dictionary values.
 |  
 |  >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
 |  
 |  >>> c.most_common(3)                # three most common elements
 |  [('a', 5), ('b', 4), ('c', 3)]
 |  >>> sorted(c)                       # list all unique elements
 |  ['a', 'b', 'c', 'd', 'e']
 |  >>> ''.join(sorted(c.elements()))   # list elements with repetitions
 |  'aaaaabbbbcccdde'
 |  >>> sum(c.values())                 # total of all counts
 |  15
 |  
 |  >>> c['a']                          # count of letter 'a'
 |  5
 |  >>> for elem in 'shazam':           # update counts from an iterable
 |  ...     c[elem] += 1                # by adding 1 to each element's count
 |  >>> c['a']                          # now there are seven 'a'
 |  7
 |  >>> del c['b']                      # remove all 'b'
 |  >>> c['b']                          # now there are zero 'b'
 |  0
 |  
 |  >>> d = Counter('simsalabim')       # make another counter
 |  >>> c.update(d)                     # add in the second counter
 |  >>> c['a']                          # now there are nine 'a'
 |  9
 |  
 |  >>> c.clear()                       # empty the counter
 |  >>> c
 |  Counter()
 |  
 |  Note:  If a count is set to zero or reduced to zero, it will remain
 |  in the counter until the entry is deleted or the counter is cleared:
 |  
 |  >>> c = Counter('aaabbc')
 |  >>> c['b'] -= 2                     # reduce the count of 'b' by two
 |  >>> c.most_common()                 # 'b' is still in, but its count is zero
 |  [('a', 3), ('c', 1), ('b', 0)]
```

</details>

### 4-2. DefaultDict

* import 방법

```python
from collections import defaultdict
```

* 기본 설명
  * 존재하지 않는 key 값을 참조할 때, 오류를 발생시키는 대신 **지정한 type의 초기값을 자동으로 생성** 한다.
  * 예를 들어, ```defaultdict(list)``` 는 지정한 초기값으로 빈 리스트 (list) 를 자동 생성한다.
* 사용 방법
  * 하나의 키를 하나의 값 (value) 이 아닌, **여러 개의 값으로 mapping 시킬 때** 주로 사용한다.

```python
>>> portfolio = [
	{'name': 'qara', 'months': 24, 'type': 'full-time'},
	{'name': 'kaier', 'months': 13, 'type': 'full-time'},
	{'name': 'oh-lora', 'months': 15, 'type': 'personal project'},
	{'name': 'necton', 'months': 2, 'type': 'freelancer'},
	{'name': 'motov', 'months': 4, 'type': 'full-time'},
	{'name': 'artistcompany', 'months': 5, 'type': 'full-time'}
]
>>> from collections import defaultdict
>>> 
>>> portfolio_per_type = defaultdict(list)
>>> for item in portfolio:
	name = item.get('name')
	months = item.get('months', 0)
	portfolio_per_type[item.get('type')].append((name, months))

	
>>> portfolio_per_type
defaultdict(<class 'list'>, {'full-time': [('qara', 24), ('kaier', 13), ('motov', 4), ('artistcompany', 5)],
'personal project': [('oh-lora', 15)], 'freelancer': [('necton', 2)]})
```

## 5. 리스트 컴프리헨션 (list comprehension)

* 리스트 컴프리헨션 (list comprehension) 은 **iterable 의 각 원소에 연산을 적용하여 새로운 리스트를 생성하는 것** 이다.
* 일반적인 구문은 ```[func(x) for x in iterable]``` 이다.
* 사용 예시 (단, 아래 리스트를 기준으로 한다.)

```python
>>> company
['qara', 'kaier', 'motov', 'artistcompany']
```

| 예시 설명              | 예시                                                               |
|--------------------|------------------------------------------------------------------|
| 1번째 글자 추출          | ```[c[:1] for c in company]``` → ```['q', 'k', 'm', 'a']```      |
| 특정 조건을 만족하는 항목만 추출 | ```[c for c in company if 'n' in c]``` → ```['artistcompany']``` |

리스트 컴프리헨션의 본질은 **수학 (집합론) 의 조건제시법** 이라고 할 수 있다.

| Python                                 | 수학 (집합 표시 방법)                                |
|----------------------------------------|----------------------------------------------|
| ```v = [2 * x for x in s if x >= 0]``` | $v = \lbrace 2x \| x \in s, x \ge 0 \rbrace$ |

## 6. 객체와 복사

### 6-1. 객체 ID와 레퍼런스

* 2개의 값이 서로 같은 객체인지 검사하려면 ```is``` 또는 ```==``` 을 사용하되, 되도록 ```==``` 을 사용한다.

```python
>>> a = 'test'
>>> b = a
>>> a == b
True
>>> b == a
True
```

* 객체 ID (메모리 주소) 확인 방법

```python
>>> id(a)
2480686280112
>>> id(b)
2480686280112
```

### 6-2. 얕은 복사 (shallow copy) 와 깊은 복사 (deep copy)

**1. 얕은 복사**

* ```b = list(a)``` 처럼 ```a```의 사본을 만들면, **리스트가 새로 만들어졌지만 그 리스트 안의 항목은 공유되는 현상** 이 발생한다.
* 이는 리스트 안의 항목이 리스트인 경우, **가리키는 메모리 주소 (객체 ID) 가 공유** 되기 때문이다.

```python
>>> a = [1, 2, [3, 4, 5], [6, 7, 8]]
>>> b = list(a)  # shallow copy
>>> a[2], b[2]
([3, 4, 5], [3, 4, 5])
>>> a[2].append(9)
>>> a[2], b[2]
([3, 4, 5, 9], [3, 4, 5, 9])
```

```python
>>> id(a[2]), id(b[2])
(2480716899008, 2480716899008)
```

**2. 깊은 복사**

* 깊은 복사 (deep copy) 는 **객체와 그 안의 모든 사본을 새로운 메모리 주소에 저장** 하는 것이다.
* 다음과 같이 **객체 ID (= 메모리 주소) 가 공유되지 않는다.**

```python
>>> from copy import deepcopy
>>> a = [1, 2, [3, 4, 5], [6, 7, 8]]
>>> b = deepcopy(a)
>>> a[2], b[2]
([3, 4, 5], [3, 4, 5])
>>> a[2].append(9)
>>> a[2], b[2]
([3, 4, 5, 9], [3, 4, 5])
```

```python
>>> id(a[2]), id(b[2])
(2480716914944, 2480717000320)
```

