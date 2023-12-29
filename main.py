# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json
import re
import csv

csvTitles = ['review', 'rating', 'sentiment']


def createTemplateCSV():
    with open('reviews.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csvTitles)


def extract(ids):
    with open('reviews.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csvTitles)
        writer.writeheader()

        for id in ids:
            idString = id.split("|")
            name = idString[0]
            idApp = idString[1]

            slack = AppStore(country='us', app_name=name, app_id=idApp)

            slack.review(how_many=5000)

            for review in slack.reviews:
                review_comment = review['review']
                rating = review['rating']
                sentiment = '0' if rating in [1, 2] else '1'

                writer.writerow({'review': review_comment,
                                 'rating': rating,
                                 'sentiment': sentiment})


# createTemplateCSV()
ids = ['99-vá-de-carro-moto-ou-taxi|553663691']
extract(ids=ids)
