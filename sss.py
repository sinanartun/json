## Kütüphane yüklenmesi

import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import glob
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)


## döküman çekimi
xml_files = glob.glob("data/splitted_xml/*.xml")

for i in xml_files:
    root = ET.parse(i).getroot()

## satir sayisi
xml_release=[]
for i in root:
    xml_release.append(root[0].tag)
xml_release_count= len(xml_release)


## released_id

release_id=[]
for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for x in root.findall("./release/[@id]"):
        release_id.append(x.attrib["id"])
        print(index)


## artist_id
artist_id=[]
for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for a in root.findall("./release/artists/artist[1]/id"):
        artist_id.append(a.text)
        print(index)


## artist_name
artist_name=[]
for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for b in root.findall("./release/artists/artist[1]/name"):
        print(b.text)
        artist_name.append(b.text)
        print(index)


## title
titleYes=[]
titleNo=[]
for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
    if 'title' in childTag:
        titleYes.append(i)
    else:
        titleNo.append(i)
title=[]
for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in titleYes:
            for child in root[root_index]:
                if child.tag=='title':
                    title.append(child.text)
                    print(index)
        else:
            title.append('None')
            print(index)

## Released
releasedYes=[]
releasedNo=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
    if 'released' in childTag:
        releasedYes.append(i)
    else:
        releasedNo.append(i)

year=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in releasedYes:
            for child in root[root_index]:
                if child.tag=='released':
                    year.append(str(child.text).split('-')[0])
                    print(index)
        else:
            year.append('None')
            print(index)

## genre

genresYes=[]
genresNo=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
    if 'genres' in childTag:
        genresYes.append(i)
    else:
        genresNo.append(i)
genre=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in genresYes:
            for child in root[root_index]:
                if child.tag=='genres':
                    genre.append((child[0].text))
                    print(index)
        else:
            genre.append('None')
            print(index)

## genre2

genres2Yes=[]
genres2No=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
        if child.tag=='genres':
            if len(child)>2:
                genres2Yes.append(i)
    else:
        if not i in genres2Yes:
            genres2No.append(i)
genre2=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in genres2Yes:
            for child in root[root_index]:
                if child.tag=='genres':
                    if len(child)>2:
                        genre2.append((child[1].text))
                        print(index)
        else:
            genre2.append('None')
            print(index)

## genre3

genres3Yes=[]
genres3No=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
        if child.tag=='genres':
            if len(child)>3:
                genres3Yes.append(i)
    else:
        if not i in genres3Yes:
            genres3No.append(i)
            print(index)

genre3=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in genres3Yes:
            for child in root[root_index]:
                if child.tag=='genres':
                    if len(child)>3:
                        genre3.append((child[2].text))
        else:
            genre3.append('None')
            print(index)

## styles
stylesYes=[]
stylesNo=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
    if 'styles' in childTag:
        stylesYes.append(i)
    else:
        stylesNo.append(i)

style=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in stylesYes:
            for child in root[root_index]:
                if child.tag == 'styles':
                    style.append(child[0].text)
                    print(index)

        else:
            style.append('None')
            print(index)

## style2

styles2Yes=[]
styles2No=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
        if child.tag=='styles':
            if len(child)>2:
                styles2Yes.append(i)
    else:
        if not i in styles2Yes:
             styles2No.append(i)

style2=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in styles2Yes:
            for child in root[root_index]:
                if child.tag == 'styles':
                    if len(child) > 2:
                        style2.append((child[1].text))
                        print(index)

        else:
            style2.append('None')
            print(index)

## style3

styles3Yes=[]
styles3No=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
        if child.tag=='styles':
            if len(child)>3:
                styles3Yes.append(i)
    else:
        if not i in styles3Yes:
             styles3No.append(i)


style3=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in styles3Yes:
            for child in root[root_index]:
                if child.tag == 'styles':
                    if len(child) > 3:
                        style3.append((child[2].text))
                        print(index)

        else:
            style3.append('None')
            print(index)

## format

formatsYes=[]
formatsNo=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
    if 'formats' in childTag:
        formatsYes.append(i)
    else:
        formatsNo.append(i)

format=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in formatsYes:
            for child in root[root_index]:
                if child.tag == 'formats':
                    format.append(child[0].attrib['name'])
                    print(index)

        else:
            format.append('None')
            print(index)

# country

countriesYes=[]
countriesNo=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
    if 'country' in childTag:
        countriesYes.append(i)
    else:
        countriesNo.append(i)

country=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in countriesYes:
            for child in root[root_index]:
                if child.tag == 'country':
                    country.append((child.text))
                    print(index)

        else:
            country.append('None')
            print(index)

# label

labelYes=[]
labelNo=[]

for i in range(0,xml_release_count):
    childTag=[]
    for child in (root[i]):
        childTag.append(child.tag)
    if 'labels' in childTag:
        labelYes.append(i)
    else:
        labelNo.append(i)

label=[]

for index,i in enumerate(xml_files):
    root = ET.parse(i).getroot()
    for root_index in range(xml_release_count):
        if root_index in formatsYes:
            for child in root[root_index]:
                if child.tag == 'labels':
                    label.append((child[0].attrib['name']))
                    print(index)

        else:
            label.append('None')
            print(index)

# dataframe

columns_values={'release_id':release_id,
                'artist_id':artist_id,
                'artist_name':artist_name,
                'title':title,
                'genre':genre,
                'genre2':genre2,
                'genre3':genre3,
                'style':style,
                'style2':style2,
                'style3':style3,
                'country':country,
                'label':label,
                'format':format,
                'year':year
               }

df=pd.DataFrame(columns_values)
df.to_csv("discogs_final.csv", index=False)

# statistics

import requests
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")

for index, i in enumerate(df['release_id']):

    url = 'https://www.discogs.com/release/' + i
    response = requests.get(url)

    if response.status_code != 200:  # could also check == requests.codes.ok
        continue

    else:

        html_text = requests.get(url).text
        soup_i = (BeautifulSoup(html_text, 'html.parser'))

        statistics = soup_i.find("section", {"id": "release-stats"}).find_all("ul")

        df.loc[index, 'have'] = statistics[0].find_all('li')[0].find('a').get_text()

        df.loc[index, 'want'] = statistics[0].find_all('li')[1].find('a').get_text()

        df.loc[index, 'avg_rating'] = statistics[0].find_all('li')[2].find('span').get_text()

        df.loc[index, 'ratings'] = statistics[0].find_all('li')[3].find('a').get_text()

        print(index)

# rating 0 olma durumu

for index,i in enumerate(df['ratings']):
    if i=='0':
        df.loc[index,'avg_rating']=0

# final dataframe

df.to_csv("discogs_final.csv", index=False)