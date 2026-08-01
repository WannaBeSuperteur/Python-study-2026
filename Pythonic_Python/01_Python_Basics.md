
## 목차

* [1. 리스트, 튜플, 딕셔너리, 세트](#1-리스트-튜플-딕셔너리-세트)
  * [1-1. 리스트 관련 함수](#1-1-리스트-관련-함수)
  * [1-2. 튜플 관련 함수](#1-2-튜플-관련-함수)
  * [1-3. 딕셔너리의 특징 및 관련 함수](#1-3-딕셔너리의-특징-및-관련-함수)
  * [1-4. 세트 (set) 관련 함수](#1-4-세트-set-관련-함수)
* [2. 조건문, 반복문 관련](#2-조건문-반복문-관련)

## 1. 리스트, 튜플, 딕셔너리, 세트

리스트 (list), 튜플 (tuple), 딕셔너리 (dict), 세트 (set) 를 **컬렉션 자료형** 이라고 한다.

### 1-1. 리스트 관련 함수

* 리스트 관련 함수

| 함수                   | 설명                               |
|----------------------|----------------------------------|
| ```extend([x, y])``` | 리스트의 끝에 여러 원소 추가                 |
| ```insert(i, x)```   | 리스트의 ```i``` index에 ```x``` 를 추가 |
| ```remove(x)```      | 리스트에서 ```x```를 제거                |
| ```reverse()```      | 리스트 뒤집기                          |

```python
>>> companies = ['qara', 'kaier', 'motov']
>>> companies.extend(['artistcompany', 'rainbow8'])
>>> companies
['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> companies.insert(2, 'necton')
>>> companies
['qara', 'kaier', 'necton', 'motov', 'artistcompany', 'rainbow8']
>>> companies.remove('artistcompany')
>>> companies
['qara', 'kaier', 'necton', 'motov', 'rainbow8']
>>> companies.reverse()
>>> companies
['rainbow8', 'motov', 'necton', 'kaier', 'qara']
```

### 1-2. 튜플 관련 함수

* 튜플 관련 함수

| 함수             | 설명                   |
|----------------|----------------------|
| ```count(x)``` | ```x```라는 값의 개수 반환   |
| ```index(x)``` | ```x```의 인덱스 (위치) 반환 |

```python
>>> ymd = (2026, 1, 26)
>>> y, m, d = ymd  # tuple 은 unpacking 가능
>>> y
2026
>>> m
1
>>> d
26
>>> ymd.count(1)
1
>>> ymd.count(26)
1
>>> ymd.count(29)
0
>>> ymd.index(2026)
0
>>> ymd.index(26)
2
>>> ymd.index(33)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ymd.index(33)
ValueError: tuple.index(x): x not in tuple
```

* 튜플은 **딕셔너리의 키로 활용 가능** 하다.

### 1-3. 딕셔너리의 특징 및 관련 함수

* 딕셔너리의 특징
  * **Python3.7+** 에서는 **순서를 보장** 한다.
  * ```get(key, default)``` 를 이용하면 딕셔너리에 ```key```가 없어도 오류가 발생하지 않고, 대신 ```default``` 가 출력된다.
  * **불변 객체 (tuple 포함)** 만이 key가 될 수 있다. 
* 딕셔너리의 활용
  * JSON 구조와 동일한 점을 활용 (API 응답 처리 등)
  * 데이터 매핑, 빈도수 세기 등
  * 간결한 딕셔너리 생성 (dict comprehension)
* 딕셔너리 관련 함수

| 함수                       | 설명                                  |
|--------------------------|-------------------------------------|
| ```update(key, value)``` | 딕셔너리의 ```key``` 키를 ```value``` 로 갱신 |
| ```pop(key)```           | 딕셔너리에서 특정 키 삭제                      |

```python
>>> career = {'qara': 24, 'kaier': 12, 'motov': 3, 'artistcompany': 6, 'rainbow8': 2}
>>> career.pop('rainbow8')
2
>>> career
{'qara': 24, 'kaier': 12, 'motov': 3, 'artistcompany': 6}
>>> career.update({'artistcompany': 5})
>>> career
{'qara': 24, 'kaier': 12, 'motov': 3, 'artistcompany': 5}
>>> career.get('rainbow8', '404 not found in the system')
'404 not found in the system'
```

### 1-4. 세트 (set) 관련 함수

* 세트 (set) 관련 함수

| 함수               | 설명                                              |
|------------------|-------------------------------------------------|
| ```add(x)```     | set에 원소 ```x``` 추가                              |
| ```remove(x)```  | set에서 원소 ```x``` 제거 (단, 해당 원소가 없을 시 **오류 발생**)  |
| ```discard(x)``` | set에서 원소 ```x``` 제거 (단, 해당 원소가 없을 시 **그냥 무시됨**) |

* ```frozenset``` 은 **불변 집합** 을 만들 수 있고, 이는 **딕셔너리의 키로 기능** 할 수 있다.

```python
>>> companies = {'qara', 'kaier', 'motov'}
>>> companies.add('artistcompany')
>>> companies
{'kaier', 'motov', 'qara', 'artistcompany'}
>>> companies.remove('rainbow8')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    companies.remove('rainbow8')
KeyError: 'rainbow8'
>>> companies.discard('rainbow8')
>>> companies.discard('artistcompany')
>>> companies
{'kaier', 'motov', 'qara'}
```

```python
>>> test = frozenset([2014, 2, 6])
>>> test
frozenset({2, 2014, 6})
>>> test_dict = {test: 'Frozen (Elsa)'}
>>> test_dict
{frozenset({2, 2014, 6}): 'Frozen (Elsa)'}
```

## 2. 조건문, 반복문 관련

* ```enumerate``` 함수에서 ```start=n``` 으로 하면 인덱스의 값을 ```n```부터 시작할 수 있다.

```python
>>> companies = ['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> for i, company in enumerate(companies, start=1):
	print(f"{i} 번째 회사: {company}")

	
1 번째 회사: qara
2 번째 회사: kaier
3 번째 회사: motov
4 번째 회사: artistcompany
5 번째 회사: rainbow8
```

* ```if-elif-else``` 구문으로 연산을 분기할 때, **딕셔너리 매핑 (dictionary dispatch)** 을 사용하면 이를 pythonic 하게 만들 수 있다.

```python
>>> operations = {
	"mean": lambda x: sum(x) / len(x) if x else 'x is empty',
	"max_min_diff": lambda x: max(x) - min(x),
	"max_min_div": lambda x: max(x) / min(x) if min(x) > 0 else 'min of x is 0 or below'
}
```

```python
>>> x = [100, 45, 20, 75, 70, 90]
>>> print(operations["mean"](x))
66.66666666666667
>>> print(operations["max_min_diff"](x))
80
>>> print(operations["max_min_div"](x))
5.0
```
