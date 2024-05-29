import json
with open('D:\\GithubBeta\\Vue\\sft\\TKdeal.json','r',encoding='utf-8')as f1:
    x1=json.load(f1)
with open('D:\\GithubBeta\\Vue\\sft\\deal.json','r',encoding='utf-8')as f1:
    x2=json.load(f1)
list2 = [i for i in x1]
print(len(list2))
for i in x2:
    list2.append(i) 
print(len(list2))
with open('D:\\GithubBeta\\Vue\\sft\\train.json','w',encoding='utf-8')as f1:
    json.dump(list2,f1,ensure_ascii=False,indent=2)