#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests, time, json, threading, random

class Presstest(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
    }

    # def __init__(self, login_url, press_url, phone="1376193000", password="123456"):
    #     self.login_url = login_url
    #     self.press_url = press_url
    #     self.phone = phone
    #     self.password = password
    #     self.session = requests.Session()
    #     self.session.headers = self.headers
    #
    # def login(self):
    #     '''登陆获取session'''
    #     data = data = {'t': int(time.time() * 1000), 'userName': self.phone, 'passWord': self.password}
    #     res = self.session.post(self.login_url, data=json.dumps(data))
    #     XToken = res.json().get('data').get('companyToken')
    #     self.session.headers['X-Token'] = XToken

    def testinterface(self):
        '''压测接口'''
        self.session.headers['X-UnionId'] = 'of6uw1CUVhP533sQok'
        data = {"id": int(''.join(str(random.choice(range(10))) for _ in range(10))),
                "openId": "oMr0c5LGJjlTc", "addressId": 10, "shipType": "SELF", "totalAmount": 5,
                "receivable": 5, "carts": [
                {"amount": 1, "barcode": "1234567890", "skuId": 1, "spec": "34", "itemAmount": 5, "price": 0,
                 "cover": "xxxx-dd.oss-cn-shanghai.aliyuncs.com/dfc91fd067ac464c096c90af33a196a5.png",
                 "name": "沙宣洗发水", "packingType": "瓶", "placeOfOrigin": "上海", "productId": "310153323435134976",
                 "retailPrice": 5, "suitableAge": "1-100"}], "formId": "the formId is a mock one", "comments": "aa"}
        global ERROR_NUM
        try:
            html = self.session.post(self.press_url, data=json.dumps(data))
            if html.json().get('code') != 0:
                print(html.json())
                ERROR_NUM += 1
        except Exception as e:
            print(e)
            ERROR_NUM += 1

    def testonework(self):
        '''一次并发处理单个任务'''
        i = 0
        while i < ONE_WORKER_NUM:
            i += 1
            self.work()
        time.sleep(LOOP_SLEEP)

    def run(self):
        '''使用多线程进程并发测试'''
        t1 = time.time()
        Threads = []

        for i in range(THREAD_NUM):
            t = threading.Thread(target=self.testonework, name="T" + str(i))
            t.setDaemon(True)
            Threads.append(t)

        for t in Threads:
            t.start()
        for t in Threads:
            t.join()
        t2 = time.time()

        print("===============压测结果===================")
        print("URL:", self.press_url)
        print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
        print("总耗时(秒):", t2 - t1)
        print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
        print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
        print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    login_url = 'https://ds.xxxxx.com/sys/sysUser/login'
    press_url = 'https://ds.xxxxx.com/weshop/order/checkout'
    phone = "1376193000"
    password = "123456"

    THREAD_NUM = 1  # 并发线程总数
    ONE_WORKER_NUM = 5  # 每个线程的循环次数
    LOOP_SLEEP = 0.1  # 每次请求时间间隔(秒)
    ERROR_NUM = 0  # 出错数

    obj = Presstest(login_url=login_url, press_url=press_url, phone=phone, password=password)
    obj.login()
    obj.run()