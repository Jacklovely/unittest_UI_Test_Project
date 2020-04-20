import re
import requests

def test_login_1():

    url = "http://49.235.92.12:9000/admin/login/"
    s = requests.session()
    r = s.get(url)
    #print(r.text)
    csrfmiddlewaretoken = re.findall("'csrfmiddlewaretoken' value='(.+?)'",r.text)
    #print (csrfmiddlewaretoken[0])
    body ={
        "csrfmiddlewaretoken":csrfmiddlewaretoken[0],
        "username":"admin",
        "password":"yoyo123456",
        "next":"/admin/"
    }
    r2 = s.post(url,data=body)
    print(r2.text)
    assert 'Welcome' in r2.text

if __name__ == '__main__':
    test_login_1()

