import pytest
from lotto.lotto import Lotto


@pytest.mark.custom_name("로또 번호의 개수가 6개가 넘어가면 예외가 발생한다.")
def test_create_lotto_by_over_size():
    """
    로또 번호가 6개를 초과할 경우 ValueError가 발생해야 합니다.
    """
    with pytest.raises(ValueError):
        Lotto([1, 2, 3, 4, 5, 6, 7])


# 로또 번호 중복 예외 테스트
@pytest.mark.custom_name("로또 번호에 중복된 숫자가 있으면 예외가 발생한다.")
def test_create_lotto_by_duplicated_number():
    """
    로또 번호에 중복된 숫자가 있을 경우 ValueError가 발생해야 합니다.
    """
    with pytest.raises(ValueError):
        Lotto([1, 2, 3, 4, 5, 5])


# 로또 번호 범위 초과 예외 테스트 (예: 46이 포함된 경우)
@pytest.mark.custom_name("로또 번호가 1~45 범위를 벗어나면 예외가 발생한다.")
def test_create_lotto_by_out_of_range():
    with pytest.raises(ValueError):
        Lotto([0, 1, 2, 3, 4, 5])  # 0 포함
    with pytest.raises(ValueError):
        Lotto([1, 2, 3, 4, 5, 46])  # 46 포함


# 보너스 번호 중복 예외 테스트 (보너스 번호가 당첨 번호와 중복)
@pytest.mark.custom_name("보너스 번호가 당첨 번호와 중복되면 예외가 발생한다.")
def test_validate_bonus_number_by_duplicate():
    lotto = Lotto([1, 2, 3, 4, 5, 6])
    with pytest.raises(ValueError):
        lotto.validate_bonus_number(5)  # 기존 당첨 번호와 중복된 보너스 번호


# 보너스 번호 범위 초과 예외 테스트
@pytest.mark.custom_name("보너스 번호가 1~45 범위를 벗어나면 예외가 발생한다.")
def test_validate_bonus_number_by_out_of_range():
    lotto = Lotto([1, 2, 3, 4, 5, 6])
    with pytest.raises(ValueError):
        lotto.validate_bonus_number(0)  # 0 포함
    with pytest.raises(ValueError):
        lotto.validate_bonus_number(46)  # 46 포함


# 로또 자동 발행 시, 6개의 숫자가 포함되어 있는지 확인
@pytest.mark.custom_name("로또 자동 발행 시, 6개의 숫자가 포함되어야 한다.")
def test_issuance_lotto_size():
    numbers = Lotto.issuance_lotto()
    assert len(numbers) == 6


# 로또 자동 발행 시, 숫자가 정렬되어 있는지 확인
@pytest.mark.custom_name("로또 자동 발행 시, 번호가 오름차순 정렬되어야 한다.")
def test_issuance_lotto_sorted():
    numbers = Lotto.issuance_lotto()
    assert numbers == sorted(numbers)


# 로또 번호 비교 테스트 (당첨 개수 확인)
@pytest.mark.custom_name("발행된 로또 번호와 당첨 번호를 비교하여 일치 개수를 확인한다.")
def test_compare_winning_number():
    winning_lotto = Lotto([1, 2, 3, 4, 5, 6])
    issued_numbers = [1, 2, 3, 10, 20, 30]  # 3개 일치
    assert winning_lotto.compare_winning_number(issued_numbers) == 3


# 보너스 번호 비교 테스트
@pytest.mark.custom_name("발행된 로또 번호와 보너스 번호를 비교하여 일치 여부를 확인한다.")
def test_compare_bonus_number():
    winning_lotto = Lotto([1, 2, 3, 4, 5, 6])
    winning_lotto.validate_bonus_number(7)

    issued_numbers = [7, 8, 9, 10, 11, 12]  # 보너스 번호(7) 포함
    assert winning_lotto.compare_bonus_number(issued_numbers) == 1

    issued_numbers = [1, 2, 3, 4, 5, 6]  # 보너스 번호 미포함
    assert winning_lotto.compare_bonus_number(issued_numbers) == 0