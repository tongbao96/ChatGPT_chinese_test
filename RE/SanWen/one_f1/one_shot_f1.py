TP = 0
FP = 0
FN = 0

with open('one_shot2.txt', 'r',encoding='utf-8') as f1, open('../data/SanWen_main.txt', 'r',encoding='utf-8') as f2:
#with open('1.txt', 'r',encoding='utf-8') as f1, open('2.txt', 'r',encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    R = ['unknown', 'Create', 'Use', 'Near', 'Social', 'Located', 'Owership', 'General-Spicial', 'Family','Part-Whole']

    for i in range(len(lines1)):
        flag = []
        result = eval(lines1[i])['predict']
        result = result.replace('Unknow','unknow')

        for tag in R:
            if tag in result:
                flag.append(tag)

        true = lines2[i].split('	')
        relation= true[2]
        print(flag,relation)

        Tp = 0
        Fp = 0
        Fn = 0

        if len(flag) == 0:
            Fp += 1
            Fn += 1

        if len(flag) == 1:
            if flag[0]==relation:
                Tp+=1
            else:
                Fp+=1
                Fn+=1

        if len(flag)>1:
            if relation in flag:
                Tp+=1
                Fp=len(flag)-1

            else:
                Fp+=len(flag)
                Fn+=1

        TP += Tp
        FP += Fp
        FN += Fn

print(TP,FP,FN)
presion = TP/(TP+FP)
recall = TP/(TP+FN)
F1 = 2*presion*recall/(presion+recall)
print(presion,recall,F1)

