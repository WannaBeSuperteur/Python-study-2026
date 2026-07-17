
## 목차

* [1. 가변 인자](#1-가변-인자)
  * [1-1. 위치 가변 인자 (*args)](#1-1-위치-가변-인자-args)
  * [1-2. 키워드 가변 인자 (**kwargs)](#1-2-키워드-가변-인자-kwargs)
  * [1-3. 혼합 사용](#1-3-혼합-사용)
  * [1-4. 예제](#1-4-예제)
* [2. key 함수를 이용한 정렬](#2-key-함수를-이용한-정렬)
* [3. 람다 함수 (lambda) 사용 시 유의사항](#3-람다-함수-lambda-사용-시-유의사항)
* [4. 클로저 (Closure)](#4-클로저-closure)
  * [4-1. 지연된 평가 (delayed evaluation)](#4-1-지연된-평가-delayed-evaluation)
  * [4-2. 데코레이터 함수 (decorator function)](#4-2-데코레이터-함수-decorator-function)
* [5. 메서드의 데코레이션](#5-메서드의-데코레이션)

## 1. 가변 인자

* 가변 인자에는 ```*args``` 와 ```**kwargs``` 가 있다.
* 가변 인자를 사용한다는 것은 **임의의 개수의 인자를 받는** 다는 것이다.

| 구분        | 표시 형식          | 추가 인자 호출 방법   | 추가 인자를 받는 방법 |
|-----------|----------------|---------------|--------------|
| 위치 가변 인자  | ```*args```    | 키워드 **없어도 됨** | **튜플** 형태    |
| 키워드 가변 인자 | ```**kwargs``` | 키워드 **필요**    | **딕셔너리** 형태  |

### 1-1. 위치 가변 인자 (*args)

```def f(x, *args):``` 의 의미는 다음과 같다.

* 함수 호출 시 최초의 1개의 인자를 ```x```로 한다.
* 나머지 (n-1) 개의 인자를 ```*args``` 에 넣어서 추가적으로 튜플로 전달한다.
* [참고](../Python_for_beginners/things_I_didnt_know.md#6-인자-매개변수)

추가적으로 **튜플을 가변 인자로 확장** 할 수 있다. 예를 들어 다음과 같다.

* 아래 예시에서 ```f(100, *test)``` 는 ```f(100, 1, 2, 3)``` 과 같은 의미이다.

```python
test = (1, 2, 3)
f(100, *test)
```

### 1-2. 키워드 가변 인자 (**kwargs)

```def f(x, y, **kwargs):``` 의 의미는 다음과 같다.

* 함수 호출 시 최초의 2개의 인자를 각각 ```x```, ```y```로 한다.
* 나머지 (n-2) 개의 인자를 ```**kwargs``` 에 넣어서 추가적으로 딕셔너리로 전달한다.

### 1-3. 혼합 사용

```def f(*args, **kwargs):``` 의 의미는 다음과 같다.

* 함수 호출 시 키워드를 명시하지 않은 (예: ```value```) argument 들은 ```*args``` 로 전달된다.
* 함수 호출 시 키워드를 명시한 (예: ```keyword=value```) argument 들은 ```**kwargs``` 로 전달된다.
* ```def f(x, *args, **kwargs)``` 와 같이 하는 경우, 최초 1개의 인자는 ```x``` 로 한다.

### 1-4. 예제

* 위치 가변 인자, 키워드 가변 인자의 기본

```python
>>> def test_args(x, *args):
	print(f"x: {x}")
	print(f"additional args: {args}")

	
>>> def test_kwargs(x, **kwargs):
	print(f"x: {x}")
	print(f"additional kwargs: {kwargs}")

	
>>> test_args(1, 2, 10)
x: 1
additional args: (2, 10)
>>> test_kwargs(1, 2, 10)
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    test_kwargs(1, 2, 10)
TypeError: test_kwargs() takes 1 positional argument but 3 were given
>>> test_kwargs(1, keyword=2, argument=10)
x: 1
additional kwargs: {'keyword': 2, 'argument': 10}
```

* 혼합 사용

```python
>>> def test_both(*args, **kwargs):
	print(f"args: {args}")
	print(f"kwargs: {kwargs}")

	
>>> test_both(15, 30, test=45)
args: (15, 30)
kwargs: {'test': 45}
```

```python
>>> def test_both_2(x, *args, **kwargs):
	print(f"x: {x}")
	print(f"args: {args}")
	print(f"kwargs: {kwargs}")

	
>>> test_both_2(15, 30, test=45)
x: 15
args: (30,)
kwargs: {'test': 45}
```

## 2. key 함수를 이용한 정렬

* ```iterable.sort(key=func)``` 에서 ```func``` 을 정렬 기준 함수로 전달할 수 있다.
* 해당 정렬 기준 함수의 반환값을 기준으로 정렬된다.

```python
>>> data = [
	{'name': '김', 'coding_test': 80, 'interview': 60},
	{'name': '이', 'coding_test': 75, 'interview': 55},
	{'name': '박', 'coding_test': 99, 'interview': 70},
	{'name': '최', 'coding_test': 70, 'interview': 84}
]
>>> def total_score(s):
	return s.get('coding_test', 0) + s.get('interview', 0)

>>> data.sort(key=total_score, reverse=True)
>>> pprint.pprint(data)
[{'coding_test': 99, 'interview': 70, 'name': '박'},
 {'coding_test': 70, 'interview': 84, 'name': '최'},
 {'coding_test': 80, 'interview': 60, 'name': '김'},
 {'coding_test': 75, 'interview': 55, 'name': '이'}]
```

* 이 key 함수는 **콜백 함수 (Callback function)** 의 일종이다.

## 3. 람다 함수 (lambda) 사용 시 유의사항

* 람다 함수는 ```iterable.sort(key=lambda ...)``` 와 같이 일반적으로 **다른 함수와 함께 사용한다.**
* 람다 함수는 제한적으로 사용하며, **단일 표현식 수준으로만 가능** 하다.
* 람다 함수에 **if, while 등 추가 구문은 허용되지 않는다.**

## 4. 클로저 (Closure)

* 어떤 함수에 대해 **그 함수의 내부 함수를 결과로 반환** 할 때, 그 내부 함수를 말한다.
* 클로저의 용도는 다음과 같다.
  * 콜백 함수
  * [지연된 평가 (delayed evaluation)](#4-1-지연된-평가-delayed-evaluation)
  * [데코레이터 함수](#4-2-데코레이터-함수-decorator-function)
  * 과도한 코드 반복을 피하는 용도

### 4-1. 지연된 평가 (delayed evaluation)

**지연된 평가 (delayed evaluation)** 는 **계산 결과값이 필요할 때까지 계산을 지연시키는 것** (주로 함수만 생성/정의해 놓고) 이다.

* 지연된 평가를 하는 이유는 다음과 같다.
  * 불필요한 계산 생략을 통한 **빠른 실행**
  * 오류 회피

```python
>>> def compute_score(performance: int = 0, competency: int = 0, attitude: int = 0):
	def do_compute():
		print(f'성과: {performance}, 역량: {competency}, 태도: {attitude}')
		total = performance + competency + attitude
		print(f'합계: {total}')
		print(f'평균: {round(total / 3, 2)}')
		if total >= 200:
			print('수습 통과')
		else:
			print('수습 탈락')
	return do_compute

>>> PROBATION_PERIOD = 90
>>> import time
>>> def evaluate_probation(days, compute_score_func):
	while days < PROBATION_PERIOD:
		remaining = PROBATION_PERIOD - days
		print(f'수습 평가까지 {remaining} 일 남았습니다.')
		days += 1
		time.sleep(0.15)
	compute_score_func()

	
>>> evaluate_probation(90, compute_score(75, 50, 60))
성과: 75, 역량: 50, 태도: 60
합계: 185
평균: 61.67
수습 탈락

>>> evaluate_probation(75, compute_score(45, 40, 100))
수습 평가까지 15 일 남았습니다.
수습 평가까지 14 일 남았습니다.
수습 평가까지 13 일 남았습니다.
수습 평가까지 12 일 남았습니다.
수습 평가까지 11 일 남았습니다.
수습 평가까지 10 일 남았습니다.
수습 평가까지 9 일 남았습니다.
수습 평가까지 8 일 남았습니다.
수습 평가까지 7 일 남았습니다.
수습 평가까지 6 일 남았습니다.
수습 평가까지 5 일 남았습니다.
수습 평가까지 4 일 남았습니다.
수습 평가까지 3 일 남았습니다.
수습 평가까지 2 일 남았습니다.
수습 평가까지 1 일 남았습니다.
성과: 45, 역량: 40, 태도: 100
합계: 185
평균: 61.67
수습 탈락
```

### 4-2. 데코레이터 함수 (decorator function)

데코레이터 함수는 **함수를 실행할 때, 실행 전후에 특정 기능을 하는 함수를 만들어서 그 함수를 'wrapping' 하는 것** 을 말한다.

* 주로 여러 함수에서 사용되는 공통되는 기능을 wrapping 하기 위해서 사용된다.

```python
>>> from time import perf_counter
>>> def execution_timer(func):
	def wrapper(*args, **kwargs):
		print(f'자, {func.__name__} 함수를 실행해 볼까요?')
		start_at = perf_counter()
		result = func(*args, **kwargs)
		elapsed_time = perf_counter() - start_at
		print(f'{func.__name__} 함수 실행 종료! 걸린 시간은 {elapsed_time} 초입니다.')
		return result
	return wrapper

>>> @execution_timer
def test():
	i = 0
	while i < 20260717:
		i += 1
	return i

>>> test()
자, test 함수를 실행해 볼까요?
test 함수 실행 종료! 걸린 시간은 0.7259770000000572 초입니다.
20260717
>>> print(test())
자, test 함수를 실행해 볼까요?
test 함수 실행 종료! 걸린 시간은 0.74524079999901 초입니다.
20260717
```

## 5. 메서드의 데코레이션

* 함수뿐만 아니라 **Class의 메서드 역시 데코레이션이 가능** 하다.

| 데코레이션               | 설명                                                                                                                   |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| ```@classmethod```  | - 클래스 메서드 정의에 사용<br>- **클래스 객체 자체를 첫 매개변수** 로 함<br>- 새 인스턴스를 생성하는 **생성자 (constructor) 를 클래스 자체 메서드로 포함시키기 위해** 종종 사용 |
| ```@staticmethod``` | - 클래스에 속한 함수이지만, **클래스의 객체 (instance) 를 처리하지는 않음**<br>- 생성한 인스턴스 관리 (메모리, lock 등) 목적으로 사용                            |
| ```@property```     | getter & setter 목적으로 사용 [(참고)](05_Internal_Working_of_Python_Object.md#5-속성-property)                                |
