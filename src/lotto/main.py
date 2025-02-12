import random


def main():
    count = check_valid()
    lotto_list = make_lotto(count)
    print_lotto(count, lotto_list)

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


def make_lotto(count):
    lotto_list = [sorted(random.sample(range(1,46),6)) for _ in range(count)]
    return lotto_list


def print_lotto(count, lotto_list):
    print(f"\n{count}개를 구매했습니다.")
    for lotto in lotto_list:
        print(lotto)


def user_input():
    while True:
        print("\n당첨 번호를 입력해 주세요.")
        user_num = list(map(int, input().split(',')))
        try:
            if len(set(user_num)) < 6:
                raise ValueError("숫자는 중복되지 않아야 합니다.")
            if len(user_num) > 6:
                raise ValueError("숫자 6개를 입력해주세요.")
            if max(user_num) > 46 or min(user_num) < 1:
                raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")
            return user_num
        except ValueError as e:
            print(f"[ERROR] {e}")


def bonus_input(user_num):
    while True:
        print("\n보너스 번호를 입력해 주세요.")
        bonus_num = input()
        try: 
            if not bonus_num.isdigit:
                raise ValueError("숫자를 입력해 주세요.")
            if int(bonus_num) in user_num:
                raise ValueError("보너스 숫자와 입력한 당첨 번호는 중복되지 않아야 합니다.")
            if int(bonus_num) > 46 or int(bonus_num) < 1:
                raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")
            return int(bonus_num)
        except ValueError as e:
            print(f"[ERROR] {e}") 


if __name__ == "__main__":
    main()
