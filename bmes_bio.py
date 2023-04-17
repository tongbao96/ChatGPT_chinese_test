f = open("test.char(1).bmes",encoding='utf-8')
sentences = []
sentence = []
label_set=set()
cnt_line=0
for line in f:
    #print(line)
    cnt_line+=1
    if len(line)==0  or line[0]=="\n":
        if len(sentence) > 0:
            sentences.append(sentence)
            #print(sentence)
            sentence = []
        continue
    splits = line.split(' ')
    sentence.append([splits[0],splits[-1][:-1]])
    label_set.add(splits[-1])
    if('\n' not in splits[-1]):
        print(splits[0],splits[-1])
        print(cnt_line)
    #print([splits[0],splits[-1]])

if len(sentence) >0:
    sentences.append(sentence)
    sentence = []


f2=open("test.char(1).bio","w+",encoding="utf-8")
for sen in sentences:
    for word in sen:
        char=word[0]
        label=word[1]
        if(label[0]=='S'):
            label='B'+label[1:]
        elif(label[0]=='E' or label[0]=='M'):
            label='I'+label[1:]
        f2.write(f'{char} {label}\n')
    f2.write('\n')
f2.close()