import random


def main():
    count = check_valid()
    lotto_list = make_lotto(count)
    print_list(count, lotto_list)

    user_num = num_list()


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


def print_list(count, lotto_list):
    print()
    print(f"{count}개를 구매했습니다.")
    for lotto in lotto_list:
        print(lotto)

def num_list():
    pass

if __name__ == "__main__":
    main()
