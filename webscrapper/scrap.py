# import os
# import requests
# from bs4 import BeautifulSoup
# import csv
# import io
# from pathlib import Path
#
# # Install the ghananews-scraper package
# # !pip install ghananews-scraper
#
# # Scrape data from GhanaWeb
# from ghanaweb.scraper import GhanaWeb
#
# urls = [
#     "https://www.ghanaweb.com/GhanaHomePage/NewsArchive/",
#     "https://www.ghanaweb.com/GhanaHomePage/business/",
#     "https://www.ghanaweb.com/GhanaHomePage/SportsArchive/",
#     "https://www.ghanaweb.com/GhanaHomePage/entertainment/",
#
#
# ]
#
# for url in urls:
#     print(f"Downloading: {url}")
#     web = GhanaWeb(url=url)
#     web.download(output_dir=None)
#
# # Scrape data from MyJoyOnline
# from myjoyonline.scraper import MyJoyOnlineNews
#
# urls = [
#     'https://myjoyonline.com/news',
#     'https://myjoyonline.com/politics',
#     'https://myjoyonline.com/entertainment',
#     'https://myjoyonline.com/business',
#     'https://myjoyonline.com/sports',
#     'https://myjoyonline.com/opinion',
#     'https://myjoyonline.com/technology'
# ]
#
# for url in urls:
#     print(f"Downloading data from: {url}")
#     joy = MyJoyOnlineNews(url=url)
#     joy.download()
#
# # Scrape data from CitiBusinessOnline
# from citionline.scraper import CitiBusinessOnline
#
# urls = [
#     "https://citibusinessnews.com/ghanabusinessnews/features/",
#     "https://citibusinessnews.com/ghanabusinessnews/telecoms-technology/",
#     "https://citibusinessnews.com/ghanabusinessnews/international/",
#     "https://citibusinessnews.com/ghanabusinessnews/news/government/",
#     "https://citibusinessnews.com/ghanabusinessnews/news/",
#     "https://citibusinessnews.com/ghanabusinessnews/business/",
#     "https://citibusinessnews.com/ghanabusinessnews/news/economy/",
#     "https://citibusinessnews.com/ghanabusinessnews/news/general/",
#     "https://citibusinessnews.com/ghanabusinessnews/news/top-stories/",
#     "https://citibusinessnews.com/ghanabusinessnews/business/tourism/"
# ]
#
# for url in urls:
#     print(f"Downloading data from: {url}")
#     citi = CitiBusinessOnline(url=url)
#     citi.download()
#
# # Scrape data from GraphicOnline
# from graphiconline.scraper import GraphicOnline
#
# urls = [
#     "https://www.graphic.com.gh/news/business.html",
#     "https://www.graphic.com.gh/news/sports.html",
#     "https://www.graphic.com.gh/news/entertainment.html",
#     "https://www.graphic.com.gh/news/lifestyle.html"
# ]
#
# for url in urls:
#     print(f"Downloading data from: {url}")
#     graphic = GraphicOnline(url=url)
#     graphic.download()
#
# # Convert dataset to CSV file
# with open('ghana_news.csv', 'w', newline='') as csvfile:
#     fieldnames = ['headline', 'link', 'summary', 'image_url']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for article in articles:
#         writer.writerow(article)


import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# Load the CSV file containing the links
links_df = pd.read_csv('Link 1.csv')

# Create a list to store the scraped data
scraped_data = []

# Loop through each link in the CSV file
for index, row in links_df.iterrows():
    link = row['published_page_url']
    print(f"Scraping data from {link}...")

    # Send a GET request to the link
    response = requests.get(link)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the relevant data from the page (e.g., title, date, content)
    title = soup.find('h1', class_='article-title').title.text.strip()
    date = soup.find('span', class_='article-date').text.strip()
    content = soup.find('div', class_='article-content').text.strip()

    # Store the scraped data in a dictionary
    data = {
        'title': title,
        'published_date': date,
        'content': content
    }

    # Append the data to the list
    scraped_data.append(data)

# Create a new CSV file to store the scraped data
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'date', 'content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for data in scraped_data:
        writer.writerow(data)

print("Scraping complete! Data saved to scraped_data.csv")