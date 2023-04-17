# -*- coding: utf-8 -*-
from chatGPT import chatGPT_runse

count= 0
read_file = open('../data/test.txt','r',encoding='utf-8')
wrete_file = open('zero_shot.txt','a',encoding='utf-8')
for n,line in enumerate(read_file.readlines()):
    print(n)
    data_ ={}
    tuples  = line.split('	')
    entity1 = tuples[0]
    entity2 = tuples[1]
    relation= tuples[2]
    true_lable  = [entity1,entity2,relation]
    text = tuples[3].replace('\n','')
    data_['text'] = text
    prompt = "relation tags：['unknown', '注资', '拥有', '纠纷', '自己', '增持', '重组', '买资', '签约', '持股', '交易', '入股', '转让', '成立', '分析', '合作', '帮助', '发行', '商讨', '合并', '竞争', '订单', '减持', '合资', '收购', '借壳', '欠款', '被发行', '被转让', '被成立', '被注资', '被持股', '被拥有', '被收购', '被帮助', '被借壳', '被买资', '被欠款', '被增持', '拟收购', '被减持', '被分析', '被入股', '被拟收购']\nsentence：{}\nentity：{}，{}\nrelation：\n".format(text,entity1,entity2)
    #print(prompt)
    ChatGPT_result = chatGPT_runse(prompt,text)
    ChatGPT_result.replace('\n','')
    data_['predict']  = ChatGPT_result
    wrete_file.write(str(data_)+'\n')
