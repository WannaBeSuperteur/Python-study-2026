
## 목차

* [1. 컴프리헨션/제너레이터 표현식 적용 리팩토링](#1-컴프리헨션제너레이터-표현식-적용-리팩토링)
  * [1-1. 중첩 컴프리헨션](#1-1-중첩-컴프리헨션)
* [2. 튜플 언패킹](#2-튜플-언패킹)

## 1. 컴프리헨션/제너레이터 표현식 적용 리팩토링

* 소수 중에서 일의 자리가 7인 것의 합 구하기 (제너레이터 표현식 적용)

```python
# old (not Pythonic)
>>> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
>>> def old_sum_sevens(primes: list) -> list:
	result = 0
	for p in primes:
		if p % 10 == 7:
			result += p
	return result

# new (Pythonic)
>>> def new_sum_sevens(primes: list) -> list:
	return sum(p for p in primes if p % 10 == 7)

>>> print(old_sum_sevens(primes))
61
>>> print(new_sum_sevens(primes))
61
```

* 소수 중에서 일의 자리가 7인 것의 제곱의 리스트 구하기 (list comprehension 적용)

```python
>>> def old_square_sevens(primes: list) -> list:
	result = []
	for p in primes:
		if p % 10 == 7:
			result.append(p * p)
	return result

>>> def new_square_sevens(primes: list) -> list:
	return [p * p for p in primes if p % 10 == 7]

>>> print(old_square_sevens(primes))
[49, 289, 1369]
>>> print(new_square_sevens(primes))
[49, 289, 1369]
```

* 회사 이름에 'n' 포함 여부를 mapping 시키는 딕셔너리 만들기 (dict comprehension 적용)

```python
>>> companies = ['qara', 'kaier', 'motov', 'artistcompany', 'rainbow8']
>>> def old_is_n_map(names: list) -> dict:
	result: dict = {}
	for name in names:
		result[name] = 'n' in name
	return result

>>> def new_is_n_map(names: list) -> dict:
	return {name: 'n' in name for name in names}

>>> print(old_is_n_map(companies))
{'qara': False, 'kaier': False, 'motov': False, 'artistcompany': True, 'rainbow8': True}
>>> print(new_is_n_map(companies))
{'qara': False, 'kaier': False, 'motov': False, 'artistcompany': True, 'rainbow8': True}
```

### 1-1. 중첩 컴프리헨션

* 모든 ```소수```월 ```소수```일 구하기 (단, ```일```은 28일까지만 있음)

```python
>>> def old_prime_md(months: list, days: list) -> list:
	mds: list = []
	for m in months:
		for d in days:
			if m <= 12 and d <= 28:
				mds.append((m, d))
	return mds

>>> def new_prime_md(months: list, days: list) -> list:
	return [(m, d) for m in months for d in days
		if m <= 12 and d <= 28]

>>> print(old_prime_md(months=primes, days=primes))
[(2, 2), (2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (2, 19), (2, 23), (3, 2), (3, 3), (3, 5), (3, 7), (3, 11), (3, 13), (3, 17), (3, 19), (3, 23), (5, 2), (5, 3), (5, 5), (5, 7), (5, 11), (5, 13), (5, 17), (5, 19), (5, 23), (7, 2), (7, 3), (7, 5), (7, 7), (7, 11), (7, 13), (7, 17), (7, 19), (7, 23), (11, 2), (11, 3), (11, 5), (11, 7), (11, 11), (11, 13), (11, 17), (11, 19), (11, 23)]
>>> print(new_prime_md(months=primes, days=primes))
[(2, 2), (2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (2, 19), (2, 23), (3, 2), (3, 3), (3, 5), (3, 7), (3, 11), (3, 13), (3, 17), (3, 19), (3, 23), (5, 2), (5, 3), (5, 5), (5, 7), (5, 11), (5, 13), (5, 17), (5, 19), (5, 23), (7, 2), (7, 3), (7, 5), (7, 7), (7, 11), (7, 13), (7, 17), (7, 19), (7, 23), (11, 2), (11, 3), (11, 5), (11, 7), (11, 11), (11, 13), (11, 17), (11, 19), (11, 23)]
```

## 2. 튜플 언패킹

* 각 회사의 재직 개월 수 출력

```python
>>> career = [{'qara': 24}, {'kaier': 12}, {'motov': 3}, {'artistcompany': 6}, {'rainbow8': 2}]
>>> career = [('qara', 24), ('kaier', 12), ('motov', 3), ('artistcompany', 6), ('rainbow8', 2)]
>>> def old_unpack(career: list):
	for c in career:
		name = c[0]
		months = c[1]
		print(f'{name} ({months} 개월 재직)')

		
>>> def new_unpack(career: list):
	for name, months in career:
		print(f'{name} ({months} 개월 재직)')

		
>>> old_unpack(career)
qara (24 개월 재직)
kaier (12 개월 재직)
motov (3 개월 재직)
artistcompany (6 개월 재직)
rainbow8 (2 개월 재직)
>>> new_unpack(career)
qara (24 개월 재직)
kaier (12 개월 재직)
motov (3 개월 재직)
artistcompany (6 개월 재직)
rainbow8 (2 개월 재직)
```
