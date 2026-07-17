
## 목차

* [1. 객체 instance 의 private dictionary](#1-객체-instance-의-private-dictionary)
* [2. 상속의 원리](#2-상속의-원리)
* [3. 메서드 찾기 순서 (MRO)](#3-메서드-찾기-순서-mro)
  * [3-1. MRO의 기본](#3-1-mro의-기본)
  * [3-2. 다중 상속](#3-2-다중-상속)
* [4. 프라이빗 어트리뷰트와 관리 어트리뷰트](#4-프라이빗-어트리뷰트와-관리-어트리뷰트)
  * [4-1. 프라이빗 어트리뷰트 (private attribute)](#4-1-프라이빗-어트리뷰트-private-attribute)
  * [4-2. 관리 어트리뷰트 (managed attribute)](#4-2-관리-어트리뷰트-managed-attribute)
* [5. 속성 (property)](#5-속성-property)
* [6. ```__slots__``` 애트리뷰트](#6-slots-애트리뷰트)

## 1. 객체 instance 의 private dictionary

* Class의 객체 (instance) 마다, 이에 대응되는 **private dictionary** 가 생성된다.
* 이 private dictionary 는 ```object.__dict__``` 로 확인할 수 있다.

```python
>>> class Resume3:
	def __init__(self, name: str, company_list: list):
		self.name = name
		self.company_list = company_list

	def get_company_count(self):
		return len(self.company_list)

	
>>> my_resume = Resume3(name='hskim',
		        company_list=['qara', 'kaier', 'motov', 'widerplanet'])
>>> 
>>> my_resume.__dict__
{'name': 'hskim', 'company_list': ['qara', 'kaier', 'motov', 'widerplanet']}
>>> my_resume.__class__
<class '__main__.Resume3'>
```

## 2. 상속의 원리

* 클래스는 다른 클래스로부터 상속할 수 있으며, **```Class.__bases__``` 를 사용하면 부모 클래스로의 링크를 확인할 수 있다.**

```python
>>> class A():
	def __init__(self):
		pass

	
>>> class B():
	def __init__(self):
		pass

	
>>> class C(A, B):
	def __init__(self):
		pass

	
>>> A.__bases__
(<class 'object'>,)
>>> B.__bases__
(<class 'object'>,)
>>> C.__bases__
(<class '__main__.A'>, <class '__main__.B'>)
```

## 3. 메서드 찾기 순서 (MRO)

### 3-1. MRO의 기본

* Python의 Class 간 상속 관계를 나타내는 **상속 사슬** 은 해당 클래스의 ```MRO``` attribute에 저장된다.
* 이 상속 사슬, 즉 **메서드 찾기 순서 (Method Resolution Order)** 라고 한다.
  * 동일한 이름의 method가 등장할 때, **MRO 에서 첫 번째로 일치하는 class 의 해당 method 가 선택** 된다.

```python

"""상속 관계 그래프:
A <---+
      C <--- D
B <---+
"""

>>> class D(C):
	def __init__(self):
		pass

	
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

### 3-2. 다중 상속

* **다중 상속 (여러 개의 class를 상속하는 것)** 에서는 다음과 같은 방법으로 MRO를 실시한다.
  * 이를 **협동 다중 상속 (cooperative multiple inheritance)** 이라고 한다.
  * 알고리즘의 이름은 **C3 선형화 (Linearization)** 이다.

```
1. 부모 Class보다, 자식 (상속받는) Class 를 먼저 확인한다.
2. 부모가 둘 이상인 경우에는, 리스트된 순서대로 확인한다.
```

* 예제

```python
"""상속 관계 그래프:
    |--- F <--|
E <-|         +--- H
    |--- G <--|
"""

>>> class E():
	def __init__(self):
		pass

	
>>> class F(E):
	def __init__(self):
		pass

	
>>> class G(E):
	def __init__(self):
		pass

	
>>> class H(F, G):
	def __init__(self):
		pass

	
>>> H.__mro__
(<class '__main__.H'>, <class '__main__.F'>, <class '__main__.G'>, <class '__main__.E'>, <class 'object'>)
```

* 다중 상속 시, ```super()``` 를 통해 MRO의 **다음 순서 클래스의 해당 method** 를 사용할 수 있다.

## 4. 프라이빗 어트리뷰트와 관리 어트리뷰트

* Python의 다음과 같은 문제점은 **내부 구현을 따로 분리** 할 때 이슈가 된다.
  * 객체의 내부를 쉽게 확인, 수정 가능
  * access control 에 대한 개념이 detail 하지 않음 (기껏해야 'private class member' 수준)

### 4-1. 프라이빗 어트리뷰트 (private attribute)

* 이름이 ```_``` 로 시작하는 attribute는 **private attribute (내부 구현)** 로 간주한다.
* 이것은 **프로그래밍 스타일 (코딩 스타일, 코딩 컨벤션)** 이며, 실제로는 해당 attribute의 값을 확인, 변경이 가능하다.

### 4-2. 관리 어트리뷰트 (managed attribute)

* Python의 attribute 값 할당의 문제점은 **attribute의 값을 형식의 제한 없이 수정** 할 수 있다는 것이다.
* 이를 방지하기 위해, **attribute의 값을 확인, 수정할 때 추가적인 검사를 하기 위한 attribute (= 관리 어트리뷰트)** 를 도입할 수 있다.

```python
>>> class Resume4:
	def __init__(self, name: str, picture_url: str, company_list: list):
		self.name = name
		self.company_list = company_list
		self.set_picture_url(picture_url)
	
    def get_company_count(self):
		return len(self.company_list)
	
    def get_picture_url(self):
		if hasattr(self, '_picture_url'):
			return self._picture_url
		else:
			raise Exception('picture URL not defined')
	
    def set_picture_url(self, picture_url):
		if not isinstance(picture_url, str):
			raise TypeError('expected string')
		if not picture_url.startswith('http'):
			raise Exception('picture URL must be a URL')
		self._picture_url = picture_url
```
	
```python	
>>> my_resume = Resume4(name='hskim',
		        picture_url='https://avatars.githubusercontent.com/u/32893014?v=4',
		        company_list=['qara', 'kaier', 'motov', 'artistcompany'])
>>> 
>>> my_resume.get_picture_url()
'https://avatars.githubusercontent.com/u/32893014?v=4'
>>> my_resume.set_picture_url(1234)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    my_resume.set_picture_url(1234)
  File "<pyshell#40>", line 15, in set_picture_url
    raise TypeError('expected string')
TypeError: expected string
>>> my_resume.set_picture_url('cdn-avatars.huggingface.co/v1/production/uploads/664978f751dae61645b3aaa9/RwD-XTf8JaKwNPeaqovgo.png')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    my_resume.set_picture_url('cdn-avatars.huggingface.co/v1/production/uploads/664978f751dae61645b3aaa9/RwD-XTf8JaKwNPeaqovgo.png')
  File "<pyshell#40>", line 17, in set_picture_url
    raise Exception('picture URL must be a URL')
Exception: picture URL must be a URL
>>> my_resume.set_picture_url('https://cdn-avatars.huggingface.co/v1/production/uploads/664978f751dae61645b3aaa9/RwD-XTf8JaKwNPeaqovgo.png')
>>> my_resume.get_picture_url()
'https://cdn-avatars.huggingface.co/v1/production/uploads/664978f751dae61645b3aaa9/RwD-XTf8JaKwNPeaqovgo.png'
```

## 5. 속성 (property)

다음과 같이 ```@property``` 와 ```@shares.setter``` 를 이용하여 getter, setter method 를 트리거할 수 있다.

```python
>>> class Resume5:
	def __init__(self, name: str, picture_url: str = None, company_list: list = None):
		self.name = name
		self.company_list = company_list
		if picture_url is not None:
			self.set_picture_url(picture_url)
	def get_company_count(self):
		return len(self.company_list)
	
        @property
	def picture_url(self):
		if hasattr(self, '_picture_url'):
			return self._picture_url
		else:
			raise Exception('picture URL not defined')
	
        @picture_url.setter
	def picture_url(self, picture_url):
		if not isinstance(picture_url, str):
			raise TypeError('expected string')
		if not picture_url.startswith('http'):
			raise Exception('picture URL must be a URL')
		self._picture_url = picture_url
```

```python
>>> my_resume = Resume5(name='hskim',
		        company_list=['qara', 'kaier', 'motov', 'artistcompany'])
>>> my_resume.picture_url
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    my_resume.picture_url
  File "<pyshell#57>", line 14, in picture_url
    raise Exception('picture URL not defined')
Exception: picture URL not defined
>>> my_resume.picture_url = 1234
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    my_resume.picture_url = 1234
  File "<pyshell#57>", line 18, in picture_url
    raise TypeError('expected string')
TypeError: expected string
>>> my_resume.picture_url = 'avatars.githubusercontent.com/u/32893014?v=4'
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    my_resume.picture_url = 'avatars.githubusercontent.com/u/32893014?v=4'
  File "<pyshell#57>", line 20, in picture_url
    raise Exception('picture URL must be a URL')
Exception: picture URL must be a URL
>>> my_resume.picture_url = 'https://avatars.githubusercontent.com/u/32893014?v=4'
>>> my_resume.picture_url
'https://avatars.githubusercontent.com/u/32893014?v=4'
```

## 6. ```__slots__``` 애트리뷰트

```__slots__``` 애트리뷰트를 이용하여 **애트리뷰트 이름의 집합을 제한** 할 수 있다.

```python
>>> class Test:
	__slots__ = ('name', 'age')
	def __init__(self, name):
		self.name = name

		
>>> a = Test(name='test')
>>> a.age = 30
>>> a.job = 'ML engineer'
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.job = 'ML engineer'
AttributeError: 'Test' object has no attribute 'job'
```

* 이를 통해 다음과 같은 효과를 얻을 수 있다.
  * 성능 향상
  * 메모리의 효율적인 사용
