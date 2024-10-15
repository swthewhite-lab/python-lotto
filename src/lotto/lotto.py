class Lotto:
    def __init__(self, numbers):
        self.validate(numbers)
        self._numbers = numbers

    def validate(self, numbers):
        if len(numbers) != 6:
            raise ValueError("로또 번호는 6개의 숫자여야 합니다.")
        # TODO: 추가 유효성 검사 구현

    # TODO: 추가 기능 구현
