from chatGPT import chatGPT_runse

count= 0
read_file = open('../data/SanWen.txt','r',encoding='utf-8')
wrete_file = open('zero_shot2.txt','a',encoding='utf-8')
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
    prompt = "relation：['Unknown', 'Create', 'Use', 'Near', 'Social', 'Located', 'Owership', 'General-Spicial', 'Family', 'Part-Whole']\nsentence：{}\nentity：{}，{}\nrelation：\n".format(text,entity1,entity2)
    #print(prompt)
    ChatGPT_result = chatGPT_runse(prompt,text)
    ChatGPT_result.replace('\n','')
    data_['predict']  = ChatGPT_result
    wrete_file.write(str(data_)+'\n')
