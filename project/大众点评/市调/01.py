from fontTools.ttLib import TTFont
import requests
import re
from lxml import etree
import xlwings as xw
import urllib


zitiUrl = "http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/eefbade032229a6dee49f659442b8455.css"
# def get_ziti():   # 根据字体的url把字体文件保存到本地
#     res = requests.get(zitiUrl)
#     font = re.findall(r'font-family: "(.*?)";src.*?(//s3plus\.meituan\.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/\w+.woff)', res.text, re.S)
#     font_list = ['https:' + x[1] for x in font]
#     font_name = [x[0] for x in font]
#     for i in font_list:
#         result = requests.get(i)
#         file_name = "./" + i.split('/')[-1]
#         with open(file_name, 'wb')as f:
#             f.write(result.content)
#             print("sucess")
#
#
# def parse_ziti(self, class_name, datas):  # datas表示传进来的经过处理的列表
#     # 因为加密用了不同的文件，所以加个名称，便于区别
#     if class_name == 'shopNum':   # 评论数， 人均消费， 口味环境服务分数
#         woff_name = 'ebb40305.woff'
#     elif class_name == 'tagName':   # 店铺分类，哪个商圈
#         woff_name = '9b3f551f.woff'
#     else:
#         woff_name = '1d742900.woff'   # 店铺具体地址
#     # 评分
#     font_data = TTFont(woff_name)
#     font_data.saveXML(woff_name)   # 保存xml便于做分析
#
# if __name__ == '__main__':
#     get_ziti()



start_url = 'http://www.dianping.com/search/keyword/17/0_%E5%92%96%E5%95%A1/p{}'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'fspop=test; cy=17; cye=xian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=177f7dba95dc8-005f474e0eb037-53e3566-100200-177f7dba95ec8; _lxsdk=177f7dba95dc8-005f474e0eb037-53e3566-100200-177f7dba95ec8; _hc.v=98fb828e-2923-5403-dc18-0b0e144f7db4.1614771104; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1614771105; s_ViewType=10; _dp.ac.v=cca643d9-5f63-4a66-811f-92ab60dcb21c; dplet=97098a89ebf6466d96eea05cb131b225; dper=52e1a0a2e55dde5b796e809e72c66e35dbe127e80793e4680bf02ed99015e09f0e2d5bd2da1aad516cd0b310810bf5cdb081c6f4a5e5198d83c911c16754b31f0b4c71a6252db2d00367e325ece2a87197187eaaed39aede563b2de3e352c7ff; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_9504504425; ctu=08eebc56af2eedae670f76f101f34391f2f07a494b517bfda8c82c3878192dfc; uamo=17828896385; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1614773388; _lxsdk_s=177f7dba95f-cf7-81b-80d%7C%7C446',
    'Host': 'www.dianping.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
