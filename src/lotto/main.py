from .lotto import Lotto, Rank



def _validate_amount(amount):
        """로또 금액 검증"""
        # 숫자만 포함된 문자열인지 확인
        if not amount.isdigit():  # 숫자가 아닌 문자가 포함되면 예외
            raise ValueError("[ERROR] 숫자를 입력하세요.")
        
        amount = int(amount)  # 숫자로 변환
        if amount < 1000 or amount % 1000 != 0:  # 금액이 1000원 이상이거나 1000원 단위로 입력되지 않으면 예외
            raise ValueError("[ERROR] 1000원 단위로 입력해야 합니다. .")
        
        
def get_lotto_count():
        """로또 구입 금액 입력 및 예외 처리"""
        try:
            amount = input("로또 구입 금액을 입력하세요: ")
            _validate_amount(amount)

            amount = int(amount)
            lotto_count = amount // 1000
            print(f"{lotto_count}개의 로또를 구입합니다.")
            return lotto_count
        except ValueError as e:
            print(e)
            raise



def _validate_numbers(numbers, count):
        """입력된 숫자 검증"""
        if len(numbers) != count or len(set(numbers)) != count:
            raise ValueError(f"[ERROR] {count}개의 숫자를 입력해야 하며, 중복이 없어야 합니다.")
        if not all(1 <= num <= 45 for num in numbers):
            raise ValueError("[ERROR] 숫자는 1부터 45 사이여야 합니다.")

def print_lotto_tickets(tickets):
    print(f"\n{len(tickets)}개를 구매했습니다.")
    for ticket in tickets:
        print(ticket)

def get_winning_numbers():
    while True:
        print("\n당첨 번호를 입력해 주세요.")
        try:
            winning_numbers = list(map(int, input().split(",")))
            count=len(winning_numbers)
            _validate_numbers(winning_numbers,count)
            print(str(winning_numbers))
            return winning_numbers
        except ValueError as error:
            print(f"[ERROR] {error}")

def check_bonus_number(bonus_num, winning_numbers):
    if not bonus_num.isdigit():
        raise ValueError("숫자를 입력해 주세요.")
    if int(bonus_num) in winning_numbers:
        raise ValueError("보너스 숫자와 입력한 당첨 번호는 중복되지 않아야 합니다.")
    if int(bonus_num) > 45 or int(bonus_num) < 1:
        raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")
    return int(bonus_num)


def get_bonus_number(winning_numbers):
    """보너스 번호 입력 (유효성 검증 포함)"""
    while True:
        try:
            bonus_number = input("보너스 번호를 입력하세요: ")  
            return check_bonus_number(bonus_number, winning_numbers)
        except ValueError as error:
            print(f"[ERROR] {error}")



def check_results(purchased_lottos, winning_numbers, bonus_number):
    """구입한 로또 번호와 당첨 번호 비교"""

    # ✅ Rank.NONE도 포함하도록 초기화
    results = {rank: 0 for rank in Rank}
    totalprize = 0

    for lotto in purchased_lottos:
        lotto_numbers = lotto.get_numbers()  # ✅ 리스트 형태의 로또 번호 가져오기
        matched_count = len(set(lotto_numbers) & set(winning_numbers))  # ✅ 로또 번호 비교
        has_bonus = bonus_number in lotto_numbers  # ✅ 보너스 번호가 포함되어 있는지 확인

        rank = Rank.get_rank(matched_count, has_bonus)  # ✅ 항상 Rank 객체 반환
        results[rank] += 1  # ✅ 꽝(0개 맞춤)도 정상 카운트됨
        totalprize += rank.prize  # ✅ 당첨 금액 합산

    return results, totalprize



def print_result(result, totalprize, amount):
    profit_percentage = round((totalprize / (amount * 1000)) * 100, 2)

    print("\n당첨 통계")
    print("---")
    for rank in Rank:
        if rank == Rank.SECOND:
            print(f"{rank.match_cnt}개 일치, 보너스 볼 일치 ({rank.prize:,}원) - "
                  f"{result[rank]}개")

        if rank != Rank.NONE and rank != Rank.SECOND:
            print(f"{rank.match_cnt}개 일치 ({rank.prize:,}원) - "
                  f"{result[rank]}개")

    print(f"총 수익률은 {profit_percentage}%입니다.")

def main():
    
    lotto_count = get_lotto_count()  # 로또 구입 금액 입력
    
    
    # 2. 로또 번호 생성 (구입한 개수만큼 로또 번호 생성)
    purchased_lottos = [Lotto.generate_random_lotto() for _ in range(lotto_count)]
    print(purchased_lottos)


    # 3. 당첨 번호와 보너스 번호 입력
    
    winning_numbers = get_winning_numbers()  # 당첨 번호 및 보너스 번호 입력
    bonus_number = get_bonus_number(winning_numbers)
    
    # 4. 당첨 결과 확인 (로또 번호와 당첨 번호 비교)
    results, totalprize = check_results(purchased_lottos, winning_numbers, bonus_number)

    # 5. 당첨 통계 및 수익률 출력
    total_cost = lotto_count * 1000  # 총 구입 금액
    print_result(results, totalprize, total_cost)

if __name__ == "__main__":
    main()
