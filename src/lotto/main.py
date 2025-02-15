from .lotto import Rank, Lotto

def check_amount(input_amount):
    if not input_amount.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해 주세요.")
    if int(input_amount) % 1000 != 0:
        raise ValueError("구입 금액은 1,000원으로 나누어 떨어져야 합니다.")
    if int(input_amount) < 1000:
        raise ValueError("구입 금액은 1,000원 이상이어야 합니다.")
    return int(input_amount) // 1000

def prompt_purchase_amount():
    while True:
        try:
            print("구입금액을 입력해 주세요.")
            amount = input()
            return check_amount(amount)
        except ValueError as error:
            print(f"[ERROR] {error}")
            raise

def print_lotto_tickets(tickets):
    print(f"\n{len(tickets)}개를 구매했습니다.")
    for ticket in tickets:
        print(ticket)  # ✅ __str__() 사용하여 출력

def prompt_winning_numbers():
    while True:
        print("\n당첨 번호를 입력해 주세요.")
        try:
            winning_numbers = list(map(int, input().split(",")))
            return Lotto(winning_numbers).get_numbers()
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

def prompt_bonus_number(winning_numbers):
    while True:
        try:
            bonus_num = input("\n보너스 번호를 입력해 주세요.\n")
            return check_bonus_number(bonus_num, winning_numbers)
        except ValueError as error:
            print(f"[ERROR] {error}")

def evaluate_tickets(tickets, winning_numbers, bonus_num):
    results = {rank: 0 for rank in Rank}
    total_prize = 0

    for ticket in tickets:
        ticket_numbers = ticket.get_numbers()  # ✅ 변수명 변경
        match_count = len(set(winning_numbers) & set(ticket_numbers))  # ✅ 비교 순서 통일
        bonus = bonus_num in ticket_numbers  # ✅ 보너스 번호 `int` 변환 후 비교

        rank = Rank.get_rank(match_count, bonus)
        results[rank] += 1
        total_prize += rank.prize

    return results, total_prize

def print_results(results, total_prize, amount):
    profit_percentage = round((total_prize / (amount * 1000)) * 100, 2)

    print("\n당첨 통계")
    print("---")
    for rank in Rank:
        if rank == Rank.SECOND:
            print(f"{rank.match_cnt}개 일치, 보너스 볼 일치 ({rank.prize:,}원) - "
                  f"{results[rank]}개")

        if rank != Rank.NONE and rank != Rank.SECOND:
            print(f"{rank.match_cnt}개 일치 ({rank.prize:,}원) - "
                  f"{results[rank]}개")

    print(f"총 수익률은 {profit_percentage}%입니다.")

def main():
    amount = prompt_purchase_amount()
    tickets = [Lotto.generate_random_lotto() for _ in range(amount)]  # ✅ 메서드명 수정
    print_lotto_tickets(tickets)

    winning_numbers = prompt_winning_numbers()
    bonus_num = prompt_bonus_number(winning_numbers)  # ✅ `int` 변환 적용

    results, total_prize = evaluate_tickets(tickets, winning_numbers, bonus_num)
    print_results(results, total_prize, amount)

if __name__ == "__main__":
    main()
