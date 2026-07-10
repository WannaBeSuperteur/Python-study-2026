
## Imports

* 각 라이브러리의 import 는 **서로 다른 line 에 있어야** 한다.
* 단, ```from xxx import ...``` 의 경우에는 한 line에 여러 개를 import 할 수 있다.
* Import 의 순서는 다음과 같다.
  * 표준 파이썬 라이브러리 (```os```, ```math``` 등)
  * Third Party 라이브러리 (```NumPy```, ```Pandas``` 등)
  * 해당 코드에서 사용하는 local 부분

## Dunders

* Dunders (```__all__``` 등) 는 **Docstring 과 import (단, ```__future__``` 제외) 사이** 에 있어야 한다.

```python
# OK

"""Example Docstring

Blah blah ...
"""

from __future__ import absolute_import

__all__ = ['oh-lora', 'wannabe', 'superteur', 'artist', 'company']
__version__ = '2026.3.23'
__author__ = 'Hong-sik Kim'

import os
import math
...
```