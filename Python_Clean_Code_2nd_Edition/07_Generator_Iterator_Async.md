
## 목차

* [1. 제너레이터의 용도](#1-제너레이터의-용도)
* [2. 제너레이터 표현식](#2-제너레이터-표현식)
* [3. 제너레이터를 이용한 중첩 루프의 처리](#3-제너레이터를-이용한-중첩-루프의-처리)

## 기존 정리한 내용

* 제너레이터
  * [Practical Python Programming > 06_Generator.md](../Practical_Python_programming/06_Generator.md)
* 비동기 프로그래밍
  * [Python Clean Code 2nd Edition > 02_Pythonic_Code.md > 8. 비동기 코드](../Python_Clean_Code_2nd_Edition/02_Pythonic_Code.md#8-비동기-코드) 
* 이터러블, 이터레이터 관련
  * ```itertools``` 모듈 관련: [Practical Python Programming > 06_Generator.md > 4. itertools 모듈](../Practical_Python_programming/06_Generator.md#4-itertools-모듈)

## 1. 제너레이터의 용도

* 파일의 모든 데이터를 읽어오는 대신, **한번에 하나의 데이터를 읽어온다.**
  * 이를 통해 메모리 사용량 및 데이터 read 소요시간을 줄인다.
  * 이때 **필요한 내용만 그때그때 가져올 수 있다.**

## 2. 제너레이터 표현식

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

## 3. 제너레이터를 이용한 중첩 루프의 처리

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
