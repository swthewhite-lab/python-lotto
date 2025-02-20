from enum import Enum
import random


LOTTO_SIZE = 6  # 로또 길이 매직넘버상수
LOTTO_NUMBER_RANGE = range(1, 46)  # 로또 숫자 범위 매직넘버상수


class Lotto:
    def __init__(self, numbers: list[int] = None):
        if numbers is None:  # numbers가 주어지지 않으면 자동으로 생성
            numbers = self.issuance_lotto()
        self._validate(numbers)
        self._numbers = numbers
        self.bonus_number = int
        self.numbers_list = list[list]
        self.result_list = list[int]
        self.statistics_list = list[list]

    def _validate(self, numbers: list[int]):
        if len(numbers) != LOTTO_SIZE:
            raise ValueError("[ERROR] 당첨 번호는 6자리입니다.")
        elif not all(num in LOTTO_NUMBER_RANGE for num in numbers):
            raise ValueError("[ERROR] 당첨 번호는 1 ~ 45 사이여야 합니다.")
        elif not all(numbers.count(num) == 1 for num in numbers):
            raise ValueError("[ERROR] 당첨 번호는 중복될 수 없습니다.")

    def validate_bonus_number(self, number: int):
        self.bonus_number = number
        if self.bonus_number in self._numbers:
            raise ValueError("[ERROR] 보너스 번호는 당첨 번호와 중복될 수 없습니다.")
        elif self.bonus_number not in LOTTO_NUMBER_RANGE:
            raise ValueError("[ERROR] 보너스 번호는 1 ~ 45 사이여야 합니다.")

    @staticmethod
    def issuance_lotto():
        """랜덤한 6자리 로또 번호 생성 후 정렬하여 반환"""
        value = sorted(random.sample(LOTTO_NUMBER_RANGE, LOTTO_SIZE))
        return value

    def __str__(self):
        """str 형식으로 변환하여 반환"""
        return str(self._numbers)

    def get_numbers(self):
        """로또 번호 리스트 반환"""
        return self._numbers

    def compare_winning_number(self, numbers: list[int]):
        """당첨 번호와 발행 번호를 비교"""
        count = 0
        for i in numbers:
            if i in self._numbers:
                count += 1
        return count

    def compare_bonus_number(self, numbers: list[int]):
        """보너스 번호와 발행 번호를 비교"""
        if self.bonus_number in numbers:
            return 1
        return 0

    def calculate_result(self, numbers_list: list[list]):
        """발행한 로또를 순서대로 당첨 번호, 보너스 번호와 비교"""
        self.numbers_list = numbers_list
        self.result_list = [0 for _ in range(len(numbers_list))]
        for i in range(len(self.result_list)):
            count_winning = self.compare_winning_number(self.numbers_list[i])
            count_bonus = self.compare_bonus_number(self.numbers_list[i])
            self.result_list[i] = [count_winning, count_bonus]
        return self.result_list


class Score(Enum):
    FIRST = (6, 0, 2000000000)  # 6개 일치, 보너스 X, 1등
    SECOND = (5, 1, 30000000)    # 5개 일치, 보너스 O, 2등
    THIRD = (5, 0, 1500000)      # 5개 일치, 보너스 X, 3등
    FOURTH = (4, 0, 50000)        # 4개 일치, 보너스 X, 4등
    FIFTH = (3, 0, 5000)          # 3개 일치, 보너스 X, 5등
    NONE = (0, 0, 0)               # 당첨되지 않음

    def __init__(self, m_count, b_match, prize):
        self.m_count = m_count  # 맞춘 숫자 개수
        self.b_match = b_match  # 보너스 번호 일치 여부
        self.prize = prize  # 상금

    @classmethod
    def get_score(cls, m_count, b_match):
        """
        당첨 번호 개수와 보너스 번호 여부를 받아 해당하는 Score 반환
        """
        for score in cls:
            if score.m_count == m_count and score.b_match == b_match:
                return score
        return cls.NONE  # 당첨되지 않은 경우
