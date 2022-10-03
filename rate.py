from bs4  import BeautifulSoup
import requests



html_file = requests.get('https://monitordolarvenezuela.com/').text
soup = BeautifulSoup(html_file, 'lxml')

# Obtener div con valores de USD

with open ('dolar.txt', 'w') as f: 

    usd_h4 = soup.find('h4', class_= 'title-prome' , text= 'BCV (Oficial)' )
    usd_parent = usd_h4.parent
    rate  = usd_parent.find('p').text
    print(usd_h4.text)
    print(usd_parent)
    print(rate.split(' ')[-1])

    f.write(f"{usd_h4.text} \n")
    f.write(f"{rate.split(' ')[-1]} \n")
