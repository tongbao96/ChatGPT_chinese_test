# -*- coding: utf-8 -*-
from chatGPT import chatGPT_runse

count= 0
read_file = open('../data/SanWen.txt','r',encoding='utf-8')
write_file = open('few_shot_2.txt','a',encoding='utf-8')
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
    prompt = "relation tags:['Unknown', 'Create', 'Use', 'Near', 'Social', 'Located', 'Owership', 'General-Spicial', 'Family', 'Part-Whole']\nsentence:我伸出手去\nentity:我，手\nrelation:Part-Whole\nsentence:现在的后门山更是常年树木葱翠、鸟语花香\nentity:后门山，树木\nrelation:Located\nsentence:" + text +'\nentity:{}，{}\nrelation:\n'.format(entity1,entity2)
    #print(prompt)
    ChatGPT_result = chatGPT_runse(prompt,text)
    ChatGPT_result.replace('\n','')
    data_['predict']  = ChatGPT_result
    data_['prompt'] = prompt
    write_file.write(str(data_)+'\n')
