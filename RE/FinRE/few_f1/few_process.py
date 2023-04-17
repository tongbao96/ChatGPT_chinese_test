# -*- coding: utf-8 -*-
from chatGPT import chatGPT_runse

count= 0
read_file = open('../data/test.txt','r',encoding='utf-8')
wrete_file = open('few_shot.txt','a',encoding='utf-8')
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
    prompt = "relation tags：['unknown', '注资', '拥有', '纠纷', '自己', '增持', '重组', '买资', '签约', '持股', '交易', '入股', '转让', '成立', '分析', '合作', '帮助', '发行', '商讨', '合并', '竞争', '订单', '减持', '合资', '收购', '借壳', '欠款', '被发行', '被转让', '被成立', '被注资', '被持股', '被拥有', '被收购', '被帮助', '被借壳', '被买资', '被欠款', '被增持', '拟收购', '被减持', '被分析', '被入股', '被拟收购']\nsentence：国信证券分析师王继林在其研报中指出,平安的股价上涨几乎全依赖于其良好的业绩驱动。\nentity：平安，国信证券\nrelation：被分析\nsentence：而在<N>年时,蔡希有担任中石化股份公司的全资子公司——中国国际石油化工联合有限责任公司的总经理,\nentity：中石化股份公司，中国国际石油化工联合有限责任公司\nrelation：拥有\nsentence：华润强势联姻乐购整合待考验\nentity：华润，乐购\nrelation：合作\nsentence：中兴通讯应诉爱立信IPR专利诉讼\nentity：中兴通讯，爱立信\nrelation：纠纷\nsentence：和讯网消息<N>月<N>日,振华重工发布公告称,公司与PetrofacLimited在<N>年<N>月<N>日签订了《铺管船建造及销售合同》,\nentity：PetrofacLimited，振华重工\nrelation：签约\nsentence：<N>年<N>月<N>日,中核集团与中国国电集团共同出资建立中核国电漳州能源有限公司,\nentity：中核集团，中国国电集团\nrelation：合资\nsentence：{}\nentity：{}，{}\nrelation：\n".format(text,entity1,entity2)
    #print(prompt)
    ChatGPT_result = chatGPT_runse(prompt,text)
    ChatGPT_result.replace('\n','')
    data_['predict']  = ChatGPT_result
    wrete_file.write(str(data_)+'\n')
