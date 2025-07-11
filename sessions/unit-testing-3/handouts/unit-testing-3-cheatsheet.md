# Unit Testing 3 cheatsheet

## Patching

`@patch("path.to.module.method")` creates a Mock object which needs to be passed in as function parameter

```python
from unittest.mock import patch

def hello_world(msg): # No DI
    print(msg) # Dependency

@patch("builtins.print")
def test_prints_hello_world(mock_print):
    my_msg = "Hello World!" # Assemble
    hello_world(my_msg) # Act
    mock_print.assert_called_with("Hello World!") # Passes
```

### Unit Testing Terms and Definitions

- `Mock`: A piece of _fake_ code standing in to replace some _real_ code.
- `Stub`: Dummy data serving to replace real data, usually returned from an external source.
