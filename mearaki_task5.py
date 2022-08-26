
# import requests
# import json
# from bs4 import BeautifulSoup
# url_list=[]
# with open('web_task1.json','r') as f:
#     a=json.load(f)
# for i in a:
#     url_list.append(i['url'])

# b=url_list[:20]
# # print(b)
# list=[]
# for j in b :
#     rel=requests.get(j)
#     soup=BeautifulSoup(rel.content,"html.parser")
#     con=soup.find('script',type='application/ld+json').text
#     h=json.loads(con)
#     dic={}
#     for k in h:
#         dic['name']=h['name']
#         dic['director']=[h['director'][0]['name']]
#         dic['image']=h['image']
#         dic['description']=h['description']
#         dic["language"]=h['review']['inLanguage']
#         dic['genre']=h['genre']
#         dic['country']='india'
#     list.append(dic)

        
# with open('5th_task.json','w') as file:
#     json.dump(list,file,indent=8)


import requests
import json
from bs4 import BeautifulSoup
url_list=[]
with open('task2.json','r') as f:
    a=json.load(f)
   
for i in a:
    url_list.append(i['url'])
print(url_list)

# b=url_list[:25]

# details=['name','director','image','description','language','genre',]
# # print(b)
# list=[]
# for j in url_list:
   
#     rel=requests.get(j)
#     soup=BeautifulSoup(rel.content,"html.parser")
#     con=soup.find('script',type='application/ld+json').text
#     h=json.loads(con)
#     dic={}
#     for k in h:
#         dic['name']=h['name']
#         dic['director']=h['director'][0]['name']
#         dic['image']=h['image']
#         dic['description']=h['description']
#         dic["language"]=h['review']['inLanguage']
#         dic['genre']=h['genre']
#         dic['country']='india'
#     list.append(dic)

# with open('5th_task.json','w') as file:
#     json.dump(list,file,indent=8)