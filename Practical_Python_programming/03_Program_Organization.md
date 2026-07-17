## 목차

* [1. 함수 작성 시 유의 사항](#1-함수-작성-시-유의-사항)
  * [1-1. docstring 및 type annotation](#1-1-docstring-및-type-annotation)
  * [1-2. 전역 변수와 지역 변수](#1-2-전역-변수와-지역-변수)
  * [1-3. 변수 할당과 메모리](#1-3-변수-할당과-메모리)
* [2. 오류 (Exception) 잡기](#2-오류-exception-잡기)
  * [2-1. 오류를 잡을 때 권장사항](#2-1-오류를-잡을-때-권장사항) 
  * [2-2. finally 문을 통한 '오류 여부 무관하게 항상 실행'](#2-2-finally-문을-통한-오류-여부-무관하게-항상-실행)
* [3. 모듈 검색 경로 추가](#3-모듈-검색-경로-추가)
* [4. shebang (#!)](#4-shebang-)

## 1. 함수 작성 시 유의 사항

* 단일 작업에 대한 **중복된 코드는 함수로 만들어서 사용** 해야 한다.
* 함수는 **나중에 나오는 함수는 앞의 함수를 바탕으로 하는 상향식 (bottom-up)** 방식으로 작성하는 것이 좋다.

```python
def parse_name(x: str) -> list:
    ...

def check_validity(name: str):
    ...
    parse_result = parse_name(name)
    ...

check_validity()
```

### 1-1. docstring 및 type annotation

* 다음과 같이 **함수를 나타내는 docstring** 을 작성하는 것이 좋다.
  * 이 문자열은 ```help()``` 함수 등에서 인식한다.
* 함수 정의에서 **type annotation** 을 추가할 수 있다. (type hint로 순전히 **정보성** 이지만, IDE 등에서 사용할 수 있다.)

```python
def parse_name(x: str) -> list:
   """return [성, 이름] from the name string 'x'."""
   ...
```

### 1-2. 전역 변수와 지역 변수

* 함수 내에서 할당된 변수는 **지역 변수 (private)** 이다. (다른 곳의 변수와 충돌하지 않음)
* 함수는 같은 파일 내에서 정의된 **전역 변수 (global) 에 자유롭게 접근** 할 수 있다.
  * 단, **함수 안에서는 전역 변수를 수정할 수 없다.**

```python
>>> company = 'widerplanet'  # global 변수
>>> 
>>> def test():
	company = 'artistcompany'  # global 을 수정하는 것이 아닌, local 을 새로 정의하는 것임

	
>>> test()
>>> company  # global 변수에 할당된 값인 'widerplanet' 출력
'widerplanet'
```

* 즉, **함수 내에서 일어나는 모든 변수 할당은 로컬 (local) 레벨** 이다.

### 1-3. 변수 할당과 메모리

* 함수 내의 argument로 주어진 변수를 ```argument = ...``` 식으로 재할당하는 경우, **로컬 'argument' 변수를 새로 만들어서 다른 객체를 가리키게 된다.**
* **변수 할당은 메모리를 덮어쓰지 않고, 새로운 메모리 공간을 차지한다. (즉, 불필요한 메모리 낭비를 발생시킬 수 있다.)**

**1. 변수 수정**

```python
>>> def foo(anniversary):
	anniversary.append(16)

	
>>> widerplanet_anniversary = list(range(1, 16))
>>> foo(widerplanet_anniversary)
>>> print(widerplanet_anniversary)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # 변수 수정 - argument로 들어온 변수 내용이 수정됨
```

**2. 변수 재할당**

```python
>>> def foo(anniversary):
	anniversary = list(range(1, 17))  # 'anniversary' 변수에 새로운 값 재 할당

	
>>> widerplanet_anniversary = list(range(1, 16))
>>> foo(widerplanet_anniversary)
>>> print(widerplanet_anniversary)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # 변수 재할당 - argument로 들어온 변수 내용이 수정되지 않음
```

## 2. 오류 (Exception) 잡기

### 2-1. 오류를 잡을 때 권장사항

```except``` 를 여러 개 활용하여, 각 종류에 따른 여러 가지 오류를 잡을 수 있다.

```python
try:
    ...
except ValueRrror as e:
    ...
except KeyboardInterrupt as e:
    ...
```

* 다음과 같이 **모든 오류를 ```Exception``` 하나로 붙잡는 것은 디버깅을 불편하게 하므로 일반적으로 잘못된 방식** 이다.

```python
try:
    celebrate_widerplanet_16th_anniversary()
except Exception:  # 발생 가능한 모든 오류를 catch 하므로, 예상치 못한 오류도 여기서 catch 하여 디버깅이 곤란해질 수 있다.
    print('Why failed?')
```

* 이 경우 다음과 같이 **오류 메시지를 출력 (민감한 정보, 기밀 정보의 경우 출력에 주의 필요)** 하도록 하는 것이 좋다.

```python
try:
    celebrate_widerplanet_16th_anniversary()
except Exception as e:
    print(f'Why failed? Reason: {e}')
```

* 여기서 catch 한 Exception을 **전파 (raise)** 할 수도 있다.
  * 이를 통해 이 부분을 호출한 함수에 **오류를 전달하고, 로깅 등에 도움을 줄 수 있다.**

```python
try:
    celebrate_widerplanet_16th_anniversary()
except Exception as e:
    print(f'Why failed? Reason: {e}')
    raise
```

### 2-2. finally 문을 통한 '오류 여부 무관하게 항상 실행'

```finally``` 문에서는 오류 발생 여부와 관계없이 **항상 실행되어야 하는 코드** 를 넣는다.

```python
>>> try:
	a = 1 / 0
except ValueError as e:
	print(f'Value Error: {e}')
except Exception as e:
	print(f'Other Exception: {e}')
finally:
	print('Happy birthday Widerplanet!')

	
Other Exception: division by zero
Happy birthday Widerplanet!
```

## 3. 모듈 검색 경로 추가

```sys.path.append(...)``` 를 이용하여 **모듈을 검색할 수 있는 경로를 추가** 할 수 있다.

* 예시: ```sys.path.append('../deep_learning/models')```

## 4. shebang (#!)

**shebang (#!)** 은 **Linux, Mac 등의 OS** 에서,

* **스크립트 코드 최상단** 에서
* **인터프리터 (interpreter) 의 절대 경로** 를 지정 (어떤 인터프리터의 명령어 집합인지 알려주는) 하는 것이다.

일반적으로 다음과 같이 ```env``` 안에 있는 ```python``` 또는 ```python3``` 을 사용한다.

* ```#!/usr/bin/env``` 를 사용하면 **절대 경로에 상관없이, Python 인터프리터의 위치를 찾아 준다.**

```python
#!/usr/bin/env python3
# test.py
```

* 이때, 해당 Python 코드 (```test.py```) 에 대한 실행 권한이 필요하다. (```chmod +x test.py```)

