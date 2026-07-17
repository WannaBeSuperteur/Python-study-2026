
## 목차

* [1. 객체 지향 프로그래밍 (OOP) 의 개념](#1-객체-지향-프로그래밍-oop-의-개념)
* [2. 다양한 특수 method](#2-다양한-특수-method)
  * [2-1. 수학 연산을 위한 다양한 특수 method](#2-1-수학-연산을-위한-다양한-특수-method)
  * [2-2. 항목 접근을 위한 특수 method](#2-2-항목-접근을-위한-특수-method)
* [3. 바운드 메서드 (bound method)](#3-바운드-메서드-bound-method)
* [4. attribute 접근 방식](#4-attribute-접근-방식)
* [5. 커스텀 예외 정의하기](#5-커스텀-예외-정의하기)

## 1. 객체 지향 프로그래밍 (OOP) 의 개념

* 코드를 **객체 (object) 의 집합** 을 통해 조직화하는 형태의 프로그래밍
* 객체의 구성

| 구성 요소             | 설명                                           |
|-------------------|----------------------------------------------|
| 데이터 (data)        | 객체가 저장하고 있는 정보, 즉 객체의 상태 (state)             |
| 애트리뷰트 (attribute) | 이 **데이터 (data)** 를 표현하기 위한 **Class에 정의된 속성** |
| 행위 (behavior)     | 객체가 수행할 수 있는 행위/행동                           |
| 메서드 (method)      | 객체의 **행동 (behavior)** 을 함수로 정의한 것            |

## 2. 다양한 특수 method

### 2-1. 수학 연산을 위한 다양한 특수 method

* 참고: ```__del__```, ```__repr__```, ```__add__```, ```__lt__``` 메서드는 [여기](../Python_for_beginners/things_I_didnt_know.md#15-del-repr-add-lt-메서드) 에 정리함.

**1. 수학 연산을 위한 method**

| 특수 method          | 설명                                     |
|--------------------|----------------------------------------|
| ```__add__```      | ```a + b``` → ```a.__add__(b)```       |
| ```__sub__```      | ```a - b``` → ```a.__sub__(b)```       |
| ```__mul__```      | ```a * b``` → ```a.__mul__(b)```       |
| ```__truediv__```  | ```a / b``` → ```a.__truediv__(b)```   |
| ```__floordiv__``` | ```a // b``` → ```a.__floordiv__(b)``` |
| ```__mod__```      | ```a % b``` → ```a.__mod__(b)```       |
| ```__lshift__```   | ```a << b``` → ```a.__lshift__(b)```   |
| ```__rshift__```   | ```a >> b``` → ```a.__rshift__(b)```   |
| ```__and__```      | ```a & b``` → ```a.__and__(b)```       |
| ```__or__```       | ```a \| b``` → ```a.__or__(b)```       |
| ```__xor__```      | ```a ^ b``` → ```a.__xor__(b)```       |
| ```__pow__```      | ```a ** b``` → ```a.__pow__(b)```      |
| ```__neg__```      | ```-a``` → ```a.__neg__()```           |
| ```__invert__```   | ```~a``` → ```a.__invert__()```        |
| ```__abs__```      | ```abs(a)``` → ```a.__abs__()```       |

```python
>>> class Experience():
	def __init__(self, months):
		self.months = months
	def __add__(self, other):
		return self.months + other.months
	def __sub__(self, other):
		return self.months - other.months
	def __mul__(self, other):
		return 'months multiplication not defined'
	def __truediv__(self, other):
		return self.months / other.months
	def __floordiv__(self, other):
		return self.months // other.months
	def __mod__(self, other):
		return self.months % other.months
	def __lshift__(self, other):
		return 'left shift not defined'
	def __rshift__(self, other):
		return 'right shift not defined'
	def __and__(self, other):
		return self.months & other.months
	def __or__(self, other):
		return self.months | other.months
	def __xor__(self, other):
		return self.months ^ other.months
	def __neg__(self):
		return (-1) * self.months
```

* 실행 결과

```python
>>> widerplanet = Experience(months=12*16)
>>> my_career = Experience(months=12*3+10)
>>> widerplanet + my_career
238
>>> widerplanet - my_career
146
>>> widerplanet * my_career
'months multiplication not defined'
>>> widerplanet / my_career
4.173913043478261
>>> widerplanet // my_career
4
>>> widerplanet % my_career
8
>>> widerplanet << my_career
'left shift not defined'
>>> widerplanet >> my_career
'right shift not defined'
>>> widerplanet & my_career
0
>>> widerplanet | my_career
238
>>> widerplanet ^ my_career
238
>>> -widerplanet
-192
>>> -my_career
-46
```

### 2-2. 항목 접근을 위한 특수 method

* PyTorch Dataset 에서도 많이 사용하므로 **머신러닝 엔지니어로서 반드시 알아두어야 한다.**

| 특수 method         | 설명                                               |
|-------------------|--------------------------------------------------|
| ```__len__```     | ```len(a)``` (길이 반환) → ```a.__len__()```         |
| ```__getitem__``` | ```a[i]``` → ```a.__getitem__(self, i)```        |
| ```__setitem__``` | ```a[i] = v``` → ```a.__setitem__(self, i, v)``` |
| ```__delitem__``` | ```del a[i]``` → ```a.__delitem__(self, i)```    |

```python
>>> class Resume:
	def __init__(self, name: str, company_list: list):
		self.name = name
		self.company_list = company_list
	def __getitem__(self, i):
		return self.company_list[i]
	def __setitem__(self, i, company_name):
		self.company_list[i] = company_name

        
>>> my_resume = Resume(name='hskim',
		       company_list=['qara', 'kaier', 'motov', 'widerplanet'])
>>> my_resume[0]
'qara'
>>> my_resume[3]
'widerplanet'
>>> my_resume[3] = 'artistcompany'
>>> my_resume[3]
'artistcompany'
```

## 3. 바운드 메서드 (bound method)

**바운드 메서드 (bound method)** 는 **```()``` 에 의해 호출되지 않은 method** 를 말한다.

* 어느 인스턴스에서 왔는지를 반환한다.
* bound method 는 **오류의 원인이 되고 디버깅하기 힘들어지므로 사용하지 말아야 한다.**

```python
>>> class Resume2:
	def __init__(self, name: str, company_list: list):
		self.name = name
		self.company_list = company_list
	def __getitem__(self, i):
		return self.company_list[i]
	def __setitem__(self, i, company_name):
		self.company_list[i] = company_name
	def get_company_count(self):
		return len(self.company_list)

	
>>> my_resume = Resume2(name='hskim',
		        company_list=['qara', 'kaier', 'motov', 'widerplanet'])

>>> my_resume.get_company_count()  # () 를 포함한 정상적인 호출
4
>>> my_resume.get_company_count  # () 를 제외한 호출 (bound method)
<bound method Resume2.get_company_count of <__main__.Resume2 object at 0x000001D5479D6E20>>
```

## 4. attribute 접근 방식

attribute 에 접근하는 방식으로 다음 방법을 사용할 수 있다.

| 접근 방법                             | 설명                                                             |
|-----------------------------------|----------------------------------------------------------------|
| ```getattr(obj, 'name')```        | ```obj.name``` 과 동일한 기능, **attribute 참조**                      |
| ```setattr(obj, 'name', value)``` | ```obj.name = value``` 와 동일한 기능, **attribute 수정**              |
| ```delattr(obj, 'name')```        | ```del obj.name``` 과 동일한 기능, **"해당 객체에서" 해당 attribute 자체를 삭제** |
| ```hasattr(obj, 'name')```        | 해당 attribute 의 존재 여부 확인                                        |

```python
>>> my_resume = Resume2(name='hskim',
		        company_list=['qara', 'kaier', 'motov', 'widerplanet'])
>>> getattr(my_resume, 'name')
'hskim'
>>> setattr(my_resume, 'name', 'hs.kim')
>>> getattr(my_resume, 'name')
'hs.kim'
>>> hasattr(my_resume, 'company_list')
True
>>> getattr(my_resume, 'company_list')
['qara', 'kaier', 'motov', 'widerplanet']
>>> delattr(my_resume, 'company_list')
>>> hasattr(my_resume, 'company_list')
False
>>> getattr(my_resume, 'company_list')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    getattr(my_resume, 'company_list')
AttributeError: 'Resume2' object has no attribute 'company_list'
>>> my_resume
<__main__.Resume2 object at 0x000001D5479C0160>
```

* 동일 class의 **신규 객체** 생성 시에는 ```delattr``` 로 삭제된 attribute가 존재한다.

```python
>>> my_new_resume = Resume2(name='hskim',
	   	            company_list=['qara', 'kaier', 'motov', 'widerplanet'])
>>> hasattr(my_resume, 'company_list')
False
>>> hasattr(my_new_resume, 'company_list')
True
>>> getattr(my_new_resume, 'company_list')
['qara', 'kaier', 'motov', 'widerplanet']
```

## 5. 커스텀 예외 정의하기

커스텀 예외 (사용자 정의 예외) 는 **클래스를 통해 정의할 수 있다.**

* ```Exception``` 으로부터 상속하는 경우 (모든 예외는 기본적으로 Exception 으로부터 상속)

```python
class MyCustomError(Exception):
    ...
```

* ```OOOError``` 등 예외 계층을 직접 만드는 경우

```python
class MyCustomError(NetworkError):
    ...
```

* 예제

```python
>>> class ProbationFailedError(Exception):
	pass

>>> def get_status(months: int):
	if months <= 3:
		raise ProbationFailedError
	else:
		print(f"{months // 12} 년 {months % 12} 개월 재직 중")

		
>>> get_status(30)
2 년 6 개월 재직 중
>>> get_status(3)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    get_status(3)
  File "<pyshell#153>", line 3, in get_status
    raise ProbationFailedError
ProbationFailedError
```
