import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl



#엑셀 생성
wb = openpyxl.Workbook()

#sheet활성
sheet = wb.active

#데이터프레임 내 변수명 생성
sheet.append(["상품명", "가격"])



browser = webdriver.Chrome('E:\PYTHONWORKSPACE\chromedriver.exe') # 브라우저 생성

browser.get('https://front.wemakeprice.com/main') # 웹사이트 열기
browser.implicitly_wait(10) #로딩 10초 대기

#검색창 변수설정
search = browser.find_element_by_xpath('//*[@id="_searchKeyword"]')
search.click()

#검색어 입력
search.send_keys('플레인탄산수')
search.send_keys(Keys.ENTER)

#상품 정보 div
itemcss = browser.find_elements_by_css_selector(".list_info")

for item in itemcss:
    name = item.find_element_by_css_selector("div > p").text
    
    pricecss = item.find_element_by_css_selector("div > div.list_price > div > div.detail")
    if pricecss == 0 :
        price = item.find_element_by_css_selector("div > div.list_price > div > div > div.price_info > strong > em").text
    else :
        price = item.find_element_by_css_selector("div > div.list_price > div > div.detail > div.price_info > strong > em").text

    sheet.append([name, price])
    print(name)
    print(price, "원")
    print('--------------------')



#엑셀저장
wb.save("report.xlsx")