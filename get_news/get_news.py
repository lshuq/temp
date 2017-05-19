from bs4 import BeautifulSoup
import requests
import urllib.request


def load_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    data = requests.get(url, headers=headers).content
    # data = urllib.request.Request(url, headers=headers)
    # data = urllib.request.urlopen(data)
    return data


def get_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find('div', attrs={'class': 'weui_msg_card_list'})
    print(news)


if __name__ == '__main__':
    url = 'http://mp.weixin.qq.com/profile?src=3&timestamp=' \
          '1495160677&ver=1&signature=G1YyQEWwIaHri-SgpEXkC' \
          'u2vzaeC3fYVPZtgDvwd408MdPkj6CV0YlLPKtJS3*A6h5-QPZ4Bzomqb72RUJ01kw=='
    html = load_page(url)
    get_text(html)
