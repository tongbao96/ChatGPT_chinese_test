#{'text': '鱼米之乡(岷江、沱江、青衣江均在犍为郡)、佳茗之乡、美酒之乡(今酒城、酒都、茅台等均属犍为郡)、丝绸之乡、旅游之乡(峨眉山、瓦屋山、彭祖山等山川均在犍为郡)\n', 'predict': '鱼米之乡, 岷江、沱江、青衣江, Located\n佳茗之乡, 0\n美酒之乡, 酒城、酒都、茅台, Located\n丝绸之乡, 0\n旅游之乡, 峨眉山、瓦屋山、彭祖山, Located'}
#{'text': '时，他会拿个弹弓比划比划;拿根树枝转转悠悠;再就是给那墩从周继和家要来的、栽在矮墙南头的蝎子草\n', 'predict': '0'}
#{'text': '<N>作业区<N>队<N>组组长罗恒，是一位在抗美援朝战场入党的转业军人，吃饭总是让组员们吃在前头\n', 'predict': '(罗恒,作业区队组长,Ownership)'}
#{'text': '一个阿姨介绍用一种水鸟(当地叫翠鸟)的唾液蒸蛋能治气管炎的偏方\n', 'predict': '(阿姨, 偏方, Create)\n(水鸟, 唾液, Use)\n(唾液, 蒸蛋, Use)\n(气管炎, 偏方, General-Special)'}

count_0 = 0
TP = 0
FP = 0
FN = 0


with open('one_shot.txt', 'r',encoding='utf-8') as f1, open('../data/test_main.txt', 'r',encoding='utf-8') as f2:
#with open('1.txt', 'r',encoding='utf-8') as f1, open('2.txt', 'r',encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    R = ['unknown', '注资', '拥有', '纠纷', '自己', '增持', '重组', '买资', '签约', '持股', '交易', '入股', '转让', '成立', '分析', '合作', '帮助', '发行', '商讨', '合并', '竞争', '订单', '减持', '合资', '收购', '借壳', '欠款', '被发行', '被转让', '被成立', '被注资', '被持股', '被拥有', '被收购', '被帮助', '被借壳', '被买资', '被欠款', '被增持', '拟收购', '被减持', '被分析', '被入股', '被拟收购']

    for i in range(len(lines1)):
        flag = []

        if 'relation' in eval(lines1[i])['predict']:
            print(eval(lines1[i])['predict'])
            result = eval(lines1[i])['predict'].split('relation')[1].split('，')
            for tag in R:
                if tag in result:
                    flag.append(tag)
        else:
            result = eval(lines1[i])['predict']
            for tag in R:
                if tag in result:
                    flag.append(tag)

        true = lines2[i].split('	')
        entity1 = true[0]
        entity2 = true[1]
        relation= true[2]


        Tp = 0
        Fp = 0
        Fn = 0
        print(flag)
        print(relation)

        if len(flag) == 0:
            if relation == 'unknown':
                Tp += 1
            else:
                Fp += 1
                Fn += 1

        if len(flag)>1:
            if relation in flag:
                Tp+=1
            else:
                Fp+=len(flag)
                Fn+=1

        if len(flag) == 1:
            if flag[0]==relation:
                Tp+=1
            else:
                Fp +=1
                Fn += 1

        TP += Tp
        FP += Fp
        FN += Fn


print(TP,FP,FN)
presion = TP/(TP+FP)
recall = TP/(TP+FN)
F1 = 2*presion*recall/(presion+recall)
print(presion,recall,F1)

#265 484 735
#276 609 724

# 351 255 193
# 0.5792079207920792 0.6452205882352942 0.6104347826086958