
## 목차

* [1. 제너레이터](#1-제너레이터)
  * [1-1. 제너레이터의 용도](#1-1-제너레이터의-용도)
  * [1-2. 제너레이터 표현식](#1-2-제너레이터-표현식)
  * [1-3. 제너레이터를 이용한 중첩 루프의 처리](#1-3-제너레이터를-이용한-중첩-루프의-처리)
* [2. 이터러블과 이터레이터](#2-이터러블과-이터레이터)
* [3. 제너레이터를 코루틴으로 만들기](#3-제너레이터를-코루틴으로-만들기)
  * [3-1. close 예시](#3-1-close-예시)
  * [3-2. throw 예시](#3-2-throw-예시)
  * [3-3. send 예시](#3-3-send-예시)

## 기존 정리한 내용

* 제너레이터
  * [Practical Python Programming > 06_Generator.md](../Practical_Python_programming/06_Generator.md)
* 비동기 프로그래밍
  * [Python Clean Code 2nd Edition > 02_Pythonic_Code.md > 8. 비동기 코드](../Python_Clean_Code_2nd_Edition/02_Pythonic_Code.md#8-비동기-코드) 
* 이터러블, 이터레이터 관련
  * ```itertools``` 모듈 관련: [Practical Python Programming > 06_Generator.md > 4. itertools 모듈](../Practical_Python_programming/06_Generator.md#4-itertools-모듈)

## 1. 제너레이터

제너레이터는 **한번에 1개의 구성 요소만을 반환** 하는 이터레이터 객체를 반환하는 함수이다.

## 1-1. 제너레이터의 용도

* 파일의 모든 데이터를 읽어오는 대신, **한번에 하나의 데이터를 읽어온다.**
  * 이를 통해 메모리 사용량 및 데이터 read 소요시간을 줄인다.
  * 이때 **필요한 내용만 그때그때 가져올 수 있다.**

## 1-2. 제너레이터 표현식

* 이터러블을 인자로 받는 함수 (```max``` ```min``` ```sum``` 등) 사용 시에는 **제너레이터 표현식** 을 사용해야 한다.
  * 제너레이터 표현식은 [리스트 컴프리헨션](../Practical_Python_programming/02_Work_with_Data.md#5-리스트-컴프리헨션-list-comprehension) 의 역할을 대체한다.

```python
>>> import time
>>> def sum_with_iteration(n):
	start_at = time.time()
	result = sum([(i**2 % 1000) for i in range(n)])  # 권장되지 않음 (list + sum)
	print(f'elapsed time: {time.time() - start_at}')

	
>>> def sum_with_generator_expression(n):
	start_at = time.time()
	result = sum((i**2 % 1000) for i in range(n))  # 권장 (generator expression 사용)
	print(f'elapsed time: {time.time() - start_at}')

>>> sum_with_iteration(15_000_000)
elapsed time: 4.78777003288269

>>> sum_with_generator_expression(15_000_000)
elapsed time: 4.489528179168701
```

* 제너레이터는 **한번만 사용된 후 재사용할 수 없기 때문에** 주의가 필요하다.

## 1-3. 제너레이터를 이용한 중첩 루프의 처리

* Python에서 중첩 루프로 인해 **많은 양의 들여쓰기** 가 있는 코드는 피해야 한다.
  * 대신 중첩 루프에 해당하는 부분은 **별도의 제너레이터 함수로 빼서** 사용한다.

```python
>>> def find_lucky_number_bad(array, lucky_number):
	idx = None
	for i, cell_value in enumerate(array):
		if cell_value == lucky_number:
			idx = i
			break
	print(f'Lucky Number {lucky_number} index: {idx}')
	return idx

>>> find_lucky_number_bad([2, 0, 2, 6, 0, 7, 2, 5], 7)
Lucky Number 7 index: 5
5
```

```python
>>> def _iterator_array(array):
	for i, cell_value in enumerate(array):
		yield i, cell_value

		
>>> def find_lucky_number_good(array, lucky_number):
	idx = next(
		idx
		for (idx, cell_value) in _iterator_array(array)
		if cell_value == lucky_number
	)
	print(f'Lucky Number {lucky_number} index: {idx}')
	return idx

>>> find_lucky_number_good([2, 0, 2, 6, 0, 7, 2, 5], 7)
Lucky Number 7 index: 5
5
```

* 위 예제를 통해, 제너레이터는 **메모리 절약** 뿐만 아니라 **반복문을 추상화 수단으로 활용** 까지 할 수 있음을 알 수 있다.

## 2. 이터러블과 이터레이터

* **이터러블** (이터러블 객체) 은 ```for ... in ...``` 과 같이 사용할 수 있는, **반복을 지원하는 객체** 이다.
* **이터레이터** 는 **이터러블에 대해 한 번에 하나씩 값을 '생산'** 하는 객체이다.
  * 내장된 ```next()``` 함수를 이용한다.
* 따라서 **모든 제너레이터는 이터레이터** 라고 할 수 있다.

## 3. 제너레이터를 코루틴으로 만들기

제너레이터를 [코루틴 (Coroutine)](02_Pythonic_Code.md#8-비동기-코드) 으로 사용할 수 있다.

* 관련 메서드 (제너레이터 인터페이스 메서드) 는 다음과 같다.

| 메서드                                          | 설명                                                          |
|----------------------------------------------|-------------------------------------------------------------|
| ```close()```                                | 제너레이터에서 ```GeneratorExit``` 예외 발생 (따로 처리하지 않으면 제너레이터 반복 중지) |
| ```throw(ex_type, ex_value, ex_traceback)``` | 제너레이터 중단 위치 (현재 위치) 에서 예외 발생                                |
| ```send(value)```                            | ```next()``` 함수에 파라미터 (읽어올 데이터의 개수 등) 를 추가한 버전              |

* 단, ```send()``` 메서드 호출을 위해서는 **```next()``` 를 반드시 먼저 호출** 해야 한다.

### 3-1. close 예시

```python
>>> def close_test(start: int, end: int):
	current_value = start
	try:
		while current_value <= end:
			yield current_value
			current_value += 1
	except GeneratorExit:
		print('Generator Exit')

		
>>> test = close_test(100, 500)
>>> next(test)
100
>>> next(test)
101
>>> next(test)
102
>>> test.close()
Generator Exit
```

### 3-2. throw 예시

* CustomException 을 throw 한 결과, ```current_value``` 10 증가 처리된다.

```python
>>> class CustomException(Exception):
	pass

>>> def throw_test(start: int, end: int):
	current_value = start
	while True:
		try:
			while current_value <= end:
				yield current_value
				current_value += 1
		except CustomException as e:
			print('Custom Exception : increase 10')
			current_value += 10
		except Exception as e:
			print(f'Exception : {e}')
			current_value = end + 1
			break

		
>>> test = throw_test(start=100, end=500)
>>> next(test)
100
>>> next(test)
101
>>> test.throw(CustomException)
Custom Exception : increase 10
111
>>> next(test)
112

>>> test.throw(RuntimeError)
Exception : 
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    test.throw(RuntimeError)
StopIteration

>>> next(test)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    next(test)
StopIteration
```

### 3-3. send 예시

```python
>>> def send_test():
	while True:
		n = yield
		for i in range(1, n):
			if n % i == 0:
				print(f'{i} 는 {n}의 약수입니다.')

				
>>> test = send_test()

# 코루틴에서 send 메서드 호출 전에는 반드시 한번 next() 를 먼저 호출해야 함 !!
>>> test.send(2026)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    test.send(2026)
TypeError: can't send non-None value to a just-started generator

>>> next(test)
>>> test.send(2026)
1 는 2026의 약수입니다.
2 는 2026의 약수입니다.
1013 는 2026의 약수입니다.
>>> test.send(2028)
1 는 2028의 약수입니다.
2 는 2028의 약수입니다.
3 는 2028의 약수입니다.
4 는 2028의 약수입니다.
6 는 2028의 약수입니다.
12 는 2028의 약수입니다.
13 는 2028의 약수입니다.
26 는 2028의 약수입니다.
39 는 2028의 약수입니다.
52 는 2028의 약수입니다.
78 는 2028의 약수입니다.
156 는 2028의 약수입니다.
169 는 2028의 약수입니다.
338 는 2028의 약수입니다.
507 는 2028의 약수입니다.
676 는 2028의 약수입니다.
1014 는 2028의 약수입니다.
```

