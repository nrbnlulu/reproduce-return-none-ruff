# reproduce-return-none-ruff


run `pre-commit run -a`
and 
```python
def return_implicit_none() -> Optional[int]:
    if random.randint(1, 2) == 2:
        return 2
```
would become
```python
def return_implicit_none() -> Optional[int]:
    if random.randint(1, 2) == 2:
        return 2
    return None
```