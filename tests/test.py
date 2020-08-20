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
