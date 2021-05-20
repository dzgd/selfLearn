import datetime
import random
import time
import re
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
from pyquery import PyQuery as pq

# client = pymongo.MongoClient('localhost', 27017)
# shidai = client['mydu']
# comments = shidai['comments']


COOKIES = 'fspop=test; cy=17; cye=xian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=177fb9256efc8-036b54f9b4310b-5771e33-144000-177fb9256efc8; _lxsdk=177fb9256efc8-036b54f9b4310b-5771e33-144000-177fb9256efc8; _hc.v=fdd445f3-2a76-e2b9-aff7-5e5c44fdfae3.1614833408; s_ViewType=10; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1614833408,1614848174; lgtoken=05fd8b101-bea5-4a38-9833-976efe2301aa; dplet=5b7f6547b217651981bf169e088c6969; dper=52e1a0a2e55dde5b796e809e72c66e35c323c044e93fe2988d5cec07762b1d54a29dc970c34ca76fbfb168f23175b4eb57486572a552c9b06e5990f166b71006eb8c2af5030d1d2cb50abd949c184f0b3f68260fdd01ea35bd080c133088259f; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_9504504425; ctu=08eebc56af2eedae670f76f101f343917016bec9ca0fc0fda6cc9d7303cd7514; uamo=17828896385; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1614848273; _lxsdk_s=177fc73a140-c0c-ac5-a2c%7C%7C175'
f = open('./大众点评.txt', 'w', encoding='utf-8')


class DianpingComment(object):
    font_size = 14
    start_y = 23

    def __init__(self, shop_id, cookies, delay=7, handle_ban=True):  # comments=comments
        self.shop_id = shop_id
        self._delay = delay
        self.num = 1
        self._cookies = self._format_cookies(cookies)
        self._css_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        self._default_headers = {
            'Connection': 'keep-alive',
            'Host': 'www.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Cookie': 'fspop=test; cy=17; cye=xian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=177fb9256efc8-036b54f9b4310b-5771e33-144000-177fb9256efc8; _lxsdk=177fb9256efc8-036b54f9b4310b-5771e33-144000-177fb9256efc8; _hc.v=fdd445f3-2a76-e2b9-aff7-5e5c44fdfae3.1614833408; s_ViewType=10; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1614833408,1614848174; lgtoken=05fd8b101-bea5-4a38-9833-976efe2301aa; dplet=5b7f6547b217651981bf169e088c6969; dper=52e1a0a2e55dde5b796e809e72c66e35c323c044e93fe2988d5cec07762b1d54a29dc970c34ca76fbfb168f23175b4eb57486572a552c9b06e5990f166b71006eb8c2af5030d1d2cb50abd949c184f0b3f68260fdd01ea35bd080c133088259f; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_9504504425; ctu=08eebc56af2eedae670f76f101f343917016bec9ca0fc0fda6cc9d7303cd7514; uamo=17828896385; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1614848273; _lxsdk_s=177fc73a140-c0c-ac5-a2c%7C%7C175'}
        self._cur_request_url = 'http://www.dianping.com/shop/{}/review_all'.format(self.shop_id)
        self.sub_url = 'http://www.dianping.com'

    def run(self):
        self._css_link = self._get_css_link(self._cur_request_url)
        self._font_dict = self._get_font_dict(self._css_link)
        self._get_conment_page()

    def _delay_func(self):
        delay_time = random.randint((self._delay - 2) * 10, (self._delay + 2) * 10) * 0.1
        time.sleep(delay_time)

    def _init_browser(self):
        """
            初始化游览器
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(self._cur_request_url)
        for name, value in self._cookies.items():
            browser.add_cookie({'name': name, 'value': value})
        browser.refresh()
        return browser

    def _handle_ban(self):
        """
            爬取速度过快，出现异常时处理验证
        """
        try:
            self._browser.refresh()
            time.sleep(1)
            button = self._browser.find_element_by_id('yodaBox')
            move_x_offset = self._browser.find_element_by_id('yodaBoxWrapper').size['width']
            webdriver.ActionChains(self._browser).drag_and_drop_by_offset(
                button, move_x_offset, 0).perform()
        except:
            pass

    def _format_cookies(self, cookies):
        '''
        获取cookies;;;
        :param cookies:
        :return:
        '''
        cookies = {cookie.split('=')[0]: cookie.split('=')[1]
                   for cookie in cookies.replace(' ', '').split(';')}
        return cookies

    def _get_conment_page(self):
        """
            请求评论页，并将<span></span>样式替换成文字;
        """
        while self._cur_request_url:
            self._delay_func()
            print('[{now_time}] {msg}'.format(now_time=datetime.datetime.now(), msg=self._cur_request_url))
            res = requests.get(self._cur_request_url, headers=self._default_headers, cookies=self._cookies)
            while res.status_code != 200:
                cookie = random.choice(COOKIES)
                cookies = self._format_cookies(cookie)
                res = requests.get(self._cur_request_url, headers=self._default_headers, cookies=cookies)
                if res.status_code == 200:
                    break
            html = res.text
            class_set = []
            for span in re.findall(r'<svgmtsi class="([a-zA-Z0-9]{5,6})"></svgmtsi>', html):
                class_set.append(span)
            for class_name in class_set:
                try:
                    html = re.sub('<svgmtsi class="%s"></svgmtsi>' % class_name, self._font_dict[class_name], html)
                    print('{}已替换完毕_______________________________'.format(self._font_dict[class_name]))
                except:
                    html = re.sub('<svgmtsi class="%s"></svgmtsi>' % class_name, '', html)
                    print('替换失败…………………………………………………………………………&&&&&&&&&&&&&&&&&&&&&&&&')
            doc = pq(html)
            self._parse_comment_page(html)
            if doc('.NextPage').attr('href'):
                self._default_headers['Referer'] = self._cur_request_url
                next_page_url1 = doc('.NextPage').attr('href')
                next_page_url = self.sub_url + str(next_page_url1)
                print('next_url:{}'.format(next_page_url))
            else:
                next_page_url = None
            print('next_page_url:{}'.format(next_page_url))
            self._cur_request_url = next_page_url

    def _data_pipeline(self, data):
        """
            处理数据
        """
        print(data)

    def _parse_comment_page(self, html):
        """
            解析评论页并提取数据,把数据写入文件中；；
        """
        doc = pq(html)
        for li in doc('div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li'):

            doc_text = pq(li)
            if doc_text('.dper-info .name').text():
                name = doc_text('.dper-info .name').text()
            else:
                name = None
            try:
                star = doc_text('.review-rank .sml-rank-stars').attr('class')

            except IndexError:
                star = None
            if doc_text('div.misc-info.clearfix > .time').text():
                date_time = doc_text('div.misc-info.clearfix > .time').text()
            else:
                date_time = None
            if doc_text('.main-review .review-words').text():
                comment = doc_text('.main-review .review-words').text()
                print(comment)
            else:
                comment = None

            data = {
                'name': name,
                'date_time': date_time,
                'star': star,
                'comment': comment
            }
            print(data)
            f.write(str(data).encode('utf-8'))
            print('写入数据完成', data)

    def _get_css_link(self, url):
        """
            请求评论首页，获取css样式文件
        """
        try:
            print(url)
            res = requests.get(url, headers=self._default_headers, cookies=self._cookies)
            html = res.text
            css_link = re.search(r'<link re.*?css.*?href="(.*?svgtextcss.*?)">', html)
            print(css_link)
            assert css_link
            css_link = 'http:' + css_link[1]
            return css_link
        except:
            None

    def _get_font_dict(self, url):
        """
            获取css样式对应文字的字典
        """
        res = requests.get(url, headers=self._css_headers)
        html = res.text

        background_image_link = re.findall(r'background-image:.*?\((.*?svg)\)', html)
        print(background_image_link)
        background_image_link_list = []
        for i in background_image_link:
            url = 'http:' + i
            background_image_link_list.append(url)

        print(background_image_link_list)

        html = re.sub(r'span.*?\}', '', html)
        group_offset_list = re.findall(r'\.([a-zA-Z0-9]{5,6}).*?round:(.*?)px (.*?)px;', html)
        '''
        多个偏移字典，合并在一起；；；
        '''
        font_dict_by_offset_list = {}
        for i in background_image_link_list:
            font_dict_by_offset_list.update(self._get_font_dict_by_offset(i))

        font_dict_by_offset = font_dict_by_offset_list
        print(font_dict_by_offset)
        font_dict = {}
        for class_name, x_offset, y_offset in group_offset_list:
            x_offset = x_offset.replace('.0', '')
            y_offset = y_offset.replace('.0', '')
            try:
                font_dict[class_name] = font_dict_by_offset[int(y_offset)][int(x_offset)]

            except:
                font_dict[class_name] = ''
        return font_dict

    def _get_font_dict_by_offset(self, url):
        """
            获取坐标偏移的文字字典, 会有最少两种形式的svg文件（目前只遇到两种）
        """
        res = requests.get(url, headers=self._css_headers)
        html = res.text
        font_dict = {}
        y_list = re.findall(r'd="M0 (\d+?) ', html)
        if y_list:
            font_list = re.findall(r'<textPath .*?>(.*?)<', html)
            for i, string in enumerate(font_list):
                y_offset = self.start_y - int(y_list[i])

                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
        else:
            font_list = re.findall(r'<text.*?y="(.*?)">(.*?)<', html)
            for y, string in font_list:
                y_offset = self.start_y - int(y)
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
        return font_dict


class Customer(DianpingComment):
    def _data_pipeline(self, data):
        print(data)


if __name__ == "__main__":
    dianping = Customer('l7dKOYLSvg2ouBvr', cookies=COOKIES)
    dianping.run()
    f.close()
