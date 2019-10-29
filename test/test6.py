#coding=utf8
import time
import requests
from multiprocessing import Process
from multiprocessing import Pool

data = {
    "times": 10, # 并发量
    "method": "POST",
    "url": "http://47.98.52.20:8080/farmfriend/login/main.do",
    "header": {
        "Content-Type": "application/json",
        "user-agent": "python-mock/0.0.1"
    },
    "body": {
        # 参数
    }
}

def run_task(idx):
    response = requests.post(data["url"], json=data["body"], headers=data["header"])
    if response.status_code == 200:
        result = response.content.decode('utf-8')
    else:
        result = "访问失败"
    print("第 %s 次执行：%s \n" % (idx, result))

if __name__ == '__main__':
    p = Pool(data["times"])
    for index in range(data["times"]):
        p.apply_async(run_task, args=(index + 1,))

    p.close()
    p.join()
    print("执行结束.")