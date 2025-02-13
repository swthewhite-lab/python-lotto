import random


def Exception_handling(x):
    if len(x) != 6:
        raise ValueError("[ERROR] 당첨 번호는 6개여야 합니다.")
    x=[int(i) for i in x]

    if any(n < 1 or n > 45 for n in x):
        raise ValueError("[ERROR] 로또 번호는 1부터 45 사이의 숫자여야 합니다.")
    if len(set(x)) != 6:
        raise ValueError("[ERROR] 중복되지 않은 6개의 숫자를 입력해야 합니다.")

    return x 


def purchase_price_Input () :
    purchase_price=input("구입금액을 입력해 주세요.")
    if not purchase_price.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해야 합니다.")
    
    purchase_price=int(purchase_price)

    if purchase_price %1000 !=0:
        raise ValueError("[ERROR] 1000원 단위로 입력해야 합니다.")
    purchase_price=purchase_price/1000
    print("%d개를 구입했습니다." %purchase_price)
    return purchase_price


def winnernumber_Input () :
    winnernumber=input("당첨 번호를 입력해 주세요.").split(',')
    winnernumber=Exception_handling(winnernumber)

    return winnernumber


def bonusnumber_Input():
    bonusnumber=input("보너스 번호를 입력해 주세요.")
    if not bonusnumber.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해야 합니다.")
    
    bonusnumber=int(bonusnumber)

    return bonusnumber


def lottonumber():
    lotto=[]
    while len(lotto)<=6:
        a=random.randint(1,45)
        lotto.append(a)
    lotto.sort()
    
    return lotto


def main():
    lottocount=purchase_price_Input()
    count=1

    while count<=lottocount :
        a=lottonumber()
        print(a)

        count+=1
    pass

if __name__ == "__main__":
    main()
