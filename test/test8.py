import requests
import unittest

class sampleTest(unittest.TestCase):

    def test_sample(self):
        r = requests.get("http://127.0.0.1:5000/")
        result = r.json()
        print(result)

class RESfulGetTest(unittest.TestCase):

    def test_sample(self):
        name = "tom"
        r = requests.get("http://127.0.0.1:5000/user/"+ name)
        result = r.json()
        print(result)
class GetUserDataTest(unittest.TestCase):

    def test_uid_null(self):
        uid = '2'
        r = requests.get('http://127.0.0.1:5000/id/'+uid)
        result = r.json()
        print(result)

    def test_uid_exist(self):
        uid = '1'
        r = requests.get('http://127.0.0.1:5000/id/'+uid)
        result = r.json()
        print(result)

class GetSampleTest(unittest.TestCase):

    def test_sample_1(self):
        payload = {'q':'selenium'}
        r = requests.get('http://127.0.0.1:5000/search/',params=payload)
        result = r.json()
        print(result)

    def test_sample_2(self):
        r = requests.get('http://127.0.0.1:5000/search/?q=selenium')
        result = r.json()
        print(result)

class PostSampleTest(unittest.TestCase):

    def test_sample_1(self):
        r = requests.post('http://127.0.0.1:5000/login')
        result = r.json()
        print(result)

    def test_sample_2(self):
        payload = {'username':'','password':''}
        r =requests.post('http://127.0.0.1:5000/login',data = payload)
        result = r.json()
        print(result)

    def test_sample_3(self):
        payload = {'username':'adm','password':'123'}
        r = requests.post('http://127.0.0.1:5000/login',data = payload)
        result = r.json()
        print(result)

    def test_sample_4(self):
        payload = {'username':'admin','password':'a123456'}
        r = requests.post('http://127.0.0.1:5000/login',data = payload)
        result = r.json()
        print(result)
class POSTjsonTest(unittest.TestCase):

    def test_key_null(self):
        payload = {}
        r = requests.post('http://127.0.0.1:5000/add_user',json=payload)
        result = r.json()
        print(result)

    def test_name_null(self):
        payload = {'name':'','age':22,'height':175}
        r = requests.post('http://127.0.0.1:5000/add_user',json=payload)
        result = r.json()
        print(result)

    def test_name_exist(self):
        payload = {'name':'tom','age':22,'height':175}
        r = requests.post('http://127.0.0.1:5000/add_user',json=payload)
        result = r.json()
        print(result)

    def test_add_exist(self):
        payload = {'name':'jack','age':22,'height':175}
        r = requests.post('http://127.0.0.1:5000/add_user',json=payload)
        result = r.json()
        print(result)

class HeadersTest(unittest.TestCase):

    def test_smaple(self):
        headers = {'Content-Type':'application/json',
                   'token':'d80caXELzU1aWmHwxl0TzW7jtterObm8l5EeAfipnhyaKmhFl8KdhFRvy4'}
        r = requests.post('http://127.0.0.1:5000/header',headers=headers)
        result = r.json()
        print(result)


if __name__ == '__main__':
    unittest.main()

