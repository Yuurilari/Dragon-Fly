import admin
import category

customer = []
sum_customer = []
menu_money = []
money = 0
cost = 0

Alltemp={"ร้อน" : 0,"เย็น" :5,"ปั่น" :10}

Allsize={"S" :0,"M" : 10,"L" : 20}

sweet = ["หวานมาก 100%","หวานปกติ 50%","หวานน้อย 25%","ไม่หวาน 0%"]

def menu_list() :
    global Allmenu
    Allmenu = category.mainmenu()
    print("Menu :")
    count = 0
    for select in Allmenu : #ลูปเมนู
        count += 1
        print(f"{count} : {select} เริ่มต้น : {Allmenu[select]} บาท")
def menu() : #เลือกเมนู น้ำดื่ม
    menu_list()
    global choose_menu #ประกาศตัวแปนเมนูทุกอัน
    while True : #เลืือกเมนู
        try :
            print ("พิมพ์ 88 เพื่อย้อนกลับ")
            choose_menu = int(input("select : "))
        except ValueError : 
            print("กรุณาใส่เฉพาะ ตัวเลข เท่านั้น")
        else :
            if choose_menu == 88 :
                menu_list()
            elif choose_menu == 99 : #เข้า ไฟล์ admin
                admin.login()
                admin_menu()
            elif choose_menu > len(Allmenu) or choose_menu < 1 : #ไม่พบเมนู(เลือกเกินในเมนูที่มี)
                print("ไม่พบเมนูที่คุณต้องการ กรุณาเลือกใหม่")
            else : #เมื่อใส่ตรงกับรายบการในlist
                global cost_menu #ใช้ข้างนอกได้
                global text_menu #ใช้ข้างนอกได้
                check = 0
                for menu in Allmenu : #ดึงkeyในdic allmenu
                    check += 1
                    if check == choose_menu :
                        cost_menu = Allmenu[menu]   #ดึงราคาvalue
                        text_menu = menu #ดึงkey
                break

def temperature() : #เลือกเมนู อุณหภูมิ
    print("Temperature : ")
    count = 0
    for select in Alltemp :  #ลูปDicอุณหภูมิ
        count += 1
        print(f"{count} : {select} {Alltemp[select] + cost_menu} บาท")
    while True : #เลือกอุณหภูมิ
        try : 
            choose_temp = int(input("select Temp : "))
        except ValueError :
            print("กรุณาใส่เฉพาะ ตัวเลข เท่านั้น")
        else :
            if choose_temp > len(Alltemp) or choose_temp < 1 : #ไม่พบอุณหภูมิ(เลือกเกินที่มี)
                print("ไม่พบเมนูที่คุณต้องการ กรุณาเลือกใหม่") 
            else :
                global cost_temp #ใช้ข้างนอกได้
                global text_temp #ใช้ข้างนอกได้
                check = 0
                for temp in Alltemp : #ดึงkeyในdic alltemp
                    check += 1
                    if check == choose_temp :
                        cost_temp = Alltemp[temp] #ดึงราคาvalue
                        text_temp = temp          #ดึงkey
                break  

def size() : #ไซน์แก้ว
    print("Size : ")
    count = 0
    for select in Allsize : #ลูปDic sizeแก้ว
        count += 1
        print(f"{count} : {select} {Allsize[select] + cost_menu + cost_temp} บาท")
    while True : #เลือกSize
        try :
            choose_size = int(input("select Size : "))
        except ValueError :
            print("กรุณาใส่เฉพาะ ตัวเลข เท่านั้น")
        else :
            if choose_size > len(Allsize) or choose_size < 1 : #ไม่พบsize แก้วที่ต้องการ(เลือกเกินที่มี)
                print("ไม่พบเมนูที่คุณต้องการ กรุณาเลือกใหม่") 
            else :
                global cost_size #ใช้ข้างนอกได้
                global text_size #ใช้ข้างนอกได้
                check = 0
                for size in Allsize :
                    check += 1
                    if check == choose_size :
                        cost_size = Allsize[size]   #ดึงราคาvalue
                        text_size = size            #ดึงkey
                break  

def bulb() :
    global addbulb
    while True :
        addbulb = input("คุณต้องการหลอดหริอไม่ ( Y / N ) : ")
        if addbulb == "Y" or addbulb == "y" :
            addbulb = "เอาหลอด"
            break
        elif addbulb == "N" or addbulb == "n" : 
            addbulb = ''
            break
        else :
            print("===============")
            print("กรุณาตอบแค่ Y / N")
            print("===============")

