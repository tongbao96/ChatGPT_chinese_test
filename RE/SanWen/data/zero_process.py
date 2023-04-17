from chatGPT import chatGPT_runse

count= 0
read_file = open('SanWen.txt','r',encoding='utf-8')
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
    prompt = "关系：['Unknown', 'Create', 'Use', 'Near', 'Social', 'Located', 'Owership', 'General-Spicial', 'Family', 'Part-Whole']\n句子：" + text +'\n'+ "请找出句子中的'{}'和'{}'属于哪种关系，只需回答关系名".format(entity1,entity2)
    ChatGPT_result = chatGPT_runse(prompt,text)
    ChatGPT_result.replace('\n','')
    data_['predict']  = ChatGPT_result
    wrete_file.write(str(data_)+'\n')
