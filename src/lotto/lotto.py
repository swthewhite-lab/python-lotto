import random
from enum import Enum


class Rank(Enum):
    """
    로또 당첨 순위를 정의하는 클래스.

    - FIFTH: 3개 일치 (5,000원)
    - FOURTH: 4개 일치 (50,000원)
    - THIRD: 5개 일치 (1,500,000원)
    - SECOND: 5개 + 보너스 번호 일치 (30,000,000원)
    - FIRST: 6개 일치 (2,000,000,000원)
    - NONE: 0개 일치 (당첨 없음)
    """
    FIFTH = (3, False, 5_000)
    FOURTH = (4, False, 50_000)
    THIRD = (5, False, 1_500_000)
    SECOND = (5, True, 30_000_000)
    FIRST = (6, False, 2_000_000_000)
    NONE = (0, False, 0)

    def __init__(self, match_cnt, bonus_match, prize):
        """
        Rank 객체 초기화.

        Args:
            match_cnt (int): 일치하는 번호 개수
            bonus_match (bool): 보너스 번호 일치 여부
            prize (int): 당첨 금액
        """
        self.match_cnt = match_cnt
        self.bonus_match = bonus_match
        self.prize = prize

    @classmethod
    def get_rank(cls, match_cnt, bonus):
        """
        일치 개수와 보너스 번호 여부를 기반으로 당첨 순위 반환.

        Args:
            match_cnt (int): 일치하는 번호 개수
            bonus (bool): 보너스 번호 일치 여부

        Returns:
            Rank: 해당하는 당첨 순위
        """
        for rank in cls:
            if rank.match_cnt == match_cnt and rank.bonus_match == bonus:
                return rank
        return cls.NONE


class Lotto:
    """
    로또 번호 및 당첨 결과를 처리하는 클래스.

    - 1~45 사이의 서로 다른 6개의 숫자를 가짐.
    - 로또 번호 검증 및 생성 기능 포함.
    """
    ERROR_MESSAGE = "[ERROR] 구입 금액이 잘못되었습니다."

    def __init__(self, numbers: list[int]):
        """
        Lotto 객체 초기화.

        Args:
            numbers (list[int]): 1~45 사이의 6개 정수 리스트
        """
        self._validate(numbers)
        self._numbers = sorted(numbers)

    def _validate(self, numbers: list[int]):
        """
        로또 번호 검증: 개수, 중복, 범위 확인.

        Args:
            numbers (list[int]): 1~45 사이의 6개 정수 리스트

        Raises:
            ValueError: 유효하지 않은 로또 번호일 경우 예외 발생
        """
        if len(numbers) != 6:
            raise ValueError("로또 번호는 정확히 6개여야 합니다.")
        if len(set(numbers)) != 6:
            raise ValueError("로또 번호에 중복이 있어서는 안 됩니다.")
        if not all(1 <= num <= 45 for num in numbers):
            raise ValueError("로또 번호는 1부터 45 사이여야 합니다.")

    @classmethod
    def generate_randomlotto(cls):
        """
        무작위 로또 번호 생성.

        Returns:
            Lotto: 생성된 로또 객체
        """
        return cls(random.sample(range(1, 46), 6))

    def get_numbers(self):
        """
        로또 번호 반환.

        Returns:
            list[int]: 정렬된 로또 번호 리스트
        """
        return self._numbers

    def __str__(self):
        """
        문자열 변환.

        Returns:
            str: 로또 번호 리스트를 문자열로 반환
        """
        return str(self._numbers)
