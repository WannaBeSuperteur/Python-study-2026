
## 목차

* [1. 디스크립터의 개요](#1-디스크립터의-개요)
  * [1-1. 디스크립터의 매직 메서드 설명](#1-1-디스크립터의-매직-메서드-설명)
  * [1-2. 디스크립터의 기본 예시](#1-2-디스크립터의-기본-예시)
* [2. 디스크립터 예시](#2-디스크립터-예시)
* [3. 디스크립터의 유형](#3-디스크립터의-유형)

## 1. 디스크립터의 개요

디스크립터는 **디스크립터 프로토콜을 구현한 클래스의 객체 (instance)** 이다.

* 디스크립터는 **구현을 위해 최소 2개의 클래스** 가 필요하다.
* 디스크립터 객체는 **클라이언트 클래스 instance의 속성이 아닌, 클래스 본문에 정의하여 여러 instance가 값을 공유하는 속성 형태로 선언** 되어야 한다.
  * 이와 같이 클래스 본문에 정의되는 속성을 **클래스 속성 (class attribute)** 이라고 한다. 
* 디스크립터 클래스는 ```__get__``` ```__set__``` ```__delete__``` ```__set_name__``` 중 최소 1개의 magic method 를 포함해야 한다.

### 1-1. 디스크립터의 매직 메서드 설명

디스크립터의 각 매직 메서드의 의미는 다음과 같다.

* ```owner``` 는 디스크립터를 호출한 객체의 클래스 (= ```instance.__class__```), 즉 **클라이언트 클래스** 에 해당한다.
* 디스크립터 속성에 값 할당 시, ```__set__``` 메서드를 반드시 구현하여 부작용을 방지해야 한다.

| 매직 메서드             | 서명                                    | 의미                                                |
|--------------------|---------------------------------------|---------------------------------------------------|
| ```__get__```      | ```__get__(self, instance, owner)```  | 클래스 또는 그 인스턴스의 속성 (property) 반환                   |
| ```__set__```      | ```__set__(self, instance, value)```  | 디스크립터를 호출한 객체 (클라이언트 instance) 의 attribute에 값을 할당 |
| ```__delete__```   | ```__delete__(self, instance)```      | instance 의 attribute 삭제                           |
| ```__set_name__``` | ```__set_name__(self, owner, name)``` | 디스크립터에 해당 메서드를 추가하여, 필요한 이름 지정                    |

### 1-2. 디스크립터의 기본 예시

아래와 같이 **클라이언트 클래스 instance에서 descriptor 속성에 접근** 하면, **인스턴스 대신 ```__get__``` 메서드의 반환값을 표시** 한다.

```python
>>> class TestDescriptor:
	def __get__(self, instance, owner):
		if instance is None:
			return self
		info_dict = {
			'self.__class__.__name__ (클래스 이름)': self.__class__.__name__,
			'instance (인스턴스)': instance,
			'owner (디스크립터를 호출한 객체의 클래스)': owner
		}
		print(info_dict)
		return instance

	
>>> class TestClient:
	descriptor = TestDescriptor()

	
>>> test_client = TestClient()
>>> test_client.descriptor
{'self.__class__.__name__ (클래스 이름)': 'TestDescriptor', 'instance (인스턴스)': <__main__.TestClient object at 0x00000198047C19A0>, 'owner (디스크립터를 호출한 객체의 클래스)': <class '__main__.TestClient'>}
<__main__.TestClient object at 0x00000198047C19A0>
```

## 2. 디스크립터 예시

* 아래 예시는 **hr 권한을 가진 사용자만 수습 평가 결과를 수정, 삭제할 수 있는** 예제이다.

```python
>>> class ProbationResult:
	def __init__(self, required_perm=None):
		self.required_perm = required_perm
		self._name = None

	def __get__(self, employee, owner):
		print(f'__get__\n - employee={employee}\n - owner={owner}')
		return employee.__dict__

	def __set_name__(self, owner, name):
		print(f'__set_name__\n - owner={owner}\n - name={name}')
		self._name = name

	def __set__(self, employee, value):
		print(f'__set__\n - employee={employee}\n'
		      + f' - value={value}\n'
		      + f' - self._name={self._name}\n'
		      + f' - employee.__dict__={employee.__dict__}')

		if self.required_perm not in employee.permissions:
			raise ValueError('permission denied (1)')
		if value is None:
			raise ValueError('Value is None.')

		employee.__dict__[self._name] = value

	def __delete__(self, employee):
		print(f'__delete__\n - employee={employee}\n'
		      + f' - self._name={self._name}\n'
		      + f' - employee.__dict__={employee.__dict__}')

		if self.required_perm not in employee.permissions:
			raise ValueError('permission denied (2)')

		employee.__dict__[self._name] = None

		
>>> class Employee:
	probation_result = ProbationResult(required_perm="hr")

	def __init__(self, name: str, permission_list: list):
		self.name = name
		self.permissions = permission_list or []
	def __str__(self):
		return f'이름: {self.name}'

	
__set_name__
 - owner=<class '__main__.Employee'>
 - name=probation_result
```

* hr 권한을 **가진** Employee 객체로 실행 시

```python
>>> hr_admin = Employee("hr", ["hr", "admin"])

>>> hr_admin.probation_result = "김민우: 수습 탈락(59/100), 오로라: 수습 통과(80/100), 안지현: 수습 연장(66/100)"
__set__
 - employee=이름: hr
 - value=김민우: 수습 탈락(59/100), 오로라: 수습 통과(80/100), 안지현: 수습 연장(66/100)
 - self._name=probation_result
 - employee.__dict__={'name': 'hr', 'permissions': ['hr', 'admin']}

>>> hr_admin.probation_result
__get__
 - employee=이름: hr
 - owner=<class '__main__.Employee'>
{'name': 'hr', 'permissions': ['hr', 'admin'], 'probation_result': '김민우: 수습 탈락(59/100), 오로라: 수습 통과(80/100), 안지현: 수습 연장(66/100)'}

>>> del hr_admin.probation_result
__delete__
 - employee=이름: hr
 - self._name=probation_result
 - employee.__dict__={'name': 'hr', 'permissions': ['hr', 'admin'], 'probation_result': '김민우: 수습 탈락(59/100), 오로라: 수습 통과(80/100), 안지현: 수습 연장(66/100)'}

>>> hr_admin.probation_result
__get__
 - employee=이름: hr
 - owner=<class '__main__.Employee'>
{'name': 'hr', 'permissions': ['hr', 'admin'], 'probation_result': None}
```

* hr 권한을 **가지지 않은** Employee 객체로 실행 시

```python
>>> user = Employee("hs.kim", ["ai_engineer"])

>>> hr_admin.probation_result = "김홍식: 수습 탈락(39/100)"
__set__
 - employee=이름: hr
 - value=김홍식: 수습 탈락(39/100)
 - self._name=probation_result
 - employee.__dict__={'name': 'hr', 'permissions': ['hr', 'admin'], 'probation_result': None}

>>> user.probation_result
__get__
 - employee=이름: hs.kim
 - owner=<class '__main__.Employee'>
{'name': 'hs.kim', 'permissions': ['ai_engineer']}

>>> user.probation_result = "김홍식: 수습 통과(92/100)"
__set__
 - employee=이름: hs.kim
 - value=김홍식: 수습 통과(92/100)
 - self._name=probation_result
 - employee.__dict__={'name': 'hs.kim', 'permissions': ['ai_engineer']}
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    user.probation_result = "김홍식: 수습 통과(92/100)"
  File "<pyshell#293>", line 21, in __set__
    raise ValueError('permission denied (1)')
ValueError: permission denied (1)

>>> del user.probation_result
__delete__
 - employee=이름: hs.kim
 - self._name=probation_result
 - employee.__dict__={'name': 'hs.kim', 'permissions': ['ai_engineer']}
Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    del user.probation_result
  File "<pyshell#293>", line 33, in __delete__
    raise ValueError('permission denied (2)')
ValueError: permission denied (2)
```

## 3. 디스크립터의 유형

디스크립터의 유형은 크게 다음과 같이 2가지로 분류할 수 있다.

| 유형                                | 설명                                               |
|-----------------------------------|--------------------------------------------------|
| 데이터 디스크립터 (data descriptor)       | ```__set__``` 또는 ```__delete__``` 메서드가 구현된 디스크립터 |
| 비-데이터 디스크립터 (non-data descriptor) | ```__get__``` 메서드만을 구현한 디스크립터                    |

* 참고로 ```__set_name__``` 메서드의 존재 여부는 이 분류와 무관하다.

### 3-1. 디스크립터의 유형별 특징

**데이터 디스크립터 (data descriptor)** 의 특징은 다음과 같다.

* 데이터 디스크립터의 속성 조회 시, **객체의 ```__dict__``` 대신 클래스의 descriptor를 먼저 조회하여 그 결과를 반환** 한다.

```python
>>> class ExampleDataDescriptor:
	def __get__(self, instance, owner):
		print(f'__get__\n - instance={instance}\n'
		      + f' - owner={owner}\n'
		      + f' - instance.__dict__={instance.__dict__}')

		if instance is None:
			return self
		return 'instance'

	def __set__(self, instance, value):
		print(f'__set__\n - instance={instance}\n'
		      + f' - value={value}\n'
		      + f' - instance.__dict__={instance.__dict__}')
		
		instance.__dict__["test"] = value
		print(f'instance.__dict__={instance.__dict__}')

		
>>> class ClientClass:
	data_descriptor = ExampleDataDescriptor()

	
>>> client = ClientClass()
>>> client.data_descriptor
__get__
 - instance=<__main__.ClientClass object at 0x00000198047E1940>
 - owner=<class '__main__.ClientClass'>
 - instance.__dict__={}
'instance'

>>> client.data_descriptor = 'test'
__set__
 - instance=<__main__.ClientClass object at 0x00000198047E1940>
 - value=test
 - instance.__dict__={}
instance.__dict__={'test': 'test'}

>>> client.data_descriptor
__get__
 - instance=<__main__.ClientClass object at 0x00000198047E1940>
 - owner=<class '__main__.ClientClass'>
 - instance.__dict__={'test': 'test'}
'instance'  # data_descriptor 속성 조회 시, 클래스의 descriptor 기준 __get__ 메서드 반환값인 'instance'를 반환

>>> vars(client)
{'test': 'test'}  # 객체의 dictionary 는 정상적으로 업데이트됨
>>> client.__dict__
{'test': 'test'}
>>> client.__dict__['test']
'test'
```

* 비 데이터 디스크립터는 이와 같은 일이 없는데, 그 이유는 **```__set__``` 메서드가 객체의 dict 보다 우선순위가 높기** 때문이다.
