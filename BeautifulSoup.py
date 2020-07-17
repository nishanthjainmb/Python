from bs4 import BeautifulSoup
import requests
import csv
import os

# os.mkdir('C:\Users\Nishanth\Desktop')
csvfile=open('test.csv','w')
csvwriter=csv.writer(csvfile)
csvwriter.writerow(['Headline','Paragraph','Video link'])
source=requests.get('https://coreyms.com').text

 
soup=BeautifulSoup(source,'lxml')
# print(soup.prettify())
for article  in soup.find_all('article'):

    headline=article.h2.a.text
    print(headline)
    para=soup.find('div',class_='entry-content').p.text
    print(para)
    try:
        vid_src=article.find('iframe',class_='youtube-player')['src']
        vid_id=vid_src.split('/')[4]
        vid_id=vid_id.split('?')[0]
        youtubeurl=f'https://www.youtube.com/watch?v={vid_id}'
        
    except Exception as ex:
        print('Error in you tube link')
    print(youtubeurl)
    print()
    csvwriter.writerow([headline,para,youtubeurl])

csvfile.close()