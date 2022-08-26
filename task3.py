# import json
# f=open('web_task1.json')
# data=json.load(f)
# def rat():
#     dic={}
#     for i in data:
#         rank=[]
#         rate=i['rating']
#         if rate not in dic:
#             for j in data:
#                 if rate==j['rating']:
#                     rank.append(j)
#             dic[rate]=rank
#         print(rank)
#     with open('abc.json','w') as fil:
#         json.dump(rank,fil,indent=8)
# rat()
    


# import json
# with open("task2.json",'r') as f:
#     obj=json.load(f)
# print(obj)

def prod2sum(a, b, c, d):
    h=[]
    e=a**2+b**2
    f=c**2+d**2
    s=e*f
    print(s)
    i=1
    while i<s:
        if i**2+(i+1)**2==s:
            k=[i,i+1]
        h.append(k)
        i+=1
    return  h
    
p=prod2sum(1,2,1,3)
print(p)   


