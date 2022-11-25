admin_mode = ["add" , "delete" , "edit","end"]#เริ่มต้น admin

import select
def login() :
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "1234" :
        while True :
            print("\n ----- Admin Mode Activate ---- \n")
            admin_menu()
            try :
                choose = int(input("choose Mode :")) #เริ่มเข้า if ในเมนู admin
            except ValueError :
                print("ใส่เฉพาะตัวเลขเท่านั้น")
            else :
                if choose == 1 :
                    select.admin_add()
                elif choose == 2 :
                    select.admin_delete()
                elif choose == 3 :
                    select.admin_edit()
                elif choose == 4 :
                    break
                else : 
                    print("ไม่มี คำสั่งนี้ โปรดเลือกใหม่")            
    else : 
        print("--- Login Error back to menu --- \n")
def admin_menu() : #เข้าเลือก menu ใน admin_mode
    print("Admin Mode : ")
    global count
    count = 0
    for select in admin_mode :
        count += 1
        print(f"{count} : {select}")
                