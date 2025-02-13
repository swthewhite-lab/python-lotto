# 🎰 Lotto 프로그램

## 📜 **Lotto 클래스 기능 정리**

### 🎲 **1. 로또 번호 처리**
✅ `__init__(self, numbers: List[int])`  
   - 로또 번호를 입력받아 저장하고 검증합니다.  

✅ `_validate(numbers: List[int])`  
   - 로또 번호가 **6개인지, 중복이 없는지, 1~45 범위 내에 있는지** 검증합니다.

---

### 💰 **2. 로또 구입 관련**
✅ `get_lotto_count()`  
   - 사용자에게 **로또 구입 금액을 입력받고** 구입할 수 있는 개수를 계산합니다.  
   - **1,000원 단위로만 구입 가능**합니다.  

✅ `_validate_amount(amount)`  
   - 입력된 금액이 **숫자인지, 1,000원 이상인지, 1,000원 단위인지** 확인합니다.

---

### 🎟️ **3. 로또 번호 생성**
✅ `generate_random_lotto()`  
   - **1~45 사이의 랜덤한 6개의 숫자**를 생성하여 로또 번호를 만듭니다.  

✅ `generate_lottos(count: int)`  
   - **사용자가 구입한 개수만큼** 로또 번호를 자동 생성합니다.  

---

### 🎯 **4. 당첨 번호 입력**
✅ `get_winning_numbers()`  
   - **사용자로부터 당첨 번호와 보너스 번호를 입력받습니다.**  
   - 입력된 번호가 **유효한지 검증한 후 반환합니다.**  

✅ `_get_valid_numbers(prompt, count)`  
   - **사용자가 입력한 당첨 번호가 6개인지, 유효한 범위(1~45)인지 확인**합니다.  

✅ `_validate_numbers(numbers, count)`  
   - 입력된 숫자가 **개수 조건(6개) 및 범위(1~45)를 만족하는지 검증**합니다.  

✅ `_get_valid_bonus(prompt, numbers)`  
   - **보너스 번호를 입력받아 유효성 검증**을 수행합니다.  

✅ `_is_valid_bonus(bonus, numbers)`  
   - 보너스 번호가 **1~45 사이이며, 당첨 번호와 중복되지 않는지** 확인합니다.  

---

### 🏆 **5. 당첨 결과 비교**
✅ `check_results(purchased_lottos, winning_numbers, bonus_number)`  
   - **구입한 로또 번호와 당첨 번호를 비교**하여 당첨 등수를 결정합니다.  

✅ `_count_matches(lotto_numbers, winning_numbers, bonus_number)`  
   - 각 로또 번호가 **당첨 번호와 몇 개 일치하는지, 보너스 번호가 포함되어 있는지** 확인합니다.  

✅ `_determine_prize_key(matched_count, has_bonus)`  
   - 일치 개수 및 보너스 번호 여부를 바탕으로 **당첨 등수를 판별**합니다.  

---

### 📊 **6. 당첨 결과 출력**
✅ `print_results(results, total_cost)`  
   - **각 당첨 등수별 개수를 출력**합니다.  
   - 총 당첨 금액과 **수익률(%)을 계산하여 출력**합니다.  
