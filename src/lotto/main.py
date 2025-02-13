from lotto.lotto import Lotto

def main():
    
    lotto_count = Lotto.get_lotto_count()  # 로또 구입 금액 입력
    
    
    # 2. 로또 번호 생성 (구입한 개수만큼 로또 번호 생성)
    purchased_lottos = Lotto.generate_lottos(lotto_count)

    #  로또 번호 출력
    print(f"\n{lotto_count}개를 구매했습니다.")
    for lotto in purchased_lottos:
        print(f"{lotto._numbers}")  #  리스트 형태를 그대로 출력

    # 3. 당첨 번호와 보너스 번호 입력
    try:
        winning_numbers, bonus_number = Lotto.get_winning_numbers()  # 당첨 번호 및 보너스 번호 입력
    except ValueError as e:
        print(f"[ERROR] {e}")
        return
    
    # 4. 당첨 결과 확인 (로또 번호와 당첨 번호 비교)
    results = Lotto.check_results(purchased_lottos, winning_numbers, bonus_number)

    # 5. 당첨 통계 및 수익률 출력
    total_cost = lotto_count * 1000  # 총 구입 금액
    Lotto.print_results(results, total_cost)

if __name__ == "__main__":
    main()
