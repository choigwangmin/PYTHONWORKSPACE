# #스크롤 전 높이
# before_h = browser.execute_script("return window.scrollY")

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