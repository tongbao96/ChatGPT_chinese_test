from chatGPT import chatGPT_runse

count= 0
read_file = open('SanWen.txt','r',encoding='utf-8')
write_file = open('few_shot.txt','a',encoding='utf-8')
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
    prompt = "关系：['Unknown', 'Create', 'Use', 'Near', 'Social', 'Located', 'Owership', 'General-Spicial', 'Family', 'Part-Whole']\n样例：我伸出手去\n实体：我，手\n输出：(我，手，Part-Whole)\n样例：" + text +'\n实体：{}，{}\n'.format(entity1,entity2)+ "输出：\n"
    ChatGPT_result = chatGPT_runse(prompt,text)
    ChatGPT_result.replace('\n','')
    data_['predict']  = ChatGPT_result
    write_file.write(str(data_)+'\n')
