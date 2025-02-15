from lotto.lotto import Lotto, Score


LOTTO_EACH_PRICE = 1000  # 로또 구입 금액 단위 매직넘버상수


# data가 정수인지 검증 함수
def is_number(data):
    try:
        return int(data)
    except ValueError as e:
        raise ValueError("[ERROR] 정수만 입력해주세요.") from e


# 구입 금액 입력 검증 함수
def validate_input_purchase_amount(data):
    purchase_amount = is_number(data)  # 입력 값이 정수인지 검증
    if purchase_amount <= 0:  # 입력 값이 양의 정수인지 검증
        raise ValueError("[ERROR] 구입 금액은 양의 정수 입니다.")
    elif purchase_amount % LOTTO_EACH_PRICE != 0:  # 입력 값이 1,000원 단위인지 검증
        raise ValueError("[ERROR] 구입 금액을 1,000원 단위로 입력해 주세요.")
    return purchase_amount  # 검증 통과


def input_purchase_amount():  # 구입 금액 입력 함수
    print("구입금액을 입력해 주세요.")
    purchase_amount = input()
    purchase_amount = validate_input_purchase_amount(purchase_amount)  # 구입 금액 검증
    return purchase_amount


# 구매 가능한 로또 개수 계산
def generate_lotto_quantity(purcahse_amount):
    lotto_quantity = purcahse_amount // LOTTO_EACH_PRICE
    print("\n{0}개를 구매했습니다.".format(lotto_quantity))
    return lotto_quantity


# 입력 값을 list 형식으로 변환해주는 함수
def convert_to_list(data):
    try:
        data = list(map(int, data.replace(" ","").split(",")))
        return data
    except ValueError as e:
        raise ValueError("[ERROR] 번호는 정수로 이루어져 있어야 합니다.") from e


# 당첨 번호를 입력받고 검증하는 함수
def input_winning_numbers():
    print("\n당첨 번호를 입력해 주세요.")
    winning_numbers = input()  # 당첨 번호 입력
    winning_numbers = convert_to_list(winning_numbers)  # 당첨 번호 list형으로 변경
    lotto = Lotto(winning_numbers)  # 당첨 번호 검증
    return lotto


# 보너스 번호를 입력받고 검증하는 함수
def input_bonus_number(lotto):
    print("\n보너스 번호를 입력해 주세요.")
    bouns_number = input()  # 보너스 번호 입력
    bouns_number = is_number(bouns_number)  # 보너스 번호를 int형으로 변환
    lotto.validate_bonus_number(bouns_number)  # 보너스 번호 검증증
    return bouns_number


def print_result(result_list, purchase_amount):
    print("\n당첨 통계\n---")

    # 등수별 당첨 개수 저장 딕셔너리 초기화
    score_count = {score: 0 for score in Score if score != Score.NONE}

    # 당첨 개수 세기
    for match_count, bonus_match in result_list:
        score = Score.get_score(match_count, bonus_match)
        if score != Score.NONE:
            score_count[score] += 1

    # 총 당첨 금액 계산
    total_prize = sum(score.prize * count for score, count in score_count.items())

    # 결과 출력
    for score in Score:
        if score == Score.NONE:
            continue  # NONE 등급(낙첨)은 출력하지 않음
        description = f"{score.match_count}개 일치"
        if score.bonus_match == 1:
            description += ", 보너스 볼 일치"
        print(f"{description} ({format(score.prize, ',d')}원) - {score_count[score]}개")

    # 수익률 계산 및 출력
    revenue_rate = (total_prize / purchase_amount) * 100
    print(f"총 수익률은 {revenue_rate:.1f}%입니다.")


def main():
    purchase_amount = input_purchase_amount()  # 구입 금액 입력
    lotto_quantity = generate_lotto_quantity(purchase_amount)  # 로또 수량 계산산

    issued_lotto_list = [Lotto.issuance_lotto() for _ in range(lotto_quantity)]  # 로또 발행
    for lotto in issued_lotto_list:  # 발행된 로또 출력
        print(lotto)

    lotto = input_winning_numbers()  # 당첨 번호 입력

    bonus_number = input_bonus_number(lotto)  # 보너스 번호 입력

    result_list = lotto.calculate_result(issued_lotto_list)

    print_result(result_list, purchase_amount)


if __name__ == "__main__":
    main()
