import driver


if __name__ == '__main__' :
    url = "http://ntcbadm.ntub.edu.tw/login.aspx?Type=2"

    ## 輸入文字 ##
    user = input("帳號")
    pwd = input("密碼")
    while(user == "" or pwd == ""):
        user = input("帳號")
        pwd = input("密碼")

    driver.getNtubData(url,user,pwd)
    input()
