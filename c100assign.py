class ATM():
    def __init__(self,cashWithDrawn,cardNo,pinNo):
        self.cardNo=cardNo
        self.cashWithDrawn=cashWithDrawn
        self.pinNo=pinNo
    
    def atmInfo(self):
        print('cardNumber:',self.cardNo)
        print('cashAmount:',self.cashWithDrawn)
        print('pinNumber',self.pinNo)
        print("cash withdrawn successfully")

cashWithDrawn=int(input("enter the cash amount: "))
cardNo=int(input("enter the card number: "))
pinNo=int(input("enter the pin code: "))

man1=ATM(cardNo,cashWithDrawn,pinNo)
man1.atmInfo()