from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request  # 有的时候要分开引用
import os
import re
import time

page_num = 5


def save(page_real, filename):
    urllib.request.urlretrieve(page_real, 'D:\\bili\\' + filename)
    save()

apath = os.path.abspath(r"C:\Users\T5-SKYLAKE\AppData\Local\Google\Chrome\Application\chromedriver.exe")
# //*[@id="videolist_box"]/div[2]/div[2]/ul/li[1]/button

for i in range(0, 20):
    driver = webdriver.Chrome(apath)

    # for i in range(1,2):
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, 't')  # 新建标签页

    for j_counter in range(0, page_num):
        # time.sleep(1)
        # js = "window.open(\""+path+"\")"
        js = "window.open("")"
        driver.execute_script(js)  # 打开新窗口

    windows = driver.window_handles

    # otaku 7700
    # three_d 5233
    pagenum = 2587

    for count in range(pagenum, pagenum + page_num):

        driver.switch_to_window(windows[count - pagenum])
        # three_d
        path = "https://www.bilibili.com/v/dance/otaku/#/all/default/0/" + repr(count-i*page_num) + "/"
        driver.get(path)

        # 访问源代码，谷歌为例直接在网址前面加上view-source:
        # test=driver.find_element_by_tag_name('body')
        for n in range(1, 16):  # 鼠标拖拽事件模拟
            driver.execute_script('window.scrollBy(0,120)')
            time.sleep(0.15)

        # 动态加载整个页面，模拟鼠标事件

        # sss= driver.page_source
        # //*[@id="videolist_box"]/div[2]/ul/li[1]/div/div[1]/div/a/div/div[1]/img
        # //*[@id="videolist_box"]/div[2]/ul/li[2]/div/div[1]/div/a/div/div[1]/img
        link = driver.find_elements_by_xpath("//*[@id='videolist_box']/div[2]/ul/li/div/div[1]/div/a/div/div[1]/img")
        av_bangou = driver.find_elements_by_xpath("//*[@id='videolist_box']/div[2]/ul/li/div/div[1]/div/a")

        av = []

        for aa in av_bangou:
            avname = aa.get_attribute("href")
            avname = avname.split('/')[4]
            av.append(avname)

        counter = 0

        if not link is None:
            for ll in link:
                real = ll.get_attribute("src")
                filename = real.split('@')[0]  #
                real = filename
                filename = filename.split('/')[-1]
                filename = av[counter] + "&" + filename
                counter += 1
                # time.sleep(0.3)
                print(count-i*5)
                try:
                    save(real, filename)
                except:
                    continue
                    # f1.write(repr(ll)+'\r\n')
        else:
            pass
        # x = driver.find_element_by_tag_name('body')
        # x.send_keys(Keys.COMMAND + 't')

    # driver.close()  # 关闭标签
    driver.quit()  # 退出浏览器
