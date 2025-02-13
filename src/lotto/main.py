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
    lotto=[]
    while len(lotto)<=6:
        a=random.randint(1,45)
        lotto.append(a)
    lotto.sort()

    return lotto


def compare(a,b,c) :
    count=0
    for x,y in enumerate(zip(a,b)) :
        if x==y :
            count+=1
    count=count*10
    if c in a :
        count+=1

    return count


def price(x):
    y=x%10
    if x==3 :
        return "5000"
    elif x==4 :
        return "50000"
    elif x==5 and y==1 :
        return "1,500,000"
    elif x==6 :
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
    

    wincount=[]
    for i in range(lottocount):
        win=compare(lottonumbers[i],winnumber,bonusnumber)
        wincount.append(win)
    
    print("당첨 통계")
    print("---")
    print(wincount)
    '''
    for i in range(len(lottocount)):
        print("%d개 일치 %d")
    '''

if __name__ == "__main__":
    main()