def lid() :
    global addlid
    while True :
        addlid = input("คุณต้องการฝาหริอไม่ ( Y / N ) : ")
        if addlid == "Y" or addlid == "y" :
            addlid = "เอาฝา"
            break
        elif addlid == "N" or addlid == "n" :
            addlid = ''   
            break  
        else :   
            print("===============")
            print("กรุณาตอบแค่ Y / N")
            print("===============")
def sum_menu() : #ฟังก์ชั่น เพิ่มเมนู ใน ลิส และ แสดงเมนู
    order = (f"{text_menu}{text_temp} ขนาด {text_size} {addbulb} {addlid} ราคา : {cost_menu + cost_temp + cost_size} บาท")
    print(f"\n สรุปรายการ : {order} \n")
    moneymenu=cost_menu + cost_temp + cost_size
    menu_money.append(moneymenu)
    sum_customer.append(order)

def cal_money() : #ฟังก์ชั่น คำนวณราคาทั้งหมด
    global money
    money = money + (cost_menu + cost_temp + cost_size)
    return money

def sum_money() : #ช่วยตรงฟังชันก์คิดเงินทั้งหมด
    global money
    return money

def edit_confirm() :#แก้ไขของในตะกร้า
    global money
    money = sum_money()
    print("1.ต้องการลบเมนู")
    print("2.ต้องการเพิ่มเมนู")
    while True :
        editmenu=input("select : ")
        if editmenu=="1" :
            i = 1
            print("---------------------------------- \n")         
            for customer_select in sum_customer :      
                print(i," : ",customer_select)
                i+=1
            print("\n---------------------------------- \n")   
            remenu=int(input("เลือกรายการที่จะลบ : "))
            sum_customer.pop(remenu-1)
            money = money-menu_money[remenu-1]
            menu_money.pop(remenu-1)
            sum_money() 
            break
        elif editmenu=="2" :
            menu() #เมนู
            temperature()
            size()
            bulb()
            lid()
            sum_menu() 
            cal_money() #คิดคำนวณเงิน
            break
        else :
            print("ไม่พบเมนูที่คุณต้องการ กรุณาเลือกใหม่")
       
   
    
#----- Admin Mode -----

def admin_menu():
    print("Menu :")
    count = 0
    for select in Allmenu : #ลูปเมนู
        count += 1
        print(f"{count} : {select} เริ่มต้น : {Allmenu[select]} บาท")
        
def admin_add() : #เพิ่มราคาและเมนูใหม่
    while True :
        Allmenu = category.mainmenu()
        print("พิมพ์ 88 เพื่อย้อนกลับ \n")
        new_drink = input("ชื่อเครื่องดื่มใหม่ : ")
        if new_drink == "88" :
            break
        try :
            new_cost = int(input("ราคา : "))
        except ValueError :
            print("กรุณาใส่ราคาเป็น ตัวเลข เท่านั้น")
        else :
            if new_cost == 99 :
                break
            else :
                Allmenu.update({new_drink : new_cost})
                break
        
def admin_delete() : #ลบ
    while True :
        try :
            menu_list()
            print("พิมพ์ 88 เพื่อย้อนกลับ \n")
            delete_drink = int(input("เลือกลบเมนูไหน : "))
        except ValueError :
            print("กรุณาใส่เฉพาะ ตัวเลข เท่านั้น")
        else :
            if delete_drink == 88 :
                break
            work = False
            check = 0
            if delete_drink > len(Allmenu) or delete_drink < 1 :
                print("ไม่พบเมนูที่คุณต้องการ กรุณาเลือกใหม่")
            else : 
                for select in Allmenu :
                    check += 1
                    if check == delete_drink :
                        Allmenu.pop(select)
                        work = True
                        break
            if work == True :
                break

def admin_edit() : #แก้ไข
    while True :
        try :
            menu_list()
            print("พิมพ์ 88 เพื่อย้อนกลับ \n")
            edit_drink = int(input("เลือกแก้ไขเมนูไหน : "))
        except ValueError :
            print("กรุณาใส่เฉพาะ ตัวเลข เท่านั้น")
        else :
            if edit_drink == 88 :
                break
            check = 0
            work = False
            if edit_drink > len(Allmenu) or edit_drink < 1 :
                print("ไม่พบเมนูที่คุณต้องการ กรุณาเลือกใหม่")
            else :
                    for select in Allmenu :
                        check += 1
                        if check == edit_drink :
                            while work == False :
                                try :
                                    print("พิมพ์ 99 เพื่อย้อนกลับ \n")
                                    edit = int(input(f"แก้ไขราคา ของ {select} เท่าไหร่ : "))
                                except ValueError :
                                    print("กรุณาใส่เฉพาะตัวเลขเท่านั้น")
                                else :
                                    if edit == 99 :
                                        break
                                    Allmenu[select] = edit
                                    work = True
            if work == True :
                break               