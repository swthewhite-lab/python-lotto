from enum import Enum
import random


class Lotto:
    """
    로또 번호 생성 및 유효성 검증하는 클래스
    """

    def __init__(self, numbers: list[int]):
        """
        로또 객체 초기화
        """
        self._validate(numbers)
        self._numbers = sorted(numbers)

    def _validate(self, numbers: list[int]):
        """
        로또 번호 유효성 검사
        (로또 번호 6개, 중복 불가, 1~45의 범위)
        """
        if len(numbers) != 6:
            raise ValueError("로또 번호는 6개여야 합니다.")
        if len(set(numbers)) < 6:
            raise ValueError("로또 번호는 중복되어서는 안됩니다.")
        if max(numbers) > 46 or min(numbers) < 1:
            raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")

    @classmethod
    def generate_num(cls):
        """
        1~45 사이의 랜덤한 6개의 숫자로 로또 객체 생성
        """
        return cls(random.sample(range(1, 46), 6))

    def get_numbers(self):
        """
        로또 번호 리스트 반환
        """
        return self._numbers

    def __str__(self):
        """
        로또 번호 문자열로 반환
        """
        return str(self._numbers)


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
