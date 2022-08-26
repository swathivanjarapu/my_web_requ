from email.mime import image
import json
import requests
from bs4 import BeautifulSoup
a=requests.get('https://www.imdb.com/title/tt0066763/')
scop=BeautifulSoup(a.text,'html.parser')
b=scop.find('script',type='application/ld+json').text
c=json.loads(b)
# print(c)

# with open('ght.json','w') as f:
#     json.dump(c,f, indent=8)
d={}
for i in c:
    d['name']=c['name']
    d['director']=[c['director'][0]['name']]
    d['countery']='india'
    d['image']=c['image']
    d['description']=c['description']
    d['language']=c['review']['inLanguage']
    d['genre']=c['genre']
with open('ght.json','w') as f:
     json.dump(d,f, indent=8)


