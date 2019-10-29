#coding=utf8
import requests
import os
def load():
    url="https://img.52fuqing.com/upload/editor/2019-08-14/1565785624zUz95x.jpg"
    d='D:\\download\\'
    path=d+url.split('/')[-1]
    try:
        if not os.path.exists(d):
            os.mkdir(d)
        if not os.path.exists(path):
            r=requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("图片保存成功")
        else:
            print("图片已存在")
    except:
        print("图片获取失败")

if __name__ == '__main__':
    load()