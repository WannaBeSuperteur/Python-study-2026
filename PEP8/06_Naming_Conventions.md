
## Naming Conventions 기본

* API의 public part에 보이는 이름들은 **구현보다는 사용성에 초점을 두어야** 한다.

## Naming Styles

* 대표적인 네이밍 스타일

| Naming Style                                             | 예시                                       |
|----------------------------------------------------------|------------------------------------------|
| single lowercase letter                                  | ```b```                                  |
| single uppercase letter                                  | ```B```                                  |
| lowercase                                                | ```lowercase```                          |
| lowercase with underscores                               | ```lowercase_with_underscores```         |
| uppercase                                                | ```UPPERCASE```                          |
| uppercase with underscores                               | ```UPPERCASE_WITH_UNDERSCORES```         |
| captialized words                                        | ```CapitalizedWords```                   |
| mixed case                                               | ```mixedCase```                          |
| captialized words with underscores **(not recommended)** | ```Capitalized_Words_With_Underscores``` |

* 추가적인 네이밍 스타일

| Naming Style                           | 예시                                               | 설명                                                                                                      |
|----------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| single leading underscore              | ```_single_leading_underscore```                 | - **internal use (해당 코드 파일 내부에서만 사용)** 를 의미<br>- ```from xxx import *``` 에 의해 **외부에서 import 되지 않음**     |
| single trailing underscore             | ```single_trailing_underscore_```                | 파이썬에서 미리 정의된 키워드 (예: ```class```) 와 겹치지 않게 하기 위해 사용<br>(예: ```class_```)                                |
| double leading underscore              | ```__double_leading_underscore```                | class attribute 의 이름에 사용<br>(예: ```FooBar``` class의 ```__boo``` attribute 는 ```_FooBar__boo``` 와 같이 사용) |
| double leading and trailing underscore | ```__double_leading_and_trailing_underscore__``` | ```__init__```, ```__import__```, ```__file__``` 등 네임스페이스에서 사용                                          |

## 그 외의 Naming 규칙들

* ```l``` (lower L), ```O``` (upper o), ```I``` (upper i) 를 변수명으로 사용 금지
* ASCII 와 호환되어야 함 [(상세 규칙)](https://peps.python.org/pep-3131/#policy-specification)
* 이름 유형 별 사용해야 하는 형식
  * Class Name은 ```CapWords``` 형식으로 작성
  * Type Variable (Type을 나타내는 이름, 예를 들어 ```Uri```, ```Vector```) 은 ```CapWords``` 형식으로 작성
  * 함수 및 변수 이름은 ```lowercase``` 로 함 (```_``` 를 사용하여 가독성 향상)
  * mixedCase 는 문맥상 해당 스타일이 지배적으로 쓰이는 예외적인 경우에 한해서 사용
* method의 first argument
  * **instance method:** class 안에 있는 ```def xxx(self, ...):``` 와 같은 method
  * **class method:** ```@classmethod def xxx(cls):``` 와 같은 method로, **클래스의 객체가 아닌 클래스 자체로부터 호출**

| instance method | class method |
|-----------------|--------------|
| ```self```      | ```cls```    |

* 상수 (Constant) 는 **모듈 레벨에서 정의** 되며, **대문자 + underscore** (= uppercase with underscores) 형태

## Pythonic한 Naming Convention 가이드라인

* Public attribute에는 **leading underscore 가 없어야** 함
* Public attribute 이름이 **예약된 키워드와 충돌** 하는 경우, 해당 attribute 이름의 뒤쪽에 ```_``` 를 1개 추가
* 간단한 public data attribute 의 경우, attribute 이름만을 노출하는 것이 좋음
  * 즉, getter, setter 와 같은 함수/메서드 요소를 만들지 말 것
* subclass 의 경우 앞에 2개의 ```_``` 를 추가하고, trailing underscore 를 추가하지 않는 것이 좋음
  * 위의 ```_FooBar__boo``` 예시 참고

