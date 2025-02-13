"""main.py: 로또 프로그램의 실행을 담당하는 메인 스크립트"""

from lotto import Lotto


def main():
    """로또 프로그램 실행 함수"""
    # 1. 로또 구입 개수 입력
    lotto_count = Lotto.get_lotto_count()

    # 2. 로또 번호 생성
    purchased_lottos = Lotto.generate_lottos(lotto_count)

    # 📌 요구된 형식으로 출력
    print(f"\n{lotto_count}개를 구매했습니다.")
    for lotto in purchased_lottos:
        print(f"{lotto.numbers}")  # ✅ 리스트 형태를 그대로 출력

    # 3. 당첨 번호 및 보너스 번호 입력
    winning_numbers, bonus_number = Lotto.get_winning_numbers()

    # 4. 당첨 결과 확인
    results = Lotto.check_results(
        purchased_lottos,
        winning_numbers,
        bonus_number
    )

    # 5. 당첨 통계 및 수익률 출력
    total_cost = lotto_count * 1000  # 총 구입 금액
    Lotto.print_results(results, total_cost)


if __name__ == "__main__":
    main()
