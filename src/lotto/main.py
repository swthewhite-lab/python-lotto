import random
from lotto import Lotto, Rank


def main():
    """
    로또 프로그램 메인 함수

    1. 사용자에게 금액 입력받고 해당 개수만큼 로또 번호 생성
    2. 사용자에게서 당첨 번호와 보너스 번호 입력 받음
    3. 로또 번호와 사용자가 선택한 번호 비교하여 결과 출력
    """
    count = input_price()
    lotto_list = [Lotto.generate_num() for _ in range(count)]
    print_lotto(lotto_list)

    user_num = user_input()
    bonus_num = bonus_input(user_num)

    result, total_prize = compare_lotto(lotto_list, user_num, bonus_num)
    print_result(result, total_prize, count)


def input_price():
    """
    사용자에게서 로또 구입 금액 입력받아 유효성 검사하는 함수
    """
    while True:
        try:
            print("구입금액을 입력해 주세요.")
            price = input()
            return validate_price(price)
        except ValueError as e:
            print(f"[ERROR] {e}")
            raise


def validate_price(price):
    """
    입력된 금액 유효성 검증 후 로또 개수 반환
    """
    if not price.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해 주세요.\n")
    if int(price) % 1000 != 0:
        raise ValueError("구입 금액은 1,000원으로 나누어 떨어져야 합니다.\n")
    if int(price) < 1000:
        raise ValueError("구입 금액은 1,000원 이상이어야 합니다.\n")

    return int(price) // 1000


def print_lotto(lotto_list):
    """
    생성된 로또 번호 출력
    """
    print(f"\n{len(lotto_list)}개를 구매했습니다.")
    for lotto in lotto_list:
        print(lotto)


def user_input():
    """
    사용자로부터 당첨 번호 입력받아 반환
    """
    while True:
        print("\n당첨 번호를 입력해 주세요.")
        try:
            user_num = list(map(int, input().split(",")))
            return Lotto(user_num).get_numbers()
        except ValueError as e:
            print(f"[ERROR] {e}")


def bonus_input(user_num):
    """
    사용자로부터 보너스 번호 입력받아 반환
    """
    while True:
        try:
            bonus_num = input("\n보너스 번호를 입력해 주세요.\n")
            return validate_bonus(bonus_num, user_num)
        except ValueError as e:
            print(f"[ERROR] {e}")


def validate_bonus(bonus_num, user_num):
    """
    입력된 보너스 번호 유효성 검사 후 반환
    """
    if not bonus_num.isdigit():
        raise ValueError("숫자를 입력해 주세요.")
    if int(bonus_num) in user_num:
        raise ValueError("보너스 숫자와 입력한 당첨 번호는 중복되지 않아야 합니다.")
    if int(bonus_num) > 46 or int(bonus_num) < 1:
        raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")

    return int(bonus_num)


def compare_lotto(lotto_list, user_num, bonus_num):
    """
    로또 번호와 사용자가 선택한 번호 비교하여 당첨 결과 계산
    """
    result = {rank: 0 for rank in Rank}
    total_prize = 0

    for lotto in lotto_list:
        lotto_num = lotto.get_numbers()
        match_cnt = len(set(user_num) & set(lotto_num))
        bonus = bonus_num in lotto_num

        rank = Rank.get_rank(match_cnt, bonus)
        result[rank] += 1
        total_prize += rank.prize

    return result, total_prize


def print_result(result, total_prize, count):
    """ "
    당첨 결과 출력
    """
    profit_rate = round((total_prize / (count * 1000)) * 100, 2)

    print("\n당첨 통계")
    print("---")
    for rank in Rank:
        if rank == Rank.SECOND:
            print(
                f"{rank.match_cnt}개 일치, 보너스 볼 일치 ({rank.prize:,}원) - {result[rank]}개"
            )

        if rank != Rank.NONE and rank != Rank.SECOND:
            print(f"{rank.match_cnt}개 일치 ({rank.prize:,}원) - {result[rank]}개")

    print(f"총 수익률은 {profit_rate}%입니다.")


if __name__ == "__main__":
    main()
