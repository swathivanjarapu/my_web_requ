import requests 
import json 
def my_requests():
    res=requests.get("http://saral.navgurukul.org/api/courses")
    data1=json.loads(res.text)

    with open("meraki.json","w") as res:
        json.dump(data1,res,indent=3)

    store=data1["availableCourses"]                                                    
    id =[]
    name=[]
    # print(store)
    for i in range (len(store)):
        print(i+1,store[i]["name"],end="--")
        print(store[i]["id"])

        id.append(store[i]["id"])

        name.append(store[i]["name"])

    print("-------")

    n=int(input("please enter the  serial :- "))
    n1=id[n-1]
    print("-------")
    print()
    print("id number:--",n1)
    print()
    res2=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercises")
    # print(res2)
    data2=res2.json()
    slug=[]
    count=1
    for var in data2["data"]:
        print(count,var["name"])
        slug.append(var["slug"])
        count+=1
        for child in  var["childExercises"]:
            print(" ",count,child[name])
            slug.append(child["slug"])
            count+=1
    print("--------")

    var2=int(input("give slug number--"))
    res4=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercise/getBySlug?slug="+str(slug[var2-1]))
    data3=res4.json()
    print(data3["content"])
    while True:
        x=var2

        print()
        print("-------")
        options=input("if you want to go back ,exit:-")

        if options =="next":
            x+=1
            req=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercise/getBySlug?slug="+str(slug[x-1]))
            r1=req.json()
            print("content",r1,["content"])
            print(x)
            break
        elif options=="back":
            c=1
            for dict1 in data2["data"]:
                print(c,dict1["name"])
                c+=1
                for i in dict1 ["childExercises"]:
                    print("   ",c,i["name"])
                    c+=1
                    break
        else:
            break

my_requests()



# # import requests 
# # import json 
# res=requests.get("http://saral.navgurukul.org/api/courses")
# data1=json.loads(res.text)

# with open("meraki.json","w") as res:
#     json.dump(data1,res,indent=3)

# store=data1["availableCourses"]                                                    
# id =[]
# name=[]
# for i in range (len(store)):

#     print(i+1,store[i]["name"],end="--")

#     print(store[i]["id"])

#     id.append(store[i]["id"])

#     name.append(store[i]["name"])

# print("-------")

# n=int(input("please enter the  ID :- "))
# n1=id[n-1]
# print("-------")
# print()
# print("id number:--",n1)
# print()
# res2=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercises")
# print(res2)
# data2=res2.json()
# slug=[]
# count=1
# for var in data2["data"]:
#     print(count,var["name"])
#     slug.append(var["slug"])
#     count+=1
#     for child in  var["childExercises"]:
#         print(" ",count,child[name])
#         slug.append(child["slug"])
#         count+=1
# print("--------")

# var2=int(input("give slug number--"))
# res4=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercise/getBySlug?slug="+str(slug[var2-1]))
# data3=res4.json()
# print(data3["content"])
# while True:
#     x=var2

#     print()
#     print("-------")
#     options=input("if you want to go back ,exit:-")

#     if options =="next":
#         x+=1
#         req=requests.get("http://saral.navgurukul.org/api/courses/"+n1+"/exercise/getBySlug?slug="+str(slug[x-1]))
#         r1=req.json()
#         print("content",r1,["content"])
#         print(x)
#         break
#     elif options=="back":
#         c=1
#         for dict1 in data2["data"]:
#             print(c,dict1["name"])
#             c+=1
#             for i in dict1 ["childExercises"]:
#                 print("   ",c,i["name"])
#                 c+=1
#                 break
#     else:
#         break
