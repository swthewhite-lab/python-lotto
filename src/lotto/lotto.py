from typing import List
from enum import Enum
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
        return cls(random.sample(range(1, 46), 6))

    def get_numbers(self):
        return self._numbers

    def __str__(self):
        return str(self._numbers)


class Rank(Enum):
    FIFTH = (3, False, 5_000)
    FOURTH = (4, False, 50_000)
    THIRD = (5, False, 1_500_000)
    SECOND = (5, True, 30_000_000)
    FIRST = (6, False, 2_000_000_000)
    NONE = (0, False, 0)

    def __init__(self, match_cnt, bonus_match, prize):
        self.match_cnt = match_cnt
        self.bonus_match = bonus_match
        self.prize = prize

    @classmethod
    def get_rank(cls, match_cnt, bonus):
        for rank in cls:
            if rank.match_cnt == match_cnt and rank.bonus_match == bonus:
                return rank
        return cls.NONE
