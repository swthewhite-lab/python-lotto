from typing import List

class Lotto:
    def __init__(self, numbers: List[int]):
        self._validate(numbers)
        self._numbers = numbers

    def _validate(self, numbers: List[int]):
        if len(numbers) != 6:
            raise ValueError

    # TODO: 추가 기능 구현
