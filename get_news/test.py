from bs4 import BeautifulSoup
import requests


def load_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    data = requests.get(url, headers=headers).content
    return data


def get_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 定位文章
    article = soup.find('div', attrs={'class': 'article'})
    # 获取标题
    title = article.find('h1', attrs={'class': 'title'}).get_text()
    print(title)
    # 定义存放文章的列表
    text = []
    for para in article.find_all('p'):
        p_content = para.get_text()
        text.append(p_content)
        print(p_content)
    return title, text


if __name__ == '__main__':
    url = 'http://www.jianshu.com/p/96fbc2afca13'
    html = load_page(url)
    get_text(html)
