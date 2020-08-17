from bs4 import BeautifulSoup
import requests
import os


username = input('Enter the username: ')
url = ('https://'+username+'.tumblr.com')
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

links = []

x = soup.select('img[src^="https://64.media.tumblr.com/"]')

for img in x:
    links.append(img['src'])

total = len(links)    
#for l in links:
 #   print(l)  
os.mkdir(username)
i = 1
for index, img_link in enumerate(links):
    if i <=total:
        img_data = requests.get(img_link).content
        with open(username +'/'+str(index+1)+'.jpg', 'wb+')as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break
print('Downloading completed successfully.')