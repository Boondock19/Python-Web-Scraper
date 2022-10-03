from bs4 import BeautifulSoup
import requests
import time

print("Enter some skill you are unfamiliar with")
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        job_date = job.find('span', class_='sim-posted').span.text
        if 'few' in job_date:
            job_company = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '')
            job_skill = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            if unfamiliar_skills not in job_skill:
                job_url = job.header.h2.a['href']
                with open(f'infoFiles/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {job_company.strip()} \n")
                    f.write(f"Required Skills: {job_skill.strip()} \n")
                    f.write(f"More Info: {job_url.strip()}")
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)