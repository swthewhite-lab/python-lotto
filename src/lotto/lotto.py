from typing import List
import random

class Lotto:
    def __init__(self, numbers: List[int]):
        self._validate(numbers)
        self._numbers = sorted(numbers)

    def _validate(self, numbers: List[int]):
        if len(numbers) != 6:
            raise ValueError("로또 번호는 6개여야 합니다.")
        if len(set(numbers)) < 6:
            raise ValueError("로또 번호는 중복되어서는 안됩니다.")
        if max(numbers) > 46 or min(numbers) < 1:
            raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")


    @classmethod
    def generate_num(cls):
        return cls(random.sample(range(1,46),6))
    

    def get_numbers(self):
        return self._numbers
    
    def __str__(self):
        return str(self._numbers)