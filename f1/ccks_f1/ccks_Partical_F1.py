# chatgpt = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': '人物：曾若彤璐、少年、杨素晗、你\n地名：天下、南京\n机构：无\n位置：无'}
# true = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': [('曾若彤', 'PER'), ('杨素晗', 'PER')]}
#
# predicted = {('曾若彤璐', '人物'), ('杨素晗', '人物'), ('你', '人物')}
# true = {('曾若彤', 'PER'), ('杨素晗', 'PER')}

TP = 0
FP = 0
FN = 0
with open('../ChatGPT_test_result/CCKS2019_chatgpt_1000.txt', 'r',encoding='utf-8') as f1, open('../NER_test_data/CCKS2019_shuffle_1000_main.txt', 'r',encoding='utf-8') as f2:
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
            if '\n\n' in chatgpt:
                # print('有换行符',i)
                if '实验室检验：' in chatgpt:
                    shiyanshi = chatgpt.split('实验室检验：')[1].split('\n\n')[0]
                    shiyanshi = shiyanshi.replace('。', '')
                    shiyanshi = shiyanshi.split('、')
                    predict_shiyanshi = [(s, '实验室检验') for s in shiyanshi]

                if '影像检查：' in chatgpt:
                    yingxiangjc = chatgpt.split('影像检查：')[1].split('\n\n')[0]
                    yingxiangjc = yingxiangjc.replace('。', '')
                    yingxiangjc = yingxiangjc.split('、')
                    predict_yingxiangjc = [(s, '影像检查') for s in yingxiangjc]

                if '手术：' in chatgpt:
                    shoushu = chatgpt.split('手术：')[1].split('\n\n')[0]
                    shoushu = shoushu.replace('。', '')
                    shoushu = shoushu.split('、')
                    predict_shoushu = [(s, '手术') for s in shoushu]

                if '疾病和诊断：' in chatgpt:
                    jibing = chatgpt.split('疾病和诊断：')[1].split('\n\n')[0]
                    jibing = jibing.replace('。', '')
                    jibing = jibing.split('、')
                    predict_jibing = [(s, '疾病和诊断') for s in jibing]

                if '药物：' in chatgpt:
                    yaowu = chatgpt.split('药物：')[1].split('\n\n')[0]
                    yaowu = yaowu.split('、')
                    predict_yaowu = [(s, '药物') for s in yaowu]

                if '解剖部位实体：' in chatgpt:
                    buwei = chatgpt.split('解剖部位实体：')[1].replace('。', '')
                    buwei = buwei.split('、')
                    predict_buwei = [(s, '解剖部位实体') for s in buwei]


            else:
                # 'entities': '实验室检验：间接Coomb’s试验，新生儿G6PD活性试验，肝功能检查；影像检查：无；手术：无；疾病和诊断：溶血性贫血，G-6-PD酶缺乏症，贫血性心脏病，肝功能不全；药物：输血，洗涤红细胞；解剖部位实体：无。'}
                # print("没有换行符",i)
                if '实验室检验：' in chatgpt:
                    shiyanshi = chatgpt.split('实验室检验：')[1].split('；')[0]
                    shiyanshi = shiyanshi.replace('。', '')
                    shiyanshi = shiyanshi.split('、')
                    predict_shiyanshi = [(s, '实验室检验') for s in shiyanshi]

                if '影像检查：' in chatgpt:
                    yingxiangjc = chatgpt.split('影像检查：')[1].split('；')[0]
                    yingxiangjc = yingxiangjc.replace('。', '')
                    yingxiangjc = yingxiangjc.split('、')
                    predict_yingxiangjc = [(s, '影像检查') for s in yingxiangjc]

                if '手术：' in chatgpt:
                    shoushu = chatgpt.split('手术：')[1].split('；')[0]
                    shoushu = shoushu.replace('。', '')
                    shoushu = shoushu.split('、')
                    predict_shoushu = [(s, '手术') for s in shoushu]

                if '疾病和诊断：' in chatgpt:
                    jibing = chatgpt.split('疾病和诊断：')[1].split('；')[0]
                    jibing = jibing.replace('。', '')
                    jibing = jibing.split('、')
                    predict_jibing = [(s, '疾病和诊断') for s in jibing]

                if '药物：' in chatgpt:
                    yaowu = chatgpt.split('药物：')[1].split('；')[0]
                    yaowu = yaowu.split('、')
                    predict_yaowu = [(s, '药物') for s in yaowu]

                if '解剖部位实体：' in chatgpt:
                    buwei = chatgpt.split('解剖部位实体：')[1].replace('。', '')
                    buwei = buwei.split('、')
                    predict_buwei = [(s, '解剖部位实体') for s in buwei]

            tp = 0
            fp = 0
            fn = 0
            #{'text': '外星人如果占领地球。美国有超人，日本有奥特曼，我们有什么？！！', 'entities': '人物：超人、奥特曼\n地名：地球、美国、日本\n机构：无\n位置：地球'}
            final_label =set(predict_shiyanshi + predict_yingxiangjc + predict_shoushu + predict_jibing + predict_yaowu + predict_buwei)
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
# 2901 3784 4032
# 0.4339566192969334 0.4184335785374297 0.4260537523865472

