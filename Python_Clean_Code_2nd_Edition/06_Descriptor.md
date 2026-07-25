
## 목차

* [1. 디스크립터의 개요](#1-디스크립터의-개요)
  * [1-1. 디스크립터의 매직 메서드 설명](#1-1-디스크립터의-매직-메서드-설명)
  * [1-2. 디스크립터의 기본 예시](#1-2-디스크립터의-기본-예시)

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
