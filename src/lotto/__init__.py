# 📌 이 패키지는 로또 관련 기능을 제공하는 모듈입니다.
# 외부에서 `from lotto import Lotto`와 같은 방식으로 사용할 수 있도록 
# 필요한 모듈을 여기에 등록하세요.
#
# ✅ 새로운 모듈을 추가할 경우:
# - `from .[모듈명] import [클래스/함수]` 형식으로 추가하세요.
# - 필요한 경우 `__all__`에 추가하여 패키지 외부에서 명확하게 사용할 수 있도록 정의하세요.
# - `flake8`의 F401 경고(`imported but unused`)가 발생하는 경우, `__all__`을 활용해 해결하세요.

from .lotto import Lotto  # 🎲 로또 번호 생성 및 검증을 위한 클래스

# 패키지 외부에서 `from lotto import *` 사용 시 제공할 모듈을 명시적으로 정의합니다.
__all__ = ["Lotto"]

# 💡 예시: 새로운 모듈을 추가할 때
# from .other_module import OtherClass  # 🆕 예: 새로운 클래스 추가 시
# __all__.append("OtherClass")  # `__all__`에 추가하여 외부에서 접근 가능하게 함.
