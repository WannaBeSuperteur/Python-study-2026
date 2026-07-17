
## 목차

* [1. 클린 코드 (Clean code) 의 의미 및 중요성](#1-클린-코드-clean-code-의-의미-및-중요성)
  * [1-1. 기술 부채와 코드 스멜](#1-1-기술-부채와-코드-스멜)
  * [1-2. 프로젝트 코딩 스타일 준수](#1-2-프로젝트-코딩-스타일-준수)
* [2. 문서화](#2-문서화)
  * [2-1. Docstring](#2-1-docstring)
  * [2-2. 어노테이션 (Annotation)](#2-2-어노테이션-annotation)
* [3. 코드 리뷰의 기준](#3-코드-리뷰의-기준)
* [4. 코드 포매팅, 레이아웃 등의 자동 검사](#4-코드-포매팅-레이아웃-등의-자동-검사)
  * [4-1. 자동 검사 도구 실행 결과](#4-1-자동-검사-도구-실행-결과)
  * [4-2. 자동 포매팅](#4-2-자동-포매팅)
* [5. Makefile 사용하기](#5-makefile-사용하기)

## 1. 클린 코드 (Clean code) 의 의미 및 중요성

**클린 코드 (Clean code)** 는 **다른 엔지니어가 코드를 읽고 유지 관리할 수 있는 코드** 를 의미한다.

* 공식적인 측정 방법이 없으므로, 무엇이 클린 코드인지에 대해서는 **정답은 없지만, 특정 조직 내에서의 정답은 있을 수 있다.**

클린 코드의 중요성은 다음과 같다.

* 민첩한 개발 및 지속적 배포 가능
* 일정하고 꾸준하게, 예측 가능한 속도로 업무 진행 가능 **(개발 일정의 불확실성 감소)**
* **수정 가능한 코드를 위한 절대적인 요구사항**

### 1-1. 기술 부채와 코드 스멜

* **기술 부채** : 적당한 타협 등의 결과로 생긴 소프트웨어 결함
* **코드 스멜 (Code Smell)** : 장기적으로 코드에 나쁜 영향을 미치는, 일종의 **잘못된 코드에 대한 신호**

### 1-2. 프로젝트 코딩 스타일 준수

* 좋은 코드의 가장 핵심적인 특징은 **일관성 (일관된 구조화)** 이다.
* 모든 팀원의 코드가 **일관성을 유지 (표준화된 구조를 사용) 하고 있을수록**, 다음과 같은 장점이 있다.
  * 코드의 패턴을 신속하게 파악할 수 있음 **(빠른 이해)**
  * 평소 패턴과 다를 때, **실수 및 오류 가능성을 쉽게 감지할 수 있음**
* 팀, 회사 차원에서 준수 중인 코딩 표준이 없다면, [PEP-8](../PEP8) 을 따르는 것이 좋음

## 2. 문서화

* 코드의 문서화는 **코드에 주석 (comment) 을 추가하는 것과는 다르다.**
* 코드의 주석은 **가능한 한 적을수록 좋다.**
  * 코드 자체가 코드를 설명하도록 해야 한다.
  * 즉, 주석이 필요하지 않을 만큼 명백한 이름 (함수명, 변수명 등) 을 지정해야 한다.
  * 주석의 추가가 필요한 것은 **코드가 어딘가 잘못되었다는 징후** 이다.
  * **주석 처리된 코드** 는 혼란을 가져올 가능성이 높으므로 **삭제해야 한다.**
* 문서화의 범위
  * 문서는 **산출물에 포함** 되어야 한다.
  * 코드 변경 시 **wiki, README.md, Docstring 등을 같이 업데이트** 해야 한다.

### 2-1. Docstring

Docstring은 **소스 코드에 포함된 문서 (documentation) 로, 주석 (comment) 과는 다르다.**

* Docstring의 필요성
  * 모듈, 클래스, 함수 등에 대한 문서 (동작 방식, 입출력 등에 대한 설명) 제공
  * 프로그램 디자인 및 아키텍처의 문서화
  * Python은 **데이터 타입이 동적이기 때문에, 입출력 정보 제공에 필요**

### 2-2. 어노테이션 (Annotation)

* [참고: Practical Python Programming > Program Organization](../Practical_Python_programming/03_Program_Organization.md#1-1-docstring-및-type-annotation)
* **어노테이션 (annotation)** 은 함수 인자로 오는 값에 대한 **힌트 (hint)** 를 제공하는 것이다.
  * 이것은 **type을 강제하지 않아서 예상 type을 알기 어려운** Python의 특성상 중요하다.

```python
class VectorInSpace:
    x: float
    y: float
    z: float

def create_vector(x: float, y: float, z: float) -> VectorInSpace:
    """Create a vector <x, y, z> in 3D space."""
    ...
```

* annotation으로 docstring을 완벽히 대체할 수 없고, **annotation과 docstring은 상호 보완적으로 사용** 해야 한다.

## 3. 코드 리뷰의 기준

* 좋은 코드 여부를 파악할 수 있는 것은 **오직 사람만이 할 수 있다.**
* 코드 리뷰 시 핵심 체크 사항
  * 동료 개발자 (팀의 신규 입사자/합류자 포함) 의 **이해 가능성**
  * **업무 도메인에 대한** 언급 여부

## 4. 코드 포매팅, 레이아웃 등의 자동 검사

* 코드 포매팅, 레이아웃 등은 **검사를 자동화** 해야 한다.
* 이를 통해, **PEP-8 준수 여부 등을 빌드 시 자동으로 체크하고, 위반 시 빌드가 실패** 하도록 해야 한다.
* 자동 검사 팁
  * **annotation 을 정확하게 작성** 해야 ```mypy``` 등 자동화된 검증 도구를 신뢰성 있게 사용할 수 있다.
* 자동 검사 도구

| 자동 검사 도구                        | 자동 검사 범위             |
|---------------------------------|----------------------|
| ```mypy``` ```pytype```         | 데이터 타입 (data type) 등 |
| ```pycodestyle``` ```flake-8``` | PEP-8 준수 여부 판단       |
| ```pylint```                    | (가장 엄격한 수준)          |

### 4-1. 자동 검사 도구 실행 결과

* 대상 파일: [01_example.py](01_Code_Formatting_and_Tools.md)

**1. mypy**

```commandline
(base) PS D:\Python-study-2026\Python_Clean_Code_2nd_Edition> mypy 01_example.py              
01_example.py:19: error: Need type annotation for "result" (hint: "result: list[<type>] = ...")  [var-annotated]
Found 1 error in 1 file (checked 1 source file)
```

**2. pycodestyle**

```commandline
(base) PS D:\Python-study-2026\Python_Clean_Code_2nd_Edition> pycodestyle 01_example.py
01_example.py:16:80: E501 line too long (90 > 79 characters)
```

**3. pylint**

```commandline
(base) PS D:\Python-study-2026\Python_Clean_Code_2nd_Edition> pylint 01_example.py
************* Module 01_example
01_example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
01_example.py:1:0: C0103: Module name "01_example" doesn't conform to snake_case naming style (invalid-name)
01_example.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
01_example.py:4:13: C0103: Argument name "n" doesn't conform to snake_case naming style (invalid-name)
01_example.py:9:8: C0103: Variable name "d" doesn't conform to snake_case naming style (invalid-name)
01_example.py:16:30: C0103: Argument name "n" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 7.39/10
```

### 4-2. 자동 포매팅

* 표준 준수 여부 확인은 물론 **코드 형식을 자동으로 지정** 하게 하는 도구도 있다.

| 도구                                    | 기능                                          |
|---------------------------------------|---------------------------------------------|
| flake8 등                              | - PEP-8 준수 여부 검사<br>- PEP-8 표준 준수 코드로 자동 변환 |
| [black](https://github.com/psf/black) | 고유한 방식으로의 코드 형식 지정                          |
| [yapf](https://github.com/yapf)       | 코드의 일부분만 포매팅 (사용자 정의 가능)                    |

## 5. Makefile 사용하기

**Makefile** 은 **Linux 환경에서 빌드를 자동화** 하는 대표적인 방법 중 하나이다.

* 빌드 외에도 코딩 컨벤션 체크 등에 사용할 수도 있다.

Makefile 사용의 장점은 다음과 같다.

* 반복적인 작업 표준화 가능 (예를 들어 코드 포맷 시, 항상 ```make format``` 명령어만 입력하면 됨)
* 여러 작업을 한번에 실행 가능
