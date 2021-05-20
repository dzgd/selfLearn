import requests
import random
import time
import json

count = 0
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': 'wExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; index_location_city=%E6%88%90%E9%83%BD; WEBTJ-ID=20210331%E4%B8%8A%E5%8D%881:10:38011038-178841da6381e0-09580f922d8d8a-53e3566-1049088-178841da63981c; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; __lg_stoken__=e94ed23975e1e3255d263dbe7ea080d3c791937bab07015ab8f2c56971538f1b5828e1f520a7d95caddf92abe295989d30fcdd373536ebf455460f5dfc7441e5285bc88465d0; LGSID=20210331030012-b7d7d2c8-90e7-4f9e-9747-5812e8ea8b1c; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.af0000j5UWmzd317vC-GZU2j-hK1ovo62UcgVDkVCydNoQWReACfdCTSZIn7Wln-YUacye%5FSmjVVDvSbjo3K8GLWEWo-8GbXCBNPgrWCjZ2qgJhc6MEXpL5ODyf9tIwGapfyOc3vsr0bsFq9s6Gsyzoa%5Fs4AD5MAhsVzvE7BcyMiKygeCFK%5Fe1mV3x3K6wNwFo2h2mU2%5FDFyTkRjlwnyS3U2eoWx.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4%5FtL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPSnx1do00ThPv5HD0IgF%5Fgv-b5HDdnWfLPj6snWT0UgNxpyfqnHfzPjfLrjn0UNqGujYknj64nj6vP6KVIZK%5Fgv-b5HDznWT10ZKvgv-b5H00pywW5R9awfKWThnqPj0YP1n%26ck%3D5337.4.171.357.162.230.157.452%26dt%3D1617130808%26wd%3D%25E6%258B%2589%25E9%2592%25A9%25E7%25BD%2591%26tpl%3Dtpl%5F12273%5F24677%5F20875%26l%3D1524748027%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1617124233,1617124598,1617130813,1617131911; _gat=1; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=ad91dc25b66a09e8010231716107a58e89a155760d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219751291%22%2C%22%24device_id%22%3A%22178841a81c816-007ede6e322b8e-53e3566-1049088-178841a81c9622%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2288.0.4324.150%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22178841a81c816-007ede6e322b8e-53e3566-1049088-178841a81c9622%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1617132011; LGRID=20210331032011-db230a0c-60b2-4176-803b-3c2c03e459cb; SEARCH_ID=93f61daaa4f249488c6e68a09e0a25cc',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=sug&fromSearch=true&suginput=shuju'
}
def get_message():
    for i in range(1, 3):
        print('第' + str(i) + '页')
        time.sleep(random.randint(10, 20))
        data = {
            'first': 'false',
            'pn': i,
            'kd': '数据挖掘'
        }
        response = requests.post(url=url, data=data, headers=headers)
        result = json.loads(response.text)
        print(result)
        job_messages = result['content']['positionResult']['result']
        # 职位详情页URL获取
        job_urls = result['content']['hrInfoMap'].keys()
        for k in job_urls:
            url_1 = 'https://www.lagou.com/jobs/' + k + '.html'
            print(url_1)
            with open('job_urls.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(url_1 + '\n')
        for job in job_messages:
            global count
            count += 1
            # 岗位名称
            job_title = job['positionName']
            print(job_title)
            # 岗位薪水
            job_salary = job['salary']
            print(job_salary)
            # 岗位地点
            job_city = job['city']
            print(job_city)
            # 岗位经验
            job_experience = job['workYear']
            print(job_experience)
            # 岗位学历
            job_education = job['education']
            print(job_education)
            # 公司名称
            company_name = job['companyShortName']
            print(company_name)
            # 公司类型
            company_type = job['industryField']
            print(company_type)
            # 公司状态
            company_status = job['financeStage']
            print(company_status)
            # 公司规模
            company_people = job['companySize']
            print(company_people)
            # 工作技能
            if len(job['positionLables']) > 0:
                job_tips = ','.join(job['positionLables'])
            else:
                job_tips = 'None'
            print(job_tips)
            # 工作福利
            job_welfare = job['positionAdvantage']
            print(job_welfare + '\n\n')

if __name__ == '__main__':
    get_message()
