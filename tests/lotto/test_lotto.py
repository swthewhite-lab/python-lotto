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


# 추가 테스트 작성 가능
