## Code Layout

* 함수 안에 여러 개의 인수를 넣을 때는, **opening delimiter 와 정렬할 것** (각 line의 인수 개수는 무관)
* 함수의 argument 부분을 구분하기 위해, **argument 부분에는 추가로 4칸 공백을 넣을 것**
* 수식이 길어질 때, **연산자는 줄의 첫 부분에 넣을 것**
* Tab 보다는 **Space 를 사용할 것**

```python
# OK

def generate_image_using_mid_vector(finetune_v9_generator,
                                    mid_vector,
                                    layer_name,
                                    trunc_psi=1.0,
                                    trunc_layers=0,
                                    randomize_noise=False,
                                    lod=None):
```

```python
# NOT Good

def get_result():
    test_score = performance_score +
                 competency_score +
                 (2.5 * attitude_score)
```

## Maximum Line Length

* 79 글자
* 단, docstring, comment 등의 경우 72 글자로 제한



