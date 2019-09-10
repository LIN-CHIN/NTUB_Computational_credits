import urllib.request
import selenium.webdriver
import bs4
import  PIL
import pytesseract
import courseSum
import subprocess
# subprocess.call('dir', shell=True)


def getNtubData(url,user , pwd):

    driver = selenium.webdriver.Chrome("./chromedriver")
    driver.get(url)

    ## 解析
    html = bs4.BeautifulSoup(driver.page_source, "html.parser")
    saveCodeImg(html)
    image = PIL.Image.open("img1.jpg")
    # 驗證碼(圖片轉換成字元)
    checkCode = pytesseract.image_to_string(image)
    login(user, pwd, checkCode, driver)

    # -------------------------------------------------------#
    driver.implicitly_wait(15)  # 等待
    driver.find_element_by_id("loginbtn").click()
    driver.implicitly_wait(15)  # 等待
    driver.find_element_by_class_name("ThemePanelMainItem").click()
    driver.implicitly_wait(15)  # 等待
    driver.find_elements_by_link_text("歷年成績查詢")[0].click()
    driver.implicitly_wait(15)  # 等待
    html = bs4.BeautifulSoup(driver.page_source, "html.parser")

    table = html.findAll("table", class_="GridViewScroll")
    tbody = table[1].findAll("tbody")

    tr_Style1 = tbody[0].findAll("tr", class_="RowStyle")
    tr_Style2 = tbody[0].findAll("tr", class_="AlternatingRowStyle")
    data = []

    getCourseData(tr_Style1, data)
    getCourseData(tr_Style2, data)

    courseSum.sum(data)


def saveCodeImg(html) :
    imgTag = html.find("img", id="ImgCheckCode")
    imgSrc = imgTag["src"]
    imgSrc = "http://ntcbadm.ntub.edu.tw/" + imgSrc
    imgTag = html.find("img", id="ImgCheckCode")
    imgSrc = imgTag["src"]
    imgSrc = "http://ntcbadm.ntub.edu.tw/" + imgSrc
    urllib.request.urlretrieve(imgSrc, './img1.jpg')

def login(user,pwd,checkCode,driver):
    driver.find_element_by_id("UserID").send_keys(user)
    driver.find_element_by_id("PWD").send_keys(pwd)
    driver.find_element_by_id("txtCheckCode").send_keys(checkCode)
    driver.maximize_window()  # 最大化

def getCourseData(tr, data):
    for a in tr:
        td = a.findAll("td")
        temp = 1
        myArray = []
        for b in td:
            b.text.strip()
            if (temp == 4 or temp == 5 or temp == 6 or temp == 7):
                myArray.append(b.text)
            temp += 1
        data.append(myArray)




