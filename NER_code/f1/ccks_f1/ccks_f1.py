
TP = 0
FP = 0
FN = 0
chatgpt_count = 0
true_count = 0
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

            for t in range(min(len(text1), len(text2))):
                if text1[t] != text2[t]:
                    print(f"Line {t + 1} is different.")
                    continue
#{'entities': '实验室检验：无明确提及。\n\n影像检查：腹部B超、胸部+全腹CT。\n\n手术：左半结肠切除术。\n\n疾病和诊断：大肠回盲部结外粘膜相关淋巴组织边缘区B细胞淋巴瘤(MALT)。\n\n药物：环磷酰胺、表柔比星、长春新碱、泼尼松。\n\n解剖部位实体：回盲部壁、左半结肠、盲肠部、肠周淋巴结。'}
# 'entities': '实验室检验：间接Coomb’s试验，新生儿G6PD活性试验，肝功能检查；影像检查：无；手术：无；疾病和诊断：溶血性贫血，G-6-PD酶缺乏症，贫血性心脏病，肝功能不全；药物：输血，洗涤红细胞；解剖部位实体：无。'}
#'entities': [('头', '解剖部位'), ('头', '解剖部位'), ('胸', '解剖部位'), ('心', '解剖部位'), ('胸', '解剖部位'), ('腹', '解剖部位'),
                        # ('腹', '解剖部位'), ('腹', '解剖部位'), ('溶血性贫血', '疾病和诊断'), ('间接Coomb’s试验', '实验室检验'),
                        # ('新生儿G6PD活性试验', '实验室检验'), ('溶血性贫血', '疾病和诊断'), ('G-6-PD酶缺乏症', '疾病和诊断'), ('贫血性心脏病', '疾病和诊断'),
                        # ('肝功能不全', '疾病和诊断'), ('心', '解剖部位'), ('腹', '解剖部位'), ('腹', '解剖部位'), ('溶血性贫血', '疾病和诊断')]}
            if  '\n\n' in chatgpt:
                #print('有换行符',i)
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
                    shoushu =chatgpt.split('手术：')[1].split('\n\n')[0]
                    shoushu = shoushu.replace('。', '')
                    shoushu = shoushu.split('、')
                    predict_shoushu = [(s, '手术') for s in shoushu]

                if '疾病和诊断：' in chatgpt:
                    jibing =chatgpt.split('疾病和诊断：')[1].split('\n\n')[0]
                    jibing= jibing.replace('。', '')
                    jibing = jibing.split('、')
                    predict_jibing = [(s, '疾病和诊断') for s in jibing]

                if '药物：' in chatgpt:
                    yaowu =chatgpt.split('药物：')[1].split('\n\n')[0]
                    yaowu  = yaowu .split('、')
                    predict_yaowu  =[(s, '药物') for s in yaowu ]

                if '解剖部位实体：' in chatgpt:
                    buwei = chatgpt.split('解剖部位实体：')[1].replace('。','')
                    buwei = buwei.split('、')
                    predict_buwei = [(s, '解剖部位实体') for s in buwei]


            else:
# 'entities': '实验室检验：间接Coomb’s试验，新生儿G6PD活性试验，肝功能检查；影像检查：无；手术：无；疾病和诊断：溶血性贫血，G-6-PD酶缺乏症，贫血性心脏病，肝功能不全；药物：输血，洗涤红细胞；解剖部位实体：无。'}
                #print("没有换行符",i)
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
                    shoushu =chatgpt.split('手术：')[1].split('；')[0]
                    shoushu = shoushu.replace('。', '')
                    shoushu = shoushu.split('、')
                    predict_shoushu = [(s, '手术') for s in shoushu]

                if '疾病和诊断：' in chatgpt:
                    jibing =chatgpt.split('疾病和诊断：')[1].split('；')[0]
                    jibing= jibing.replace('。', '')
                    jibing = jibing.split('、')
                    predict_jibing = [(s, '疾病和诊断') for s in jibing]

                if '药物：' in chatgpt:
                    yaowu =chatgpt.split('药物：')[1].split('；')[0]
                    yaowu  = yaowu .split('、')
                    predict_yaowu  =[(s, '药物') for s in yaowu ]

                if '解剖部位实体：' in chatgpt:
                    buwei = chatgpt.split('解剖部位实体：')[1].replace('。','')
                    buwei = buwei.split('、')
                    predict_buwei = [(s, '解剖部位实体') for s in buwei]

            final_label =set(predict_shiyanshi + predict_yingxiangjc + predict_shoushu + predict_jibing + predict_yaowu + predict_buwei)

            true = set(true)
            #'entities': [('杨', ''), ('中信证券股份有限公司', 'ORG'), ('监事', 'TITLE')]}
            true= set(filter(lambda x: x[1] != '', true))

            final_label = set(filter(lambda x: x[0] != '无', final_label))
            final_label = set(filter(lambda x: '提及' not in x[0], final_label))
            final_label = set(filter(lambda x: '未知' not in x[0], final_label))


            chatgpt_count += len(final_label)
            true_count+=len(true)
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
print("chatgpt",chatgpt_count)
print("true",true_count)


# 1944 5126 4989
# 0.27496463932107496 0.2803980960623107 0.2776547882596586
# chatgpt 7070
# true 6933