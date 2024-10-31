import requests
from bs4 import BeautifulSoup
import time
import os

def find_jobs():
    unwanted_field= input("Which field would you want to filter out? ")
    print(f'Filtering out {unwanted_field}')

    url = "https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Dubai&geoId=100205264&distance=25&f_TPR=r604800&position=1&pageNum=0"
    response = requests.get(url).text

    soup=BeautifulSoup(response,"lxml")
    jobs=soup.find_all("div",class_="base-search-card__info")
    job_links = [link.get("href") for link in soup.find_all("a", class_="base-card__full-link")]

    if not os.path.exists('Job_posts'):
        os.makedirs('Job_posts')

    # for index,job in enumerate(jobs):
    #     posted = job.time.text.strip()
    for index, (job, job_link) in enumerate(zip(jobs, job_links)):
        posted = job.find('time').text.strip()
        if "ago" in posted:
            job_title=job.h3.text.strip()
            company=job.h4.text.strip()
            if unwanted_field.upper() not in job_title.upper():
                with open (f'Job_posts/{index}.txt','w') as f:
                    f.write(f'\nCompany Name: {company}\n')
                    f.write(f'Job Title: {job_title} \n')
                    f.write(f'Posted: {posted}\n')
                    f.write(f'More_info: {job_link}')
                print(f"File saved {index}")

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)

#
# import requests
# from bs4 import BeautifulSoup
# import time
# import os
#
# def find_jobs():
#     unwanted_field = input("Which field would you want to filter out? ")
#     print(f'Filtering out {unwanted_field}')
#
#     url = "https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Dubai&geoId=100205264&distance=25&f_TPR=r604800&position=1&pageNum=0"
#     response = requests.get(url).text
#
#     soup = BeautifulSoup(response, "lxml")
#     jobs = soup.find_all("div", class_="base-search-card__info")
#     job_links = [link.get("href") for link in soup.find_all("a", class_="base-card__full-link")]
#
#     if not os.path.exists('Job_posts'):
#         os.makedirs('Job_posts')
#
#     for index, (job, job_link) in enumerate(zip(jobs, job_links)):
#         posted = job.find('time').text.strip()
#         job_title = job.h3.text.strip()
#         company = job.h4.text.strip()
#
#         print(f"Job {index}:")
#         print(f"Title: {job_title}")
#         print(f"Company: {company}")
#         print(f"Posted: {posted}")
#         print(f"Link: {job_link}")
#
#         if "ago" in posted and unwanted_field.upper() not in job_title.upper():
#             with open(f'Job_posts/{index}.txt', 'w') as f:
#                 f.write(f'Company Name: {company}\n')
#                 f.write(f'Job Title: {job_title}\n')
#                 f.write(f'Posted: {posted}\n')
#                 f.write(f'More_info: {job_link}\n')
#             print(f"File saved {index}")
#
# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait = 10
#         print(f'Waiting {time_wait} minutes...')
#         time.sleep(time_wait * 60)

# import requests
# from bs4 import BeautifulSoup
# import time
# import os
#
# def find_jobs():
#     unwanted_field = input("Which field would you want to filter out? ")
#     print(f'Filtering out {unwanted_field}')
#
#     url = "https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Dubai&geoId=100205264&distance=25&f_TPR=r604800&position=1&pageNum=0"
#     response = requests.get(url).text
#
#     soup = BeautifulSoup(response, "lxml")
#     jobs = soup.find_all("div", class_="base-search-card__info")
#     job_links = [link.get("href") for link in soup.find_all("a", class_="base-card__full-link")]
#
#     if not os.path.exists('Job_posts'):
#         os.makedirs('Job_posts')
#
#     for index, (job, job_link) in enumerate(zip(jobs, job_links)):
#         posted = job.find('time').text.strip()
#         job_title = job.h3.text.strip()
#         company = job.h4.text.strip()
#         location = job.find('span', class_='job-search-card__location').text.strip()
#
#         # Debugging output
#         print(f"Job {index}:")
#         print(f"Title: {job_title}")
#         print(f"Company: {company}")
#         print(f"Posted: {posted}")
#         print(f"Location: {location}")
#         print(f"Link: {job_link}")
#
#         if "ago" in posted and unwanted_field.upper() not in job_title.upper() and "Data Analyst" in job_title and "Dubai" in location:
#             with open(f'Job_posts/{index}.txt', 'w') as f:
#                 f.write(f'Company Name: {company}\n')
#                 f.write(f'Job Title: {job_title}\n')
#                 f.write(f'Posted: {posted}\n')
#                 f.write(f'Location: {location}\n')
#                 f.write(f'More_info: {job_link}\n')
#             print(f"File saved {index}")
#
# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait = 10
#         print(f'Waiting {time_wait} minutes...')
#         time.sleep(time_wait * 60)


# import requests
# from bs4 import BeautifulSoup
# import time
# import os
#
# def find_jobs():
#     unwanted_field = input("Which field would you want to filter out? ")
#     print(f'Filtering out {unwanted_field}')
#
#     url = "https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Dubai&geoId=100205264&distance=25&f_TPR=r604800&position=1&pageNum=0"
#     response = requests.get(url).text
#
#     soup = BeautifulSoup(response, "lxml")
#     jobs = soup.find_all("div", class_="base-search-card__info")
#     job_links = [link.get("href") for link in soup.find_all("a", class_="base-card__full-link")]
#
#     if not os.path.exists('Job_posts'):
#         os.makedirs('Job_posts')
#
#     for index, (job, job_link) in enumerate(zip(jobs, job_links)):
#         posted = job.find('time').text.strip()
#         job_title = job.h3.text.strip()
#         company = job.h4.text.strip()
#         location = job.find('span', class_='job-search-card__location').text.strip()
#
#         # Debugging output
#         print(f"Job {index}:")
#         print(f"Title: {job_title}")
#         print(f"Company: {company}")
#         print(f"Posted: {posted}")
#         print(f"Location: {location}")
#         print(f"Link: {job_link}")
#
#         if "ago" in posted and unwanted_field.upper() not in job_title.upper() and "Data Analyst" in job_title and "Dubai" in location:
#             with open(f'Job_posts/{index}.txt', 'w') as f:
#                 f.write(f'Company Name: {company}\n')
#                 f.write(f'Job Title: {job_title}\n')
#                 f.write(f'Posted: {posted}\n')
#                 f.write(f'Location: {location}\n')
#                 f.write(f'More_info: {job_link}\n')
#             print(f"File saved {index}")
#
# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait = 10
#         print(f'Waiting {time_wait} minutes...')
#         time.sleep(time_wait * 60)











# with open("My Courses.html", "r") as html_file:
#     content = html_file.read()
#
#     soup=BeautifulSoup(content, "lxml")
#     # print(soup.prettify())
#     # courses_html_tags=soup.find_all("h5")
#     # for course in courses_html_tags:
#     #     print(course)
#     course_cards=soup.find_all("div", class_="card")
#     # print(course_cards)

    # for course in course_cards:
    #     course_name=course.h5.text
    #     course_price=course.a.text.split()[-1]
    #     print(f'{course_name} costs {course_price}')