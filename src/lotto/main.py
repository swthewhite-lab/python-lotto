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
    purchase_price=purchase_price//1000
    print("%d개를 구입했습니다." %purchase_price)
    return purchase_price


def winnernumber_Input () :
    winnernumber=input("당첨 번호를 입력해 주세요.").split(',')
    winnernumber=Exception_handling(winnernumber)
    winnernumber.sort()

    return winnernumber


def bonusnumber_Input():
    bonusnumber=input("보너스 번호를 입력해 주세요.")
    if not bonusnumber.isdigit():
        raise ValueError("[ERROR] 숫자를 입력해야 합니다.")
    
    bonusnumber=int(bonusnumber)

    return bonusnumber


def lottonumber():
    lotto=set()
    while len(lotto)<=5:
        a=random.randint(1,45)
        lotto.add(a)
    lotto=list(lotto)
    lotto.sort()

    return lotto


def compare(a,b,c) :
    count=0
    for i,num in enumerate(a) :
        if num in b :
            count+=1
    count=count*10
    if c in a :
        count+=1

    return count


def price(x):
    if x==30 :
        return "5000"
    elif x==40 :
        return "50000"
    elif x==50 :
        return "1,000,000"
    elif x==51 :
        return "1,500,000"
    elif x==60 :
        return "2,000,000,000"

def main():
    lottocount=purchase_price_Input()
    count=1
    lottonumbers=[]
    while count<=lottocount :
        a=lottonumber()
        print(a)
        lottonumbers.append(a)
        count+=1

    winnumber=winnernumber_Input()
    bonusnumber=bonusnumber_Input()
    

    wincount={"30": 0,"40": 0,"50": 0,"51": 0,"60": 0}
    for i in range(lottocount):
        win=compare(lottonumbers[i],winnumber,bonusnumber)
        print(win)
        if win == 30:
            wincount["30"]+=1
        if win == 40:
            wincount["40"]+=1
        if win == 50:
            wincount["50"]+=1
        if win == 51:
            wincount["51"]+=1
        if win == 60:
            wincount["60"]+=1

    print("당첨 통계")
    print("---")
    print(wincount)
    
   
        


if __name__ == "__main__":
    main()
