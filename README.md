# Basic Operations Python Package

jdla_basic is a python module that provides access to basic operation functions.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install jdla_basic.

```bash
pip install jdla_basic
```

## Usage

```python
from jdla_basic import basic_operations

a = 1
b = 2

addition = basic_operations.addition(a, b)
subtraction = basic_operations.substraction(b, a)
multiplication = basic_operations.multiplication(b, a)
division = basic_operations.division(b, a)
modulus = basic_operations.modulus(b, a)

print(f"{a} + {b} = {addition}")
print(f"{b} - {a} = {subtraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{b} / {a} = {division}")
print(f"{b} % {a} = {modulus}")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.