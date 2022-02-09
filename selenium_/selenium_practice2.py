import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('E:\PYTHONWORKSPACE\chromedriver.exe') # 브라우저 생성

browser.get('https://front.wemakeprice.com/main') # 웹사이트 열기
browser.implicitly_wait(10) #로딩 10초 대기

#검색창 변수설정
search = browser.find_element_by_xpath('//*[@id="_searchKeyword"]')
search.click()

#검색어 입력
search.send_keys('플레인탄산수')
search.send_keys(Keys.ENTER)

#스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# #무한스크롤
# while True:
#     #맨 아래로 스크롤을 내린다.
#     browser.find_element_by_css_selector("body").send_keys(Keys.END)

#     #페이지 이동 시 로딩
#     time.sleep(5)

#     #스크롤 후 높이
#     after_h = browser.execute_script("return window.scrollY")

#     if after_h == before_h:
#         break
#     before_h = after_h

#상품 정보 div
itemcss = browser.find_elements_by_css_selector(".list_info")

for item in itemcss:
    name = item.find_element_by_css_selector("div > p").text
    
    pricecss = item.find_element_by_css_selector("div > div.list_price > div > div.detail")
    if pricecss == 0 :
        price = item.find_element_by_css_selector("div > div.list_price > div > div > div.price_info > strong > em").text
    else :
        price = item.find_element_by_css_selector("div > div.list_price > div > div.detail > div.price_info > strong > em").text

    
    print(name)
    print(price, "원")
    print('--------------------')