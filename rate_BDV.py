from bs4  import BeautifulSoup
import requests
import time
import json
from timeloop import Timeloop
from datetime import timedelta


tl = Timeloop()

html_file = requests.get('https://www.bcv.org.ve/', verify=False).text
soup = BeautifulSoup(html_file, 'lxml')
url = 'https://gcfprojectusuario-default-rtdb.firebaseio.com/projects/proj_k69a1pcZoyHutm7c9DDdx4/data/QA/QA/TasaDolar/0.json'

# Obtener div con valores de USD
@tl.job(interval=timedelta(seconds=30))
def get_rate():
    with open ('dolar_BCV.txt', 'w') as f: 
        usd_span = soup.find('span', text=' USD')
        usd_parent = usd_span.parent
        usd_grandparent = usd_parent.parent
        rate_div = usd_grandparent.div.next_sibling.next_sibling
        rate = rate_div.strong.text.strip().replace(',', '.')

        f.write(f"{'Tasa BCV'} \n")
        f.write(f"{rate}\n")

        print("rate " + rate)
        body = {
            "Valor": float(rate)
        }

        requests.patch(url, json.dumps(body))

        print(requests.get(url).json())

# if __name__ == '__main__':
#     get_rate()
#     time_wait = 1
#     print(f'Waiting {time_wait} minutes...')
#     time.sleep(time_wait * 60)

if __name__ == "__main__":
    tl.start(block=True)