
## White Spaces

* 소괄호, 중괄호, 대괄호와 인접한 부분에는 **공백이 적절하지 않음**
* trailing comma (마지막 항목 이후의 comma) 와 그 다음에 오는 ```)``` 사이에는 **공백이 적절하지 않음**
* ```,```, ```:```, ```;``` 의 직전에는 **공백이 적절하지 않음**
* argument list 직전의 ```(```, indexing/slicing을 위한 ```[``` 직전의 공백은 **적절하지 않음**

### Slice가 Binary Operator처럼 사용되는 경우

* binary operator (이진 연산자): **2개의 피연산자를 연산하는 것 (이항 연산)**
* 이때는, **Slice 좌우에 서로 동일한 양의 공백** 이 있어야 함
  * 단, Extended Slice (```:```를 2개 사용하는 형태) 인 경우, **양쪽의 ```:```에 대해 같은 양의 공백** 이 있어야 함

```python
# Okay

test[a:b], test[a:b:c], test[a::b]
test[a+b : c+d]
```

```python
# Not Good

test[a + b:c + d]
```

## 기타

* trailing whitespace (개행 직전에 들어간 공백) 은 **혼동을 줄 수 있으므로 피할 것**
* 다음 연산자 앞뒤에는 **1칸의 공백** 이 적절함
  * 이진 연산자 (```+```, ```-``` 등)
  * assignment (```=```), augmented assignment (```+=```, ```-=```)
  * 비교 연산자 (```==```, ```<```, ```>```, ```!=```, ```<=```, ```>=``` 등)
  * 논리 연산자 (```and```, ```or```, ```not```)

## 함수 관련

* Function annotation (argument type) 의 경우 ```:``` 및 ```->``` 에 대해 공백 필요

```python
# Okay

def test(aaa: int): ...
def test() -> int: ...
```

```python
# Not Good

def test(aaa:int): ...
def test()->int: ...
```

* Keyword argument (```argument_name=value``` 형태) 의 경우 ```=``` 전후 공백을 넣는 것은 적절하지 않음
* Unannotated function parameter (자료형이 명시되지 않은) 에 기본값을 할당 시, 마찬가지로 ```=``` 전후 공백을 넣는 것은 적절하지 않음
* 단, **argument에 대한 annotation이 있을 때는 ```=``` 의 좌우에 공백 필요**

```python
# Okay

def test1(performance=50.0, competency=50.0, attitude=50.0):
    return compute_score(p=performance, c=competency, a=attitude)

def test2(performance: float = 50.0, competency: float = 50.0, attitude: float = 50.0):
    return compute_score(p=performance, c=competency, a=attitude)
```

```python
# Not Good

def test1(performance = 50.0, competency = 50.0, attitude = 50.0):
    return compute_score(p = performance, c = competency, a = attitude)

def test2(performance: float=50.0, competency: float=50.0, attitude: float=50.0):
    return compute_score(p = performance, c = competency, a = attitude)
```

