import random


def purchase_price_Input () :
    purchase_price=input("구입금액을 입력해 주세요.")
    if not purchase_price.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해야 합니다.")
    
    purchase_price=int(purchase_price)

    if purchase_price %1000 !=0:
        raise ValueError("[ERROR] 1000원 단위로 입력해야 합니다.")
    
    return purchase_price


def winnernumber_Input () :
    winnernumber=input("당첨 번호를 입력해 주세요.").split(',')
    winnernumber=[int(i) for i in winnernumber]
    
    return winnernumber


def bonusnumber_Input():
    bonusnumber=input("보너스 번호를 입력해 주세요.")
    if not bonusnumber.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해야 합니다.")
    
    bonusnumber=int(bonusnumber)

    return bonusnumber


def main():
    purchase_price_Input()
    
if __name__ == "__main__":
    main()
