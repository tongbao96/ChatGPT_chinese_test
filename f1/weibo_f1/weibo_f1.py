# chatgpt = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': '人物：曾若彤璐、少年、杨素晗、你\n地名：天下、南京\n机构：无\n位置：无'}
# true = {'text': '曾若彤璐骑单车的少年要考驾照驰鸣天下苦逼青年杨素晗不屑与你装霄', 'entities': [('曾若彤', 'PER'), ('杨素晗', 'PER')]}
#
# predicted = {('曾若彤璐', '人物'), ('杨素晗', '人物'), ('你', '人物')}
# true = {('曾若彤', 'PER'), ('杨素晗', 'PER')}

TP = 0
FP = 0
FN = 0
chatgpt_count =0
true_count = 0
with open('WeiboNER_chatgpt.txt', 'r',encoding='utf-8') as f1, open('WeiboNER.txt', 'r',encoding='utf-8') as f2:
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
            # for key in chatgpt:
            #     chatgpt[key] = chatgpt[key].replace('。', '')

            for i in range(min(len(text1), len(text2))):
                if text1[i] != text2[i]:
                    print(f"Line {i + 1} is different.")
                    continue
            try:
                if '人物：' in chatgpt:
                    per = chatgpt.split('人物：')[1].split('\n')[0]
                    per = per.replace('。', '')
                    per = per.split('、')
                    predict_per = [(s, 'PER') for s in per]

                if '地名：' in chatgpt:
                    city =chatgpt.split('地名：')[1].split('\n')[0]
                    city = city.replace('。', '')
                    city = city.split('、')
                    predict_city = [(s, 'GPE') for s in city]

                if '机构：' in chatgpt:
                    org =chatgpt.split('机构：')[1].split('\n')[0]
                    org = org.replace('。', '')
                    org = org.split('、')
                    predict_org = [(s, 'ORG') for s in org]

                if '位置：' in chatgpt:
                    loc =chatgpt.split('位置：')[1].replace('。','')
                    loc = loc.replace('。','')
                    loc = loc.split('、')
                    predict_loc =[(s, 'LOC') for s in loc]


                final_label =set(predict_per+predict_city +predict_org+predict_loc)
                true = set(true)

                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x:  '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))

                chatgpt_count += len(final_label)
                true_count += len(true)
                Tp = len(final_label & true)
                Fp = len(final_label)-Tp
                Fn = len(true)- Tp

                TP += Tp
                FP += Fp
                FN += Fn
            except IndexError:
                continue


print(TP,FP,FN)
pre = TP/(TP+FP)
rec = TP/(TP+FN)
f1 = (2*pre*rec)/(pre+rec)
print(pre,rec,f1)
print(chatgpt_count)
print(true_count)
#542 1520 860
#0.26285160038797284 0.38659058487874465 0.312933025404157