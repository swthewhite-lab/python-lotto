from typing import List
import random


LOTTO_SIZE = 6  # 로또 길이 매직넘버상수
LOTTO_NUMBER_RANGE = range(1, 46)  # 로또 숫자 범위 매직넘버상수


class Lotto:
    def __init__(self, numbers: List[int] = None):
        if numbers is None:  # numbers가 주어지지 않으면 자동으로 생성성
            numbers = self.issuance_lotto()
        self._validate(numbers)
        self._numbers = numbers


    def _validate(self, numbers: List[int]):
        if len(numbers) != 6:
            raise ValueError()

    @staticmethod
    def issuance_lotto():
        """랜덤한 6자리 로또 번호 생성 후 정렬하여 반환"""
        value = sorted(random.sample(LOTTO_NUMBER_RANGE, LOTTO_SIZE))
        return value
    

    def __str__(self):
        """str 형식으로 변환하여 반환"""
        return str(self._numbers)
    

    def get_numbers(self):
        """로또 번호 리스트 반환환"""
        return self._numbers