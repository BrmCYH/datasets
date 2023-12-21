import json,os 
import re
from tqdm import tqdm
dictET={"Idt":1,"AT":2,"Cam":3,"TA":4,"Mlw":5,"CoF":6,"Tool":7,"Vul":8,"Loc":9,"Moti":10,"Ass":11,"Trans":12,"IOC":13,"Time":14}
dictRE={"uses":1,"Located":2,"exist":3,"owns":4,"targets":5,"attributed-to":6,"indicates":7,"through":8,"mitigates":9,"host":10,"related-to":11,"happen":12}
def reladis():
    for key,item in dictRE.items():
        print(item,":",key,end="   " )
def process(item,i):#return list
    '''
        处理GPT直接输出的内容，尽可能只保留三元组
        尽可能第一次先交互式完成
        同时统计所有的关系类型

    '''
    with open(f"one/{i}.json","+a",encoding="utf-8")as f2:
        
        # print(item["input"])
        # cont=int(input("是否要继续？ 1,2"))
        # if cont!=1:
        #     f2.writelines("None")#不存在关系
        #     return False
        # 尝试转为list
        try:
            #先使用list进行转换 是否为list形式
            # "[]"-->[]
            xlist=eval(item["output"]) #普通list形式
            # 可能内容为列表 元组 字典 等等 下面再进行判断
            session1=xlist
            print(f"直接list方法 {xlist}")
            label=0
        except:
            # try:
            #     xlist=eval(item["output"].replace("\n",""))
            #     # 去掉\n后能够转为列表 元组 字典的形式，使用或不使用\n
            #     # 如果不使用\n则返回的内容 长度为1  情况 内部使用括号将实体括住
            #     session1=xlist 
            #     print(f"去掉\n再list方法 {xlist}")

            # except:
            #     #在list形式之外
            #     # 1. 字符串形式 
            session1=item["output"].split("\n")
            label=1
            print(f"直接\\n分割方法 {session1}")

        # return True
        # if label==1:
        list1=[]
        out=""

        while(not(out!="")):
            entity1=input("\t\t请输入实体1:")
            entity1type=input("\t\t请输入实体1类型:")
            entity2=input("\t\t请输入实体2:")
            entity2type=input("\t\t请输入实体2类型:")
            # print({})
            reladis()
            relation=input("\t\t输入关系类型id:")
            list1.append({"entity1":entity1,"entity1type":entity1type,"entity2":entity2,"entity2type":entity2type,"relation":relation})
            print(list1)
            out=input("\n是否继续，回车继续;1结束\n")
            if out=="1":
                json_string = json.dumps(list1,ensure_ascii=False)
                f2.writelines(json_string)


            




        # if len(session1)==1:# 无实体 或者\n无法分割
        #     #尝试使用括号进行划分
        #         #匹配左右括号
        #         # 处理\n无法分割的情况
        #     yuankuohao=re.compile(r"[(]\W*\w*\W*[)]")
        #     fangkuohao=re.compile(r"[[]\W*\w*\W*[]]")

        #     # for x in session1:
        #     ppei1=re.findall(yuankuohao,session1)
        #     ppei2=re.findall(fangkuohao,session1)
        #     print(session1,"\n",ppei1)
        #     print("\n",ppei2)
        #     tup=int(input("输入选择的内容，方括号2，圆括号1，都不正确则填0"))
        #     if tup==0:
        #         print('此时应是每条记录 未使用方括号或者圆括号')

        #     # if sign ==1:
        #         guanxilist=[]
        #         input=input("请输入第1个关系 （关系，实体1，实体2）")
        #         num=2
        #         while(not(input=="")):
                    
        #             guanxilist.append(input)
        #             input=input(f'请输入第{num}个关系')
        #             num=num+1
        #     else:


                    



        # else:# \n分割  list列表
        #     for strx in session1:
        #         #如果提取出多个
        # # session1 以\n为分隔   存在\n分隔了多个内容（比较细） 实体与关系也用\n分隔  
        # # ①\n +序号 

        # session1=item.split('\n')

    #session2  以逗号分隔 （无法区分）但 各个关系用括号包含
    
    #session3  不是三元组的方式返回 而是通过在原文中进行方括号标注或者为括号

    #session4 在实体后添加(实体A) 后面跟关系

    # session5 实体抽取一部分 关系抽取一部分

    # session6 \n分割的为一段包含关系文本

    # 本身为list(Tuple)|list(Dict) 直接使用list函数进行转换
    pass
def state(item):#return 为List
    '''
        根据三元组关系进行划分
        对关系进行分类
    '''
    pass
def Entity_type(item,Enlist):
    '''
        对关系三元组中的实体类别进行标注
        取出该行记录的所有实体 根据内容进行实体类别划分
    '''
    return 1
def Entity_extra(item):
    '''
        获取该条记录的所有实体
    '''
    pass
with open("GPTanswer.jsonl","r",encoding="utf-8")as f1:

    n_dat=f1.readlines()
    i=0
    try:
        nums =max([int(f.split('.')[0]) for f in os.listdir("one")])
    except ValueError:
        nums=0
    for x in tqdm(n_dat):
        # print(i)
        # nums=500

        i=i+1
        if nums>=i:
            continue
        
        crith=json.loads(x)
        conf=input("\n{}是否继续(1:下一个;回车:处理当前\n)".format(crith["input"]))
        if conf!="":
            continue
        
        process_t=process(crith,i)


        # try:
        #     processed_txt=process(crith)
        #     if processed_txt==False:# 如果不符合提取规范 源文本或者
        #         continue
        # except:
        #     continue

        # Enlist=[]
        # relaLS=state(processed_txt)
        # for item in relaLS:
        #     Enty=Entity_extra(item)

        #     Enlist.append(Enty)
        # x=Entity_type(item=relaLS,Enlist=Enlist)


