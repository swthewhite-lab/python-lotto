def purchase_price_Input () :
    purchase_price=int(input("구입금액을 입력해 주세요."))
    return purchase_price

def main():
    a=purchase_price_Input()
    print(a)
if __name__ == "__main__":
    main()
