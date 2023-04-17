# chatgpt = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': '人物：曾若彤璐、少年、杨素晗、你\n地名：天下、南京\n机构：无\n位置：无'}
# true = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': [('曾若彤', 'PER'), ('杨素晗', 'PER')]}
#
# predicted = {('曾若彤璐', '人物'), ('杨素晗', '人物'), ('你', '人物')}
# true = {('曾若彤', 'PER'), ('杨素晗', 'PER')}

TP = 0
FP = 0
FN = 0
with open('../ChatGPT_test_result/resume_chatgpt_1000.txt', 'r',encoding='utf-8') as f1, open('../NER_test_data/Resume_new3.txt', 'r',encoding='utf-8') as f2:
#with open('../1.txt', 'r',encoding='utf-8') as f1, open('../2.txt', 'r',encoding='utf-8') as f2:

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
            tp = 0
            fp = 0
            fn = 0
            #{'text': '外星人如果占领地球。美国有超人，日本有奥特曼，我们有什么？！！', 'entities': '人物：超人、奥特曼\n地名：地球、美国、日本\n机构：无\n位置：地球'}
            final_label = set(predict_name + predict_cont + predict_race + predict_pro + predict_edu + predict_org + predict_title)
            true = set(true)
            # 'entities': [('杨', ''), ('中信证券股份有限公司', 'ORG'), ('监事', 'TITLE')]}
            true = set(filter(lambda x: x[1] != '', true))

            final_label = set(filter(lambda x: x[0] != '无', final_label))
            final_label = set(filter(lambda x: '未提及' not in x[0], final_label))
            final_label = set(filter(lambda x: '未知' not in x[0], final_label))

            merged = {}
            for item in final_label:
                if item[0] in merged:
                    merged[item[0]].append(item[1])
                else:
                    merged[item[0]] = [item[1]]

            result = set((k, tuple(v)) for k, v in merged.items())

            for p in result:
                if len(p[1]) == 1:
                # 遍历真实实体
                     for t in true:
                    # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1][0]:  # 模糊匹配
                            tp += 1
                            break
                else:
                     for t in true:
                         for m in range(len(p[1])):
                    # 判断真实实体是否被预测为实体
                            if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1][m]:  # 模糊匹配
                                tp += 2
                                break

            fp += len(result) - tp
            fn += len(true) - tp

            TP += tp
            FP += fp
            FN += fn


print(TP,FP,FN)
pre = TP/(TP+FP)
rec = TP/(TP+FN)
f1 = (2*pre*rec)/(pre+rec)
print(pre,rec,f1)
#926 1165 476

