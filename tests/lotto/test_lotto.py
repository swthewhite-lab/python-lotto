import pytest
from lotto.main import Lotto


# 로또 번호 개수 예외 테스트
def test_로또_번호_개수_초과():
    """
    로또 번호가 6개를 초과할 경우 ValueError가 발생해야 합니다.
    """
    with pytest.raises(ValueError, match=r"로또 번호는 6개의 숫자여야 합니다."):
        Lotto([1, 2, 3, 4, 5, 6, 7])


# 로또 번호 중복 예외 테스트
def test_로또_번호_중복_예외():
    """
    로또 번호에 중복된 숫자가 있을 경우 ValueError가 발생해야 합니다.
    """
    with pytest.raises(ValueError, match=r"로또 번호에 중복된 숫자가 있습니다."):
        Lotto([1, 2, 3, 4, 5, 5])


# 추가 테스트 작성 가능
