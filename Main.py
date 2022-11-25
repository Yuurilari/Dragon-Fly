import select
import value
#main program
question = ["Y","y","N","n"]
program = "Y"
while True :
    if program == "Y" or program == "y" :
        select.menu() #เมนู
        select.temperature()
        select.size()
        select.bulb()
        select.lid()
        select.sum_menu() 
        select.cal_money() #คิดคำนวณเงิน
        while True :
            program = input("ต้องการเลือกเครื่องดื่มต่อหรือไม่ ( Y / N ) : ") #เลือกต่อรึเปล่า
            if program not in question :
                print("===============")
                print("กรุณาตอบแค่ Y / N")
                print("===============")
            else : 
                break
    else :
        break
credit = value.sum()
Nomoney="Y"
while True :#ยืนยันการจ่ายเงิน
    if Nomoney == "N" or Nomoney == "n" :
        break
    money = select.sum_money()
    print("---------------------------------- \n")         
    for customer_select in select.sum_customer :      
        print(customer_select)
    print("\n---------------------------------- \n")      
    print("จำนวนเงินที่ต้องจ่ายทั้งหมด : ",money," บาท")
    confirm = input("คุณยืนยันที่จะชำระรายการที่เลือกไว้หรือไม่ ( Y / N ) : ")
    credit = value.sum()
    if confirm == "Y" or confirm == "y" :#ยืนยัน
        if money > credit :
            while True :
                Nomoney = input("เงินคุณไม่เพียงพอต้องการเติมเงินเพิ่มหรือไม่ ( Y / N ) :")
                if Nomoney == "Y" or Nomoney == "y" :
                    value.add()
                    break
                elif Nomoney == "N" or Nomoney == "n" :
                    print("คุณไม่จ่ายเงิน ไม่สามารถทำเครื่องดื่มให้คุณได้ (จบ)")
                    break
                else :
                    print("===============")
                    print("กรุณาตอบแค่ Y / N")
                    print("===============")
        else :
            change=credit-money
            print("---------------------------------- \n")         
            for customer_select in select.sum_customer :      
                print(customer_select)
            print("\n---------------------------------- \n") 
            print("ยอดเงินคงเหลือ",change,"บาท") 
            print("รายการที่ท่านเลือกได้รับการชำระเงินเรียบร้อยแล้ว ขอบคุณที่ใช้บริการ")
            break
    elif confirm == "N" or confirm == "n" :#แก้ไข
        select.edit_confirm()
    else :
        print("===============")
        print("กรุณาตอบแค่ Y / N")
        print("===============")