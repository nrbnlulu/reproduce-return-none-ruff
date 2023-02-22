import random
from typing import Optional


def return_implicit_none() -> Optional[int]:
    if random.randint(1, 2) == 2:
        return 2
