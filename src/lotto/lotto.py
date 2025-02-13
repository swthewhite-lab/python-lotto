"""lotto.py: 로또 번호 생성 및 당첨 결과를 처리하는 모듈"""

import random
from enum import Enum


class Prize(Enum):
    """당첨 등수를 Enum으로 정의"""
    THREE_MATCH = 3
    FOUR_MATCH = 4
    FIVE_MATCH = 5
    FIVE_MATCH_BONUS = "5_bonus"
    SIX_MATCH = 6


class Lotto:
    """로또 번호 및 당첨 결과를 처리하는 클래스"""

    def __init__(self, numbers: list[int]):
        self._validate(numbers)
        self._numbers = numbers

    @property
    def numbers(self):
        """로또 번호를 반환하는 getter 메서드"""
        return self._numbers

    def _validate(self, numbers: list[int]):
        """로또 번호 검증: 개수, 중복, 범위"""
        if len(numbers) != 6:
            raise ValueError("로또 번호는 정확히 6개여야 합니다.")
        if len(set(numbers)) != 6:
            raise ValueError("로또 번호에 중복이 있어서는 안 됩니다.")
        if not all(1 <= num <= 45 for num in numbers):
            raise ValueError("로또 번호는 1부터 45 사이여야 합니다.")

    @staticmethod
    def get_lotto_count():
        """로또 구입 금액 입력 및 예외 처리"""
        try:
            amount = input("로또 구입 금액을 입력하세요: ")
            Lotto._validate_amount(amount)

            amount = int(amount)
            lotto_count = amount // 1000
            print(f"{lotto_count}개의 로또를 구입합니다.")
            return lotto_count

        except ValueError as e:
            print(e)
            raise

    @staticmethod
    def _validate_amount(amount):
        """로또 금액 검증"""
        if not amount.isdigit():
            raise ValueError("[ERROR] 숫자를 입력하세요.")

        amount = int(amount)
        if amount < 1000 or amount % 1000 != 0:
            raise ValueError("[ERROR] 최소 1,000원 이상, 1,000원 단위로 입력해야 합니다.")

    @staticmethod
    def generate_random_lotto():
        """무작위 로또 번호 생성"""
        return Lotto(sorted(random.sample(range(1, 46), 6)))

    @staticmethod
    def generate_lottos(count: int):
        """구입한 로또 개수만큼 번호 생성"""
        return [Lotto.generate_random_lotto() for _ in range(count)]

    @staticmethod
    def get_winning_numbers():
        """당첨 번호 및 보너스 번호 입력"""
        numbers = Lotto._get_valid_numbers("당첨 번호를 입력해 주세요: ", 6)
        bonus = Lotto._get_valid_bonus("보너스 번호 1개를 입력하세요: ", numbers)
        return numbers, bonus

    @staticmethod
    def _get_valid_numbers(prompt, count):
        """유효한 번호 입력 받기"""
        while True:
            try:
                numbers = list(
                    map(int, input(prompt).replace(',', ' ').split())
                )
                Lotto._validate_numbers(numbers, count)
                return numbers
            except ValueError as e:
                print(e)

    @staticmethod
    def _validate_numbers(numbers, count):
        """입력된 숫자 검증"""
        if len(numbers) != count or len(set(numbers)) != count:
            raise ValueError(f"[ERROR] {count}개의 숫자를 입력해야 하며, 중복이 없어야 합니다.")
        if not all(1 <= num <= 45 for num in numbers):
            raise ValueError("[ERROR] 숫자는 1부터 45 사이여야 합니다.")

    @staticmethod
    def _get_valid_bonus(prompt, numbers):
        """보너스 번호 입력 받기"""
        while True:
            bonus = Lotto._safe_input_bonus(prompt)
            if Lotto._is_valid_bonus(bonus, numbers):
                return bonus
            print("[ERROR] 올바른 보너스 번호를 입력하세요.")

    @staticmethod
    def _safe_input_bonus(prompt):
        """보너스 번호 안전 입력"""
        try:
            return int(input(prompt))
        except ValueError:
            return -1  # 잘못된 값 반환 (검증에서 걸러짐)

    @staticmethod
    def _is_valid_bonus(bonus, numbers):
        """보너스 번호 검증"""
        if bonus in numbers or not 1 <= bonus <= 45:
            return False
        return True

    @staticmethod
    def check_results(purchased_lottos, winning_numbers, bonus_number):
        """구입한 로또 번호와 당첨 번호 비교"""
        results = {
            Prize.THREE_MATCH: 0,
            Prize.FOUR_MATCH: 0,
            Prize.FIVE_MATCH: 0,
            Prize.FIVE_MATCH_BONUS: 0,
            Prize.SIX_MATCH: 0,
        }

        for lotto in purchased_lottos:
            matched_count, has_bonus = Lotto._count_matches(
                lotto.numbers, winning_numbers, bonus_number
            )

            Lotto._update_results(results, matched_count, has_bonus)

        return results

    @staticmethod
    def _update_results(results, matched_count, has_bonus):
        """당첨 결과 딕셔너리를 업데이트"""
        key = Lotto._determine_prize_key(matched_count, has_bonus)
        if key:
            results[key] += 1

    @staticmethod
    def _count_matches(lotto_numbers, winning_numbers, bonus_number):
        """로또 번호와 당첨 번호 비교하여 일치 개수와 보너스 여부 반환"""
        matched_count = len(set(lotto_numbers) & set(winning_numbers))
        has_bonus = bonus_number in lotto_numbers
        return matched_count, has_bonus

    @staticmethod
    def _determine_prize_key(matched_count, has_bonus):
        """당첨 등수 판별"""
        if matched_count == 5 and has_bonus:
            return Prize.FIVE_MATCH_BONUS
        if matched_count == 6:
            return Prize.SIX_MATCH
        if matched_count == 5:
            return Prize.FIVE_MATCH
        if matched_count == 4:
            return Prize.FOUR_MATCH
        if matched_count == 3:
            return Prize.THREE_MATCH
        return None

    @staticmethod
    def print_results(results, total_cost):
        """당첨 통계를 출력하고 수익률을 계산하여 표시"""
        print("\n당첨 통계")
        print("---")
        Lotto.print_winning_statistics(results)

        total_prize = Lotto.calculate_total_prize(results)
        profit_ratio = Lotto.calculate_profit_ratio(total_prize, total_cost)

        print(f"총 수익률은 {profit_ratio:.1f}%입니다.")

    @staticmethod
    def print_winning_statistics(results):
        """당첨 개수를 출력"""
        print(
            f"3개 일치 (5,000원) - {results[Prize.THREE_MATCH]}개\n"
            f"4개 일치 (50,000원) - {results[Prize.FOUR_MATCH]}개\n"
            f"5개 일치 (1,500,000원) - {results[Prize.FIVE_MATCH]}개\n"
            "5개 일치, 보너스 볼 일치 (30,000,000원) - "
            f"{results[Prize.FIVE_MATCH_BONUS]}개\n"
            f"6개 일치 (2,000,000,000원) - {results[Prize.SIX_MATCH]}개"
        )

    @staticmethod
    def calculate_total_prize(results):
        """총 당첨 금액 계산"""
        return (
            results[Prize.THREE_MATCH] * 5000
            + results[Prize.FOUR_MATCH] * 50000
            + results[Prize.FIVE_MATCH] * 1500000
            + results[Prize.FIVE_MATCH_BONUS] * 30000000
            + results[Prize.SIX_MATCH] * 2000000000
        )

    @staticmethod
    def calculate_profit_ratio(total_prize, total_cost):
        """수익률 계산"""
        if total_cost > 0:
            return (total_prize / total_cost) * 100
        return 0
