
## 목차

* [1. 리스트](#1-리스트)
* [2. 인터프리터와 컴파일러](#2-인터프리터와-컴파일러)
* [3. for-else 와 while-else](#3-for-else-와-while-else)
* [4. Python의 LEGB Rule](#4-python의-legb-rule)

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
