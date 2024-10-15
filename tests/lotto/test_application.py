import pytest
from unittest.mock import patch
from lotto.main import main

# 기능 테스트
def test_기능_테스트(capsys):
    # random.sample 모의 처리: 로또 번호 리스트를 고정된 값으로 설정
    with patch('random.sample', side_effect=[
        [8, 21, 23, 41, 42, 43], [3, 5, 11, 16, 32, 38], [7, 11, 16, 35, 36, 44],
        [1, 8, 11, 31, 41, 42], [13, 14, 16, 38, 42, 45], [7, 11, 30, 40, 42, 43],
        [2, 13, 22, 32, 38, 45], [1, 3, 5, 14, 22, 45]
    ]):
        # 사용자 입력을 모의 처리
        입력값 = iter(["8000", "1,2,3,4,5,6", "7"])
        with patch('builtins.input', side_effect=입력값):
            main()  # main 함수 실행

        # 출력 결과 캡처
        캡처된_출력 = capsys.readouterr().out
        
        # 기대하는 출력값이 포함되어 있는지 확인
        assert "8개를 구매했습니다." in 캡처된_출력
        assert "[8, 21, 23, 41, 42, 43]" in 캡처된_출력
        assert "[3, 5, 11, 16, 32, 38]" in 캡처된_출력
        assert "[7, 11, 16, 35, 36, 44]" in 캡처된_출력
        assert "[1, 8, 11, 31, 41, 42]" in 캡처된_출력
        assert "[13, 14, 16, 38, 42, 45]" in 캡처된_출력
        assert "[7, 11, 30, 40, 42, 43]" in 캡처된_출력
        assert "[2, 13, 22, 32, 38, 45]" in 캡처된_출력
        assert "[1, 3, 5, 14, 22, 45]" in 캡처된_출력
        assert "3개 일치 (5,000원) - 1개" in 캡처된_출력
        assert "4개 일치 (50,000원) - 0개" in 캡처된_출력
        assert "5개 일치 (1,500,000원) - 0개" in 캡처된_출력
        assert "5개 일치, 보너스 볼 일치 (30,000,000원) - 0개" in 캡처된_출력
        assert "6개 일치 (2,000,000,000원) - 0개" in 캡처된_출력
        assert "총 수익률은 62.5%" in 캡처된_출력

# 예외 테스트
def test_예외_테스트():
    # 잘못된 입력값으로 예외 발생 여부 테스트
    with pytest.raises(ValueError, match=r"\[ERROR\]"):
        입력값 = iter(["1000j"])  # 잘못된 금액 입력
        with patch('builtins.input', side_effect=입력값):
            main()
