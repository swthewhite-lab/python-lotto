import random
from enum import Enum


class Rank(Enum):
    """
    로또 당첨 순위 정의하는 클래스
    """
    FIFTH = (3, False, 5_000)
    FOURTH = (4, False, 50_000)
    THIRD = (5, False, 1_500_000)
    SECOND = (5, True, 30_000_000)
    FIRST = (6, False, 2_000_000_000)
    NONE = (0, False, 0)

    def __init__(self, match_cnt, bonus_match, prize):
        """
        Rank 객체 초기화
        """
        self.match_cnt = match_cnt
        self.bonus_match = bonus_match
        self.prize = prize

    @classmethod
    def get_rank(cls, match_cnt, bonus):
        """
        일치 개수와 보너스 번호 여부를 기반으로 당첨 순위 반환
        """
        for rank in cls:
            if rank.match_cnt == match_cnt and rank.bonus_match == bonus:
                return rank
        return cls.NONE


class Lotto():
    """로또 번호 및 당첨 결과를 처리하는 클래스"""
    ERROR_MESSAGE = "[ERROR] 구입 금액이 잘못되었습니다."
    def __init__(self, numbers: list[int]):
        self._validate(numbers)
        self._numbers = sorted(numbers)

    def _validate(self, numbers: list[int]):
        """로또 번호 검증: 개수, 중복, 범위"""
        if len(numbers) != 6:
            raise ValueError("로또 번호는 정확히 6개여야 합니다.")
        if len(set(numbers)) != 6:
            raise ValueError("로또 번호에 중복이 있어서는 안 됩니다.")
        if not all(1 <= num <= 45 for num in numbers):
            raise ValueError("로또 번호는 1부터 45 사이여야 합니다.")

    @classmethod
    def generate_randomlotto(cls):
        """무작위 로또 번호 생성"""
        return cls(random.sample(range(1, 46), 6))


    def get_numbers(self):
        return self._numbers


    def __str__(self):
        """str 형식으로 변환하여 반환"""
        return str(self._numbers)
