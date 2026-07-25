
## 기존 정리한 내용

* 제너레이터
  * [Practical Python Programming > 06_Generator.md](../Practical_Python_programming/06_Generator.md)
* 비동기 프로그래밍
  * [Python Clean Code 2nd Edition > 02_Pythonic_Code.md > 8. 비동기 코드](../Python_Clean_Code_2nd_Edition/02_Pythonic_Code.md#8-비동기-코드) 
* 이터레이터 관련
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
