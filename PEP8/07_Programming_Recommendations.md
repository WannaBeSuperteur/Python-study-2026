
## Programming Recommendations

* 다른 Python implementation (PyPy, Cython 등) 에 해를 주는 방법으로 코딩하지 말 것.
  * 예를 들어, ```a += b```, ```a = a + b``` 형태의 in-place string concatenation 에 의존하지 말 것.
    * 이 방법은 CPython 방식으로, PyPy 등에는 구현되어 있지 않음
    * 이 경우, 시간 복잡도가 $O(n^2)$ 수준으로 **코드 실행이 급격히 느려지는 원인** 이 될 수 있음
* ```is```, ```is not``` 관련
  * ```None``` 값과의 비교는 항상 ```is``` 또는 ```is not``` 을 사용할 것
  * ```if foo is not None``` 이 올바른 방식이고, **```if not foo is None``` 은 잘못된 방식임**
* lambda expression을 변수에 할당할 때, assignment statement 대신 def statement (함수) 를 사용할 것

```python
# Okay

def f(x): return x*x
```

```python
# Not Good

f = lambda x: x*x
```

* 모든 return statement가 값을 반환하거나, 어떤 return statement도 값을 반환하지 않도록 해야 한다.
* prefix, suffix 검사를 위해 **string에 slicing 적용을 하기보다는 ```startswith()```, ```endswith()``` 를 사용** 한다.
* object type 검사는 ```isinstance(obj, int)``` 와 같은 방식으로 하고, ```type(obj) is int``` 와 같은 방식은 사용하지 않는다.

## if 문 처리 관련

* **empty sequence 는 False로 처리** 된다는 사실을 기억한다. 즉 다음과 같다.

```python
# Okay

if sentence:
if not sentence:
```

```python
# Not Good

if len(sentence):
if not len(sentence):
if len(sentence) == 0:
if not len(sentence) == 0:
if sentence == '':
if not sentence == '':
```

* boolean value 를 True 또는 False 와 비교할 때, ```== True```, ```is True```, ```== False```, ```is False``` 를 사용하지 않는다.
  * 즉, ```if boolean_value == True:``` 대신 ```if boolean_value:``` 와 같이 한다. 

## 예외 및 오류 처리

* 예외 처리 시, ```BaseException``` 보다는 ```Exception``` 을 사용(상속) 할 것
* 예외 처리 시, 단순히 ```except:``` 보다는 **특정한 exception의 유형을 명시** 할 것
  * 단순 ```except``` 는 SystemExit, KeyboardInterrupt 까지 포함하므로, Control-C 를 이용한 인터럽트 시 혼동을 줄 수 있음

```python
# Okay (특정한 exception 유형 명시)

try:
    import oh_lora
except ImportError:
    print('import error')
```

```python
# Not Good (단순 except)

try:
    import oh_lora
except:
    print('import error')
```

* 모든 try-except clause에 대해서는, **try 는 최소한의 코드에 대해서만 사용** 할 것

```python
# Okay (try-except 에서 try를 최소한의 코드에서만 사용)

def test_function(key):
    ...
    try:
        value = collection[key]
    except KeyError:
        return key_not_found(key)
    else:
        return handle_value(value)
```

```python
# Not Good (try-except 에서 try의 범위가 너무 넓음)

def test_function(key):
    ...
    try:
        return handle_value(collection[key])
    except KeyError:
        return key_not_found(key)
```
