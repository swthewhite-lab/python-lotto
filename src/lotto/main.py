from .lotto import Rank, Lotto


def check_amount(input_amount):
    """로또 구입 금액 검증"""
    if not input_amount.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해 주세요.")

    amount = int(input_amount)
    if amount % 1000 != 0:
        raise ValueError("구입 금액은 1,000원으로 나누어 떨어져야 합니다.")
    if amount < 1000:
        raise ValueError("구입 금액은 1,000원 이상이어야 합니다.")

    return amount // 1000


def prompt_purchase_amount():
    """로또 구입 금액 입력"""
    print("구입금액을 입력해 주세요.")
    amount = input()
    return check_amount(amount)


def print_lotto_tickets(tickets):
    """구매한 로또 번호 출력"""
    print(f"\n{len(tickets)}개를 구매했습니다.")
    for ticket in tickets:
        print(ticket)  # ✅ `__str__()` 사용하여 출력


def prompt_winning_numbers():
    """당첨 번호 입력"""
    while True:
        print("\n당첨 번호를 입력해 주세요.")
        try:
            winning_numbers = list(map(int, input().split(",")))
            return Lotto(winning_numbers).get_numbers()
        except ValueError as error:
            print(f"[ERROR] {error}")


def check_bonus_number(bonus_num, winning_numbers):
    """보너스 번호 검증"""
    if not bonus_num.isdigit():
        raise ValueError("숫자를 입력해 주세요.")

    bonus_num = int(bonus_num)
    if bonus_num in winning_numbers:
        raise ValueError("보너스 숫자와 입력한 당첨 번호는 중복되지 않아야 합니다.")
    if bonus_num > 45 or bonus_num < 1:
        raise ValueError("로또 번호의 숫자 범위는 1~45까지입니다.")

    return bonus_num


def prompt_bonus_number(winning_numbers):
    """보너스 번호 입력"""
    while True:
        try:
            bonus_num = input("\n보너스 번호를 입력해 주세요.\n")
            return check_bonus_number(bonus_num, winning_numbers)
        except ValueError as error:
            print(f"[ERROR] {error}")


def evaluate_tickets(tickets, winning_numbers, bonus_num):
    """구입한 로또 번호와 당첨 번호 비교"""
    results = {rank: 0 for rank in Rank}
    total_prize = 0

    for ticket in tickets:
        ticket_numbers = ticket.get_numbers()
        match_count = len(set(winning_numbers) & set(ticket_numbers))
        bonus = bonus_num in ticket_numbers

        rank = Rank.get_rank(match_count, bonus)
        results[rank] += 1
        total_prize += rank.prize

    return results, total_prize


def print_results(results, total_prize, amount):
    """당첨 결과 및 수익률 출력"""
    profit_percentage = round((total_prize / (amount * 1000)) * 100, 2)

    print("\n당첨 통계")
    print("---")
    for rank in Rank:
        if rank == Rank.SECOND:
            print(
                f"{rank.match_cnt}개 일치, 보너스 볼 일치 ({rank.prize:,}원) - "
                f"{results[rank]}개"
            )

        if rank != Rank.NONE and rank != Rank.SECOND:
            print(
                f"{rank.match_cnt}개 일치 ({rank.prize:,}원) - "
                f"{results[rank]}개"
            )

    print(f"총 수익률은 {profit_percentage}%입니다.")


def main():
    """로또 게임 실행"""
    amount = prompt_purchase_amount()
    tickets = [Lotto.generate_randomlotto() for _ in range(amount)]
    print_lotto_tickets(tickets)

    winning_numbers = prompt_winning_numbers()
    bonus_num = prompt_bonus_number(winning_numbers)

    results, total_prize = evaluate_tickets(
        tickets, winning_numbers, bonus_num
    )
    print_results(results, total_prize, amount)


if __name__ == "__main__":
    main()
