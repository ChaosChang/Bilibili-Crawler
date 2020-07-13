from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.request#有的时候要分开引用
import os
import re
import codecs
import time

desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
# desired_capabilities["pageLoadStrategy"] = "none"
apath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(apath)


def wuxian():  # Changed in settings.Just search typo
    # 
    """
    f1 = open('test3.txt', 'w', encoding='utf-8')
    # fiction list grab
    # http://www.txt53.com/html/xuanhuan/list_21_ 370
    # http://www.txt53.com/html/yanqing/list_58_ 245
    # http://www.txt53.com/html/wuxiaxianxia/list_29_ 140
    # http://www.txt53.com/html/dushi/list_35_ 237
    # http://www.txt53.com/html/wangyoujingji2/list_47_ 65
    # http://www.txt53.com/html/kehuanxiaoshuo/list_70_ 24
    # http://www.txt53.com/html/xuanyituili/list_71_ 9
    # http://www.txt53.com/html/qita/list_45_ 99
    for i in range(13, 371):
        url = "http://www.txt53.com/html/xuanhuan/list_21_" + repr(i) + ".html"
        xpath = "/html/body/div[1]/div[5]/div[2]/div[3]/ul"
        driver.get(url)
        fics = driver.find_elements_by_xpath(xpath)

        # for count in range(len(fics)-1, -1, -1):
        for fic in fics:
            f1.write(fic.text)
            f1.write("\r\n")
            print(i)
    """


def qidian():
    # 起点
    """
    Still Testing
    maybe need server hacking
    :return:
    """


def biquge():

    """
    f1 = open('test2.txt', 'w', encoding='utf-8')
    url = "https://www.biquge5200.com/2_2598/"
    driver.get(url)
    xpath = "//*[@id='list']/dl/dd/a"
    sections = driver.find_elements_by_xpath(xpath)
    f_url = []
    for sec in sections:
        f_url.append(sec.get_attribute("href"))
    for i in range(9, len(f_url)):
        driver.get(f_url[i])
        t_xpath = "//*[@id='wrapper']/div[4]/div/div[2]/h1"
        w_title = driver.find_element_by_xpath(t_xpath)
        title = w_title.text
        print(title)
        f1.write(title + '\r\n')
        f_xpath = "//*[@id='content']"
        text = driver.find_element_by_xpath(f_xpath)
        novel = text.text
        f1.write(novel + '\r\n')
    """


def newbiquge():
    
    f1 = open('test1.txt', 'w', encoding='utf-8')
    url = "" # website already crashed
    # locator = (By.LINK_TEXT, '第2084章 大结局')
    # driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    finally:
        # driver.execute_script('window.stop()')
        # WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located(locator))
        # xpath = "//*[@id='list']/dl/dd/a"
        xpath = "//*[@id='main']/div[3]/ul/li/a"
        # time.sleep(5)
        sections = driver.find_elements_by_xpath(xpath)
        f_url = []
        for sec in sections:
            f_url.append(sec.get_attribute("href"))
        for i in range(864, len(f_url)):
            # driver.set_page_load_timeout(2)
            driver.get(f_url[i])
            # time.sleep(5)
            # t_xpath = "//*[@id='wrapper']/div[4]/div/div[2]/h1"
            t_xpath = "//*[@id='main']/div[2]/div[1]/p[1]"
            w_title = driver.find_element_by_xpath(t_xpath)
            title = w_title.text
            print(title)
            f1.write(title + '\r\n')
            f_xpath = "//*[@id='content']"
            text = driver.find_element_by_xpath(f_xpath)
            novel = text.text
            f1.write(novel + '\r\n')

    driver.quit()
    f1.close()


def zhengze():
    # 早期版本
    """
    sss = driver.page_source
    if not sss is None:
        ''''''
        res = r'<li><a href="/13/13456/(.+?)">第'  # 章节爬取
        link = re.findall(res, sss)
        for ll in link:
            driver.get(path+ll)
            ttt = driver.page_source
            if not ttt is None:
                res2 = r'<h1>(.+?)</h1>'  # 标题爬取
                header = re.findall(res2, ttt)
                for title in header:
                    f1.write(title+'\r\n')
                f1.write('\r\n')

                res3 = r'\xa0\xa0\xa0\xa0(.+?)\n'  # 正文爬取
                text = re.findall(res3,ttt)
                for body in text:
                    body = re.split(r'<br />', body)
                    str = body[0]
                    f1.write(str+'\r\n')
                f1.write('\r\n')

    else:
        pass
    """

if __name__ == '__main__':
    newbiquge()

