from typing import List
import random

class Lotto:
    """로또 번호 및 당첨 결과를 처리하는 클래스"""
    ERROR_MESSAGE = "[ERROR] 구입 금액이 잘못되었습니다."
    
    def __init__(self, numbers: List[int]):
        self._validate(numbers)
        self._numbers = numbers

    def _validate(self, numbers: List[int]):
        """로또 번호 검증: 개수, 중복, 범위"""
        if len(numbers) != 6:
            raise ValueError("로또 번호는 정확히 6개여야 합니다.")
        if len(set(numbers)) != 6:
            raise ValueError("로또 번호에 중복이 있어서는 안 됩니다.")
        if not all(1 <= num <= 45 for num in numbers):
            raise ValueError("로또 번호는 1부터 45 사이여야 합니다.")

 
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

 
    def _validate_amount(amount):
        """로또 금액 검증"""
        # 숫자만 포함된 문자열인지 확인
        if not amount.isdigit():  # 숫자가 아닌 문자가 포함되면 예외
            raise ValueError("[ERROR] 숫자를 입력하세요.")
        
        amount = int(amount)  # 숫자로 변환
        if amount < 1000 or amount % 1000 != 0:  # 금액이 1000원 이상이거나 1000원 단위로 입력되지 않으면 예외
            raise ValueError(Lotto.ERROR_MESSAGE)

 
    def generate_random_lotto():
        """무작위 로또 번호 생성"""
        return Lotto(sorted(random.sample(range(1, 46), 6)))

 
    def generate_lottos(count: int):
        """구입한 로또 개수만큼 번호 생성"""
        return [Lotto.generate_random_lotto() for _ in range(count)]

 
    def get_winning_numbers():
        """당첨 번호 및 보너스 번호 입력"""
        numbers = Lotto._get_valid_numbers("당첨 번호를 입력해 주세요: ", 6)
        bonus = Lotto._get_valid_bonus("보너스 번호 1개를 입력하세요: ", numbers)
        return numbers, bonus

 
    def _get_valid_numbers(prompt, count):
        """유효한 번호 입력 받기"""
        while True:
            try:
                numbers = list(map(int, input(prompt).replace(',', ' ').split()))  # ','를 공백으로 바꾸고, 스페이스로 구분
                Lotto._validate_numbers(numbers, count)  # 번호 검증
                return numbers
            except ValueError as e:
                print(e)

 
    def _validate_numbers(numbers, count):
        """입력된 숫자 검증"""
        if len(numbers) != count or len(set(numbers)) != count:
            raise ValueError(f"[ERROR] {count}개의 숫자를 입력해야 하며, 중복이 없어야 합니다.")
        if not all(1 <= num <= 45 for num in numbers):
            raise ValueError("[ERROR] 숫자는 1부터 45 사이여야 합니다.")

 
    def _get_valid_bonus(prompt, numbers):
        """보너스 번호 입력 받기"""
        while True:
            bonus = Lotto._safe_input_bonus(prompt)
            if Lotto._is_valid_bonus(bonus, numbers):
                return bonus
            print("[ERROR] 올바른 보너스 번호를 입력하세요.")

 
    def _safe_input_bonus(prompt):
        """보너스 번호 안전 입력"""
        try:
            return int(input(prompt))
        except ValueError:
            return -1  # 잘못된 값 반환 (검증에서 걸러짐)

 
    def _is_valid_bonus(bonus, numbers):
        """보너스 번호 검증"""
        if bonus in numbers or not (1 <= bonus <= 45):
            return False
        return True

 
    def check_results(purchased_lottos, winning_numbers, bonus_number):
        """구입한 로또 번호와 당첨 번호 비교"""
        results = {3: 0, 4: 0, 5: 0, "5_bonus": 0, 6: 0}
        for lotto in purchased_lottos:
            matched_count, has_bonus = Lotto._count_matches(
                lotto._numbers,
                winning_numbers,
                bonus_number
            )
            key = Lotto._determine_prize_key(matched_count, has_bonus)
            if key:
                results[key] += 1
        return results

 
    def _count_matches(lotto_numbers, winning_numbers, bonus_number):
        """로또 번호와 당첨 번호 비교하여 일치 개수와 보너스 여부 반환"""
        matched_count = len(set(lotto_numbers) & set(winning_numbers))
        has_bonus = bonus_number in lotto_numbers
        return matched_count, has_bonus

 
    def _determine_prize_key(matched_count, has_bonus):
        """당첨 등수 판별"""
        if matched_count == 5 and has_bonus:
            return "5_bonus"
        if matched_count in {3, 4, 5, 6}:
            return matched_count
        return None

 
    def print_results(results, total_cost):
        """당첨 통계를 출력"""
        print("\n당첨 통계")
        print("---")
        print(f"3개 일치 (5,000원) - {results[3]}개")
        print(f"4개 일치 (50,000원) - {results[4]}개")
        print(f"5개 일치 (1,500,000원) - {results[5]}개")
        print(f"5개 일치, 보너스 볼 일치 (30,000,000원) - {results['5_bonus']}개")
        print(f"6개 일치 (2,000,000,000원) - {results[6]}개")
        total_prize = (
            results[3] * 5000
            + results[4] * 50000
            + results[5] * 1500000
            + results["5_bonus"] * 30000000
            + results[6] * 2000000000
        )
        profit_ratio = (total_prize / total_cost) * 100 if total_cost else 0
        print(f"총 수익률은 {profit_ratio:.1f}%입니다.")

