credit = 0
sum_credit = 0 

def add() :
    global credit
    global sum_credit
    print(f"เงินปัจจุบันของคุณ : {sum_credit} บาท")
    while True :
        try :
            credit = float(input("คุณต้องการเติมเงินเท่าไหร่ : "))
            sum_credit = sum_credit + credit
        except ValueError :
            print("กรุณาใส่เฉพาะตัวเลขเท่านั้น")
        else :
            if credit < 0 :
                print("กรุณาระบุเงินใหม่อีกครั้ง")
            else :
                print(f"เงินปัจจุบันของคุณ : {sum_credit} บาท")
                return sum_credit
def sum() :
    return sum_credit