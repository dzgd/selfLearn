import requests
import pymysql
import random
import time
import json

count = 0
# 请求网址及请求头参数
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Cookie':'JSESSIONID=ABAAAECABIEACCAAFD6F394A8C9BD846C7E6B91C1CE50D7; sajssdk_2015_cross_new_user=1; user_trace_token=20210331010712-a25ef285-5c34-43d4-90e1-da001ec8d100; LGUID=20210331010712-7c278516-4501-4c06-8eeb-76a5f5fb3216; _ga=GA1.2.1271657354.1617124033; _gid=GA1.2.1416854182.1617124033; gate_login_token=9c37083ec15f4bdc12578d69265958edb8d190da75e11634aebd083ff2566056; _putrc=A6F438C039F6B0C8123F89F2B170EADC; login=true; unick=用户6385; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; LGSID=20210331011033-f147b4ac-3293-4f9e-bddd-6128607ce918; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https://www.baidu.com/other.php?sc.af0000aQpGALnsAHK4otZZja_lw7bFeZbktX5wDv1qtx3JTg4QAC34rNU55zl6ots26E0ikOzEbcQdZ5Lmxhf8H6SkmKEYJ5IfA8L0aN2_sdep5UHd7vX6lmxvy9rrbbsf8NoINX6nPjsn9s7SYKBJCC2Qe9m0kGCIorE7dCx9QG8zJmjR_wDXwrlwGs5avvUYvfPeUO9cXCBQodpqZCwp2eJXAT.7Y_NR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt_rE-9kYryqM764TTPqKi_nYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4VnL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPS0KzmLmqnfKdThkxpyfqnHRzPjTYrj0zPsKVINqGujYkPjcYPjT3nsKVgv-b5HDsrjbsrjmv0AdYTAkxpyfqnHczP1n0TZuxpyfqn0KGuAnqiDF70APzm1YYPWT3Ps&ck=2390.2.108.266.158.209.239.399&dt=1617124229&wd=%E6%8B%89%E5%8B%BE%E7%BD%91&tpl=tpl_12273_24677_20875&l=1524748027&us=linkName%3D%25E6%25A0%2587%25E9%25A2%2598-%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkText%3D%25E3%2580%2590%25E6%258B%2589%25E5%258B%25BE%25E6%258B%259B%25E8%2581%2598%25E3%2580%2591%25E5%25AE%2598%25E6%2596%25B9%25E7%25BD%2591%25E7%25AB%2599%2520-%2520%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591%25E9%25AB%2598%25E8%2596%25AA%25E5%25A5%25BD%25E5%25B7%25A5%25E4%25BD%259C%25EF%25BC%258C%25E4%25B8%258A%25E6%258B%2589%25E5%258B%25BE!%26linkType%3D; PRE_LAND=https://www.lagou.com/landing-page/pc/search.html?utm_source=m_cf_cpt_baidu_pcbt; index_location_city=成都; WEBTJ-ID=20210331上午1:10:38011038-178841da6381e0-09580f922d8d8a-53e3566-1049088-178841da63981c; RECOMMEND_TIP=true; sensorsdata2015session={}; __lg_stoken__=e94ed23975e1e3255d263dbe7ea080d3c791937bab07015ab8f2c56971538f1b5828e1f520a7d95caddf92abe295989d30fcdd373536ebf455460f5dfc7441e5285bc88465d0; TG-TRACK-CODE=search_code; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1617124033,1617124233,1617124598; _gat=1; X_HTTP_TOKEN=ad91dc25b66a09e8309421716107a58e89a155760d; sensorsdata2015jssdkcross={"distinct_id":"19751291","$device_id":"178841a81c816-007ede6e322b8e-53e3566-1049088-178841a81c9622","props":{"$latest_traffic_source_type":"直接流量","$latest_referrer":"","$latest_search_keyword":"未取到值_直接打开","$os":"Windows","$browser":"Chrome","$browser_version":"88.0.4324.150","lagou_company_id":""},"first_id":"178841a81c816-007ede6e322b8e-53e3566-1049088-178841a81c9622"}; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1617124904; LGRID=20210331012153-e3fcd5a5-b897-465b-87f3-33dbbee3d7be; SEARCH_ID=8ef632cd00064aec9254500cc1797f6f',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/p-city_0?px=default'
}

# 连接数据库
db = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='lagou_job', charset='utf8')


def add_Mysql(id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare):
    # 将数据写入数据库中
    try:
        cursor = db.cursor()
        sql = 'insert into job(id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare) values ("%d", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare)
        print(sql)
        cursor.execute(sql)
        print(cursor.lastrowid)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()



def get_message():
    for i in range(1, 2):
        print('第' + str(i) + '页')
        time.sleep(random.randint(10, 20))
        key = "数据分析"
        data = {
            'first': 'true',
            'pn': i,
            'kd': key
        }
        response = requests.post(url=url, data=data, headers=headers)
        result = json.loads(response.text)
        print(result)
        job_messages = result['content']['positionResult']['result']
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
            # 写入数据库
            add_Mysql(count, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare)


if __name__ == '__main__':
    get_message()