class DaZhong(object):
    def get_ziti(self):   # 根据字体的url把字体文件保存到本地
        res = requests.get(zitiUrl)
        font = re.findall(r'font-family: "(.*?)";src.*?(//s3plus\.meituan\.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/\w+.woff)', res.text, re.S)
        font_list = ['https:' + x[1] for x in font]
        font_name = [x[0] for x in font]
        for i in font_list:
            result = requests.get(i)
            file_name = "./" + i.split('/')[-1]
            with open(file_name, 'wb')as f:
                f.write(result.content)
                print("sucess")

    def parse_ziti(self, class_name, datas):

        if class_name == 'shopNum':   # 评论数， 人均消费， 口味环境服务分数
            woff_name = 'ebb40305.woff'
        elif class_name == 'tagName':   # 店铺分类，哪个商圈
            woff_name = '9b3f551f.woff'
        else:
            woff_name = '1d742900.woff'   # 店铺具体地址
        # 评分
        font_data = TTFont(woff_name)
        words = ['1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '0', '店', '中', '美', '家', '馆', '小', '车', '大',
                 '市', '公', '酒', '行', '国', '品', '发', '电', '金', '心',
                 '业', '商', '司', '超', '生', '装', '园', '场', '食', '有',
                 '新', '限', '天', '面', '工', '服', '海', '华', '水', '房',
                 '饰', '城', '乐', '汽', '香', '部', '利', '子', '老', '艺',
                 '花', '专', '东', '肉', '菜', '学', '福', '饭', '人', '百',
                 '餐', '茶', '务', '通', '味', '所', '山', '区', '门', '药',
                 '银', '农', '龙', '停', '尚', '安', '广', '鑫', '一', '容',
                 '动', '南', '具', '源', '兴', '鲜', '记', '时', '机', '烤',
                 '文', '康', '信', '果', '阳', '理', '锅', '宝', '达', '地',
                 '儿', '衣', '特', '产', '西', '批', '坊', '州', '牛', '佳',
                 '化', '五', '米', '修', '爱', '北', '养', '卖', '建', '材',
                 '三', '会', '鸡', '室', '红', '站', '德', '王', '光', '名',
                 '丽', '油', '院', '堂', '烧', '江', '社', '合', '星', '货',
                 '型', '村', '自', '科', '快', '便', '日', '民', '营', '和',
                 '活', '童', '明', '器', '烟', '育', '宾', '精', '屋', '经',
                 '居', '庄', '石', '顺', '林', '尔', '县', '手', '厅', '销',
                 '用', '好', '客', '火', '雅', '盛', '体', '旅', '之', '鞋',
                 '辣', '作', '粉', '包', '楼', '校', '鱼', '平', '彩', '上',
                 '吧', '保', '永', '万', '物', '教', '吃', '设', '医', '正',
                 '造', '丰', '健', '点', '汤', '网', '庆', '技', '斯', '洗',
                 '料', '配', '汇', '木', '缘', '加', '麻', '联', '卫', '川',
                 '泰', '色', '世', '方', '寓', '风', '幼', '羊', '烫', '来',
                 '高', '厂', '兰', '阿', '贝', '皮', '全', '女', '拉', '成',
                 '云', '维', '贸', '道', '术', '运', '都', '口', '博', '河',
                 '瑞', '宏', '京', '际', '路', '祥', '青', '镇', '厨', '培',
                 '力', '惠', '连', '马', '鸿', '钢', '训', '影', '甲', '助',
                 '窗', '布', '富', '牌', '头', '四', '多', '妆', '吉', '苑',
                 '沙', '恒', '隆', '春', '干', '饼', '氏', '里', '二', '管',
                 '诚', '制', '售', '嘉', '长', '轩', '杂', '副', '清', '计',
                 '黄', '讯', '太', '鸭', '号', '街', '交', '与', '叉', '附',
                 '近', '层', '旁', '对', '巷', '栋', '环', '省', '桥', '湖',
                 '段', '乡', '厦', '府', '铺', '内', '侧', '元', '购', '前',
                 '幢', '滨', '处', '向', '座', '下', '県', '凤', '港', '开',
                 '关', '景', '泉', '塘', '放', '昌', '线', '湾', '政', '步',
                 '宁', '解', '白', '田', '町', '溪', '十', '八', '古', '双',
                 '胜', '本', '单', '同', '九', '迎', '第', '台', '玉', '锦',
                 '底', '后', '七', '斜', '期', '武', '岭', '松', '角', '纪',
                 '朝', '峰', '六', '振', '珠', '局', '岗', '洲', '横', '边',
                 '济', '井', '办', '汉', '代', '临', '弄', '团', '外', '塔',
                 '杨', '铁', '浦', '字', '年', '岛', '陵', '原', '梅', '进',
                 '荣', '友', '虹', '央', '桂', '沿', '事', '津', '凯', '莲',
                 '丁', '秀', '柳', '集', '紫', '旗', '张', '谷', '的', '是',
                 '不', '了', '很', '还', '个', '也', '这', '我', '就', '在',
                 '以', '可', '到', '错', '没', '去', '过', '感', '次', '要',
                 '比', '觉', '看', '得', '说', '常', '真', '们', '但', '最',
                 '喜', '哈', '么', '别', '位', '能', '较', '境', '非', '为',
                 '欢', '然', '他', '挺', '着', '价', '那', '意', '种', '想',
                 '出', '员', '两', '推', '做', '排', '实', '分', '间', '甜',
                 '度', '起', '满', '给', '热', '完', '格', '荐', '喝', '等',
                 '其', '再', '几', '只', '现', '朋', '候', '样', '直', '而',
                 '买', '于', '般', '豆', '量', '选', '奶', '打', '每', '评',
                 '少', '算', '又', '因', '情', '找', '些', '份', '置', '适',
                 '什', '蛋', '师', '气', '你', '姐', '棒', '试', '总', '定',
                 '啊', '足', '级', '整', '带', '虾', '如', '态', '且', '尝',
                 '主', '话', '强', '当', '更', '板', '知', '己', '无', '酸',
                 '让', '入', '啦', '式', '笑', '赞', '片', '酱', '差', '像',
                 '提', '队', '走', '嫩', '才', '刚', '午', '接', '重', '串',
                 '回', '晚', '微', '周', '值', '费', '性', '桌', '拍', '跟',
                 '块', '调', '糕'
                 ]
        gly_list = font_data.getGlyphOrder()[2:]
        # print(gly_list)  # ['unie8a0', 'unie910', 'unif6a4', 'unif3d3', 'unie2f4', 'unie7a6', 'uniea32', 'unif0f9', 'unie2ac']
        new_dict = {}
        for index, value in enumerate(words):
            new_dict[gly_list[index]] = value
        print(new_dict)
        rel = ''
        for j in datas:
            if j.startswith('u'):
                rel += new_dict[j]
            else:
                rel += j
        return rel


    def get_page_info(self):  # 获取网页上需要的数据
        key_word = input('请输入需要搜索的关键字：')
        response = requests.get(start_url.format(urllib.parse.quote(key_word)), headers=headers)
        print(response.status_code)
        with open('dazhong.html', 'w', encoding='utf-8')as f:   # 这里我把html保存到本地方便使用，不然超级容易被封ip
           f.write(response.text)
    #     with open('dazhong.html', 'r', encoding='utf-8') as f:
    #         html_ = f.read()
    #     html_ = re.sub(r"&#x(\w+?);", r"*\1", html_)   # 网页源码每个数字对应的内容，保留括号里的内容，把括号前面的内容替换为*
    #     html = etree.HTML(html_)
    #     # 所有数据的标签
    #     all_info = []
    #     li_list = html.xpath("//div[@class='content']/div/ul/li")
    #     for li in li_list:
    #         item = {}
    #         item['店铺名'] = li.xpath('./div[2]/div/a/h4/text()')[0]
    #         item['推荐菜'] = li.xpath('./div[2]/div[4]/a//text()')
    #         if item['推荐菜'] is not None:
    #             item['推荐菜'] = ','.join(li.xpath('./div[2]/div[4]/a//text()'))
    #         else:
    #             item['推荐菜'] = ''
    #         # 标签名称
    #         class_name = li.xpath("./div[2]/div[2]/a[1]/b/svgmtsi/@class")[0]
    #         tag_name = li.xpath('./div[2]/div[3]/a[2]/span/svgmtsi/@class')[0]
    #         addr_name = li.xpath('./div[2]/div[3]/span/svgmtsi/@class')[0]
    #         comment_num = li.xpath("./div[2]/div[2]/a[1]/b//text()")   # 拿评论的数据['1', '*e2ac', '*f0f9', '*e2ac', '*e8a0']
    #         # 遍历列表，把*号开头的去掉，并与uni拼接成新的，如果是1，则放在列表里，得到新的列表 ['1', 'unie2ac', 'unif0f9', 'unie2ac', 'unie8a0']
    #         comment_num_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in comment_num]
    #         item['评价数'] = self.parse_ziti(class_name, comment_num_list)
    #
    #         avg_price = li.xpath("./div[2]/div[2]/a[2]/b//text()")   # 人均消费
    #         avg_price_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in avg_price]
    #         item['人均'] = self.parse_ziti(class_name, avg_price_list)
    #
    #         shop_area = li.xpath('./div[2]/div[3]/a[2]/span//text()')   # 商圈
    #         shop_area_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in shop_area]
    #         item['商圈'] = self.parse_ziti(tag_name, shop_area_list)
    #
    #         shop_type = li.xpath('./div[2]/div[3]/a[1]/span//text()')  # 商铺类型
    #         shop_type_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in shop_type]
    #         item['分类'] = self.parse_ziti(tag_name, shop_type_list)
    #
    #         shop_address = li.xpath('./div[2]/div[3]/span//text()')   # 具体地址
    #         shop_address_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in shop_address]
    #         item['地址'] = self.parse_ziti(addr_name, shop_address_list)
    #
    #         # comment_kouwei = li.xpath("./div[2]/span/span[1]/b//text()")  # 口味评分
    #         # if comment_kouwei:
    #         #     comment_kouwei_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in comment_kouwei]
    #         #     item['口味'] = self.parse_ziti(class_name, comment_kouwei_list)
    #         # else:
    #         #     item['口味'] = ''
    #         #
    #         # comment_huanjing = li.xpath("./div[2]/span/span[2]/b//text()")  # 环境评分
    #         # if comment_huanjing:
    #         #     comment_huanjing_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in comment_huanjing]
    #         #     item['环境'] = self.parse_ziti(class_name, comment_huanjing_list)
    #         # else:
    #         #     item['环境'] = ''
    #         #
    #         # comment_service = li.xpath("./div[2]/span/span[3]/b//text()")  # 服务评分
    #         # if comment_service:
    #         #     comment_service_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in comment_service]
    #         #     item['服务'] = self.parse_ziti(class_name, comment_service_list)
    #         # else:
    #         #     item['服务'] = ''
    #
    #         zh_comment = li.xpath("./div[2]/span/span//text()")
    #         zh_comment_list = ['uni' + i.strip('*') if i.startswith('*') else i for i in zh_comment]
    #         item['综合评分'] = self.parse_ziti(class_name, zh_comment_list)
    #
    #         # self.save_to_csv(item)
    #         all_info.append(item)
    #     self.save_to_excel(all_info)
    #
    # # def save_to_csv(self, item):
    # #     headline = ['店铺名\t', '推荐菜\t', '分类\t', '评价数\t', '人均\t', '口味\t', '环境\t', '服务\t', '商圈\t', '地址\t']
    # #     # for i in range(len(item)):
    # #     if not os.path.exists('dazhong.csv'):
    # #         with open('dazhong.csv', 'a', newline='', encoding='utf-8')as f:
    # #             f.writelines(headline)
    # #             f.writelines('\n')
    # #             f.writelines(item.values())
    # #     else:
    # #         with open('dazhong.csv', 'a', newline='', encoding='utf-8')as f:
    # #             f.writelines(item.values())
    # #             f.writelines('\n')
    #
    #
    # def save_to_excel(self, items):
    #     app = xw.App(visible=True, add_book=False)
    #     wb = app.books.add()
    #     sht = wb.sheets['sheet1']
    #     sht.range('a1').value = list(items[0].keys())
    #     for i in range(0, 3):
    #         # 列表数据要放在循环里 格式是 [{}]
    #         value_list = list(items[i].values())
    #         sht.range('A{}'.format(i + 2)).value = value_list
    #     wb.save('dzdp.xlsx')



if __name__ == '__main__':
    dz = DaZhong()
    # dz.get_ziti()
    dz.get_page_info()
    # dz.parse_ziti()
