
## 목차

* [1. 컨텍스트 관리자 (Context Manager)](#1-컨텍스트-관리자-context-manager)
* [2. 컴프리헨션 (Comprehension) 및 할당 표현식](#2-컴프리헨션-comprehension-및-할당-표현식)
  * [2-1. 컴프리헨션 및 할당 표현식을 사용하는 이유](#2-1-컴프리헨션-및-할당-표현식을-사용하는-이유)

## 1. 컨텍스트 관리자 (Context Manager)

**컨텍스트 관리자 (Context Manager)** 는 **사전 조건 및 사후 조건이 중요한** 코드를 실행하는 상황에서 유용한 도구이다.

* 컨텍스트 관리자가 사용되는 대표적인 상황은 다음과 같다.
  * 리소스 관리 (파일 열기/닫기)
  * 서비스/소켓에 대한 연결 및 연결 해제

컨텍스트 관리자의 magic method 는 다음과 같다.

| 매직 메서드          | 설명                                                                                                                   |
|-----------------|----------------------------------------------------------------------------------------------------------------------|
| ```__enter__``` | 컨텍스트 진입 (다른 Python 코드 실행이 가능한)                                                                                       |
| ```__exit__```  | 컨텍스트 종료<br>- 컨텍스트 블록 내에서 Exception이 발생한 경우, 해당 Exception을 파라미터로 받음<br>- **```__exit__``` 에서 True를 반환할 때는 명확한 이유 필요** |

컨텍스트 관리자와 관련된 데코레이터 및 클래스는 다음과 같다.

| 데코레이터, 클래스                        | 설명                                                                                 |
|-----------------------------------|------------------------------------------------------------------------------------|
| ```@contextlib.contextmanager```  | 해당 데코레이터가 적용된 함수는 **컨텍스트 매니저로 변환**                                                 |
| ```contextlib.ContextDecorator``` | - 컨텍스트 관리자 안에서 실행되는 함수에 데코레이터 적용하는 로직 제공<br>- 믹스인 클래스 (Mixin Class, 메서드만을 제공하는 형태) |

## 2. 컴프리헨션 (Comprehension) 및 할당 표현식

* Python 3.8 에서 도입된 **할당 표현식 (assignment expression)** 을 통해 **조건식을 조금 더 간단히 표현** 할 수 있다.
* [참고: 02_example.py](02_example.py)

**1. 기존 코드**

```python
interest_set = set()

for person in PERSON_INFO:
    interest = person.get('interest', None)
    if interest is not None:
        interest_set = interest_set.union(interest)
```

**2. 할당 표현식을 사용한 코드**

```python
interest_set = set()

for person in PERSON_INFO:
    if (interest := person.get('interest')) is not None:
        interest_set = interest_set.union(interest)
```

**3. 할당 표현식 + set comprehension 을 사용한 코드**

```python
interest_set = {  # used set comprehension
    item
    for person in PERSON_INFO
    if (interest := person.get('interest')) is not None
    for item in interest
}
```

* 참고로, **더 짧은 코드가 항상 더 좋은 코드는 아니다. (정답은 없다?)**
  * 단, 한 줄 코드는 **이해하기 쉬운 코드가 아니라면 권장하지 않는다.**

### 2-1. 컴프리헨션 및 할당 표현식을 사용하는 이유

* 더 적은 라인으로 동일한 기능 구현 가능 (코드 간소화) + 코드 가독성 향상
* 변환 작업 등이 필요 이상으로 호출되지 않는 **성능 향상** 효과


