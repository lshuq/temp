import time
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request


# 获取微信公众号新闻

def get_access():
    return webdriver.Firefox()


def search_page(driver, url):
    driver.get(url)
    print(driver.current_url)
    elem = driver.find_element_by_class_name("query")
    elem.send_keys(u"国际农业航空施药技术联合实验室")
    btn = driver.find_element_by_class_name("swz2")
    btn.click()
    print(driver.current_url)
    time.sleep(1)
    page = driver.page_source
    return page


def load_page(driver, url):
    driver.get(url)
    page = driver.page_source
    return page


def next_page(page):
    soup = BeautifulSoup(page, "html5lib")
    link = soup.find('div', attrs={"class": "img-box"})
    link_to = link.find('a')
    return link_to.attrs['href']


def get_news_urls(page):
    base_url = 'https://mp.weixin.qq.com'
    # 存储新闻页面的列表
    news_urls = {}
    soup = BeautifulSoup(page, "html5lib")
    # 新闻列表
    news_list = soup.find_all('h4', attrs={'class': 'weui_media_title'})
    # 全部新闻标题
    for i in news_list:
        news_title = i.get_text()
        news_url = base_url + i.attrs['hrefs']
        news_urls[news_title] = news_url
    return news_urls


def get_news(news_urls):
    for url in news_urls:
        print(url, news_urls[url])


def initial():
    html_url = "http://weixin.sogou.com/"
    web_look = get_access()
    html_url = search_page(web_look, html_url)
    true_url = next_page(html_url)
    news_urls = get_news_urls(load_page(web_look, true_url))
    get_news(news_urls)


if __name__ == '__main__':
    initial()
