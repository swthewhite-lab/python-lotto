import random
from lotto import Lotto

def main():
    count = check_valid()
    lotto_list = [Lotto.generate_num() for _ in range(count)]
    print_lotto(lotto_list)

    user_num = user_input()
    bonus_num = bonus_input(user_num)

def check_valid():
    while True:
        print("구입금액을 입력해 주세요.")
        price = int(input())
        try:
            if price % 1000 == 0 :
                return price // 1000
            raise ValueError
        except ValueError:
            print("[ERROR] 구입 금액은 1,000원으로 나누어 떨어져야 합니다.")


def print_lotto(lotto_list):
    print(f"\n{len(lotto_list)}개를 구매했습니다.")
    for lotto in lotto_list:
        print(lotto)


def user_input():
    while True:
        print("\n당첨 번호를 입력해 주세요.")
        try:
            user_num = list(map(int, input().split(',')))
            return Lotto(user_num).get_numbers()
        except ValueError as e:
            print(f"[ERROR] {e}")


def bonus_input(user_num):
    while True:
        try: 
            bonus_num = input("\n보너스 번호를 입력해 주세요.\n")
            return validate_bonus(bonus_num, user_num)
        except ValueError as e:
            print(f"[ERROR] {e}") 


def validate_bonus(bonus_num, user_num):
    if not bonus_num.isdigit:
            raise ValueError("숫자를 입력해 주세요.")
    if int(bonus_num) in user_num:
        raise ValueError("보너스 숫자와 입력한 당첨 번호는 중복되지 않아야 합니다.")
    if int(bonus_num) > 46 or int(bonus_num) < 1:
        raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")

    return bonus_num

if __name__ == "__main__":
    main()
