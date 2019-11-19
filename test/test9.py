import requests
from urllib import parse
import requests

host = 'http://zcdj.wangtiantech.com'
user = {
    'loginName': 'admin',
    'password':'1'
}

s = requests.Session() # => 会话对象

# 登录
login_url = parse.urljoin(host, '/main')
lr = s.post(login_url, data=user)
#print(lr.text)

# 上传图片
upload_url = parse.urljoin(host,'http://zcdj.wangtiantech.com/upload/uploadFile?sourceID=')
# 构造图片数据，这里必须要填上图片相关参数
file = {
    'editormd-image-file': open(r'D:\download\cs.jpg', 'rb'),   # => 用name指定文件
    'Content-Disposition': 'form-data',
    'Content-Type': 'image/jpeg',
    'filename':'cs.jpg'
    }
ur = s.post(upload_url, files=file)  # => 注意这里，参数名是 files
print(ur.json())










