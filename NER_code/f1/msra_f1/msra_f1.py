
TP = 0
FP = 0
FN = 0
chatgpt_count = 0
true_count = 0
with open('msra_chatgpt900.txt', 'r',encoding='utf-8') as f1, open('MSRA_new3.txt', 'r',encoding='utf-8') as f2:
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
 # {'text': '在采访中，记者看到，有的主人还为书房起了雅号：光芒书斋、夜读斋、星艺阁等。', 'entities': '人名：无\n地名：无\n机构名：无'}
 # {'text': '在采访中，记者看到，有的主人还为书房起了雅号：光芒书斋、夜读斋、星艺阁等。','entities': [('光芒书斋', 'LOC'), ('夜读斋', 'LOC'), ('星艺阁', 'LOC')]}

            if '人名：' in chatgpt:
                name = chatgpt.split('人名：')[1].split('\n')[0]
                name = name.replace('。', '')
                name = name.split('、')
                predict_name = [(s, 'NR') for s in name]

            if '地名：' in chatgpt:
                loc = chatgpt.split('地名：')[1].split('\n')[0]
                loc = loc.replace('。', '')
                loc = loc.split('、')
                predict_loc = [(s, 'NS') for s in loc]

            if '机构名：' in chatgpt:
                org = chatgpt.split('机构名：')[1].replace('。','')
                org = org.replace('。', '')
                org = org.split('、')
                predict_org = [(s, 'NT') for s in org]



            final_label =set(predict_name  + predict_loc + predict_org)

            true = set(true)
            #'entities': [('杨', ''), ('中信证券股份有限公司', 'ORG'), ('监事', 'TITLE')]}
            true= set(filter(lambda x: x[1] != '', true))

            final_label = set(filter(lambda x: x[0] != '无', final_label))
            final_label = set(filter(lambda x: '未提及' not in x[0], final_label))
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
print(chatgpt_count)
print(true_count)

# 1944 1874 1322
# 0.5091671031953903 0.5952235150030618 0.5488424618859402
# 3818
# 3266