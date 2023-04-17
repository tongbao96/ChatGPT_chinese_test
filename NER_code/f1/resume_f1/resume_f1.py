# chatgpt = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': '人物：曾若彤璐、少年、杨素晗、你\n地名：天下、南京\n机构：无\n位置：无'}
# true = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': [('曾若彤', 'PER'), ('杨素晗', 'PER')]}
#
# predicted = {('曾若彤璐', '人物'), ('杨素晗', '人物'), ('你', '人物')}
# true = {('曾若彤', 'PER'), ('杨素晗', 'PER')}
#{'entities': '人名：未提及\n国籍：中国\n籍贯：未提及\n种族：未提及\n专业：经济管理\n学位：研究生\n机构：公司\n头衔：党委委员、纪委书记、监事会主席、工会主席。'}
#{'entities': [('中国共产党', 'ORG'), ('研究生文化程度', 'EDU'), ('经济管理专业', 'PRO'), ('党委委员', 'TITLE'), ('纪委书记', 'TITLE'), ('监事会主席', 'TITLE'), ('工会主席', 'TITLE')]}

TP = 0
FP = 0
FN = 0
chatgpt_count = 0
true_count = 0
with open('resume_chatgpt_1000.txt', 'r',encoding='utf-8') as f1, open('Resume_new3.txt', 'r',encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    if len(lines1)!=len(lines2):
        print('文件行数不相等')
    else:

        for i in range(len(lines1)):
            text1 = eval(lines1[i])['text']
            text2 = eval(lines2[i])['text']

            chatgpt = eval(lines1[i])['entities']
            true = eval(lines2[i])['entities']

            for i in range(min(len(text1), len(text2))):
                if text1[i] != text2[i]:
                    print(f"Line {i + 1} is different.")
                    continue
 # {'entities': '人名：未提及\n国籍：中国\n籍贯：未提及\n种族：未提及\n专业：经济管理\n学位：研究生\n机构：公司\n头衔：党委委员、纪委书记、监事会主席、工会主席。'}
 # {'entities': [('中国共产党', 'ORG'), ('研究生文化程度', 'EDU'), ('经济管理专业', 'PRO'), ('党委委员', 'TITLE'), ('纪委书记', 'TITLE'), ('监事会主席', 'TITLE'), ('工会主席', 'TITLE')]}

            if '人名：' in chatgpt:
                name = chatgpt.split('人名：')[1].split('\n')[0]
                name = name.replace('。', '')
                name = name.split('、')
                predict_name = [(s, 'NAME') for s in name]

            if '国籍：' in chatgpt:
                cont = chatgpt.split('国籍：')[1].split('\n')[0]
                cont = cont.replace('。', '')
                cont = cont.split('、')
                predict_cont = [(s, 'CONT') for s in cont]

            if '籍贯：' in chatgpt:
                loc =chatgpt.split('籍贯：')[1].split('\n')[0]
                loc = loc.replace('。', '')
                loc = loc.split('、')
                predict_loc = [(s, 'LOC') for s in loc]

            if '种族：' in chatgpt:
                race =chatgpt.split('种族：')[1].split('\n')[0]
                race = race.replace('。', '')
                race = race.split('、')
                predict_race = [(s, 'RACE') for s in race]

            if '专业：' in chatgpt:
                pro =chatgpt.split('专业：')[1].split('\n')[0]
                pro = pro.replace('。', '')
                pro = pro.split('、')
                predict_pro =[(s, 'PRO') for s in pro]

            if '学位：' in chatgpt:
                edu = chatgpt.split('学位：')[1].split('\n')[0]
                edu = edu.replace('。', '')
                edu = edu.split('、')
                predict_edu = [(s, 'EDU') for s in edu]

            if '机构：' in chatgpt:
                org = chatgpt.split('机构：')[1].split('\n')[0]
                org = org.replace('。', '')
                org = org.split('、')
                predict_org = [(s, 'ORG') for s in org]


            if '头衔：' in chatgpt:
                title = chatgpt.split('头衔：')[1].replace('。','')
                title = title.replace('。', '')
                title = title.split('、')
                predict_title = [(s, 'TITLE') for s in title]



            final_label =set(predict_name + predict_cont + predict_race + predict_pro + predict_edu + predict_org + predict_title)

            true = set(true)
            #'entities': [('杨', ''), ('中信证券股份有限公司', 'ORG'), ('监事', 'TITLE')]}
            true= set(filter(lambda x: x[1] != '', true))

            final_label = set(filter(lambda x: x[0] != '无', final_label))
            final_label = set(filter(lambda x: '未提及' not in x[0], final_label))
            final_label = set(filter(lambda x: '未知' not in x[0], final_label))

            chatgpt_count += len(final_label)
            true_count += len(true)
            Tp = len(final_label & true)
            Fp = len(final_label)-Tp
            Fn = len(true)- Tp

            TP += Tp
            FP += Fp
            FN += Fn


print(TP,FP,FN)
pre = TP/(TP+FP)
rec = TP/(TP+FN)
f1 = (2*pre*rec)/(pre+rec)
print(pre,rec,f1)
print(chatgpt_count)
print(true_count)
#2627 4367 1305
#0.3756076637117529 0.6681078331637843 0.4808713161266703


#2627 4367 1262
#0.3756076637117529 0.675494985857547 0.48277129467977586


# 4162 2832 1750
# 0.5950814984272234 0.7039918809201624 0.6449713311637997
# 6994
# 5912