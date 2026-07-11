
## Comments

* 코드와 반대되는 설명을 하는 코멘트는 **없느니만 못하다.**
* 코멘트는 **코드 수정과 함께, 우선순위를 높여서 코드 수정 내용을 항상 반영** 하도록 **업데이트** 해야 한다.
* 코멘트는 **완전한 문장 형태** 여야 한다.

## Block Comments and Inline Comments

| 구분              | 설명                                    |
|-----------------|---------------------------------------|
| Block Comments  | 코드의 특정 단위 (함수, 코드 파일 전체 등) 를 나타내는 코멘트 |
| Inline Comments | 실제 코드가 동작하는 부분과 **동일한 줄** 에 있는 코멘트    |

* Block Comments 작성 원칙
  * 원본 코드와 **동일한 level 의 indentation** 적용
  * block comment의 각 줄은 ```# ``` (```#``` + single space) 로 시작
* Inline Comment 작성 원칙
  * 최소 **2개 이상의 공백 (```  ```)** 을 사이에 두고 있어야 함
  * 일반적으로 불필요하며 코드를 보는 사람 입장에서 혼동을 줄 수 있음

## Documentation Strings

* Documentation String (Docstring) 는 **```"""``` 또는 ```'''``` 으로 시작하고 끝나는 형태의 string** 을 말한다.
* Docstring 의 작성 원칙은 다음과 같다.
  * **모든 public 모듈, 함수, 클래스, method** 에 작성하는 것이 좋음
  * Multi-line Docstring의 끝부분에 있는 ```"""``` 는 독립된 줄에 있어야 함
  * Single-line Docstring의 끝부분에 있는 ```"""``` 는 그 한 줄에 그대로 있어야 함 (독립된 줄이 아닌)

```python
# Not Good (only 1 space)

x = x + 1 # compensate for border
```

```python
# Not Good

x = x + 1         # increment x
```

```python
# Sometimes OK

x = x + 1          # compensate for border
```

