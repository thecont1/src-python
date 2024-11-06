from typing import List

def add_ints(a: int, b: int) -> int:
    return a + b

def add_floats(a: float, b: float) -> float:
    return a + b

def add_strings(a: str, b: str) -> str:
    return a + b

print(add_ints(90, 10))
print(add_floats(87.3, 12.7))
print(add_strings('hall', 'mark'))

# run this on the command prompt:
# ❯ mypy static_typing.py