from bs4 import BeautifulSoup
import requests
import time

print('put some skills that you are not familiar with')
unfamiliar_skill= input('>')
print(f'filtering out:{unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        latest = job.find('span', class_='sim-posted').span.text

        if 'few' in latest:
            skills = job.find('ul', class_='list-job-dtl clearfix').text.replace(' ', '')
            job_description = job.a['href']
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'Company_name:{company_name.strip()} \n')
                    f.write(f'required_skills:{skills.strip()} \n')
                    f.write(f'job_description:{job_description} \n')
                print(f'file saved:{index}')


if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=1
        print(f'waiting {time_wait} minute.....')
        time.sleep(time_wait*30)