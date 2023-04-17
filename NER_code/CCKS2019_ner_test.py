from chatGPT import  chatGPT_runse

read_file  = open('../NER_test_data/CCKS2019_shuffle_1000.txt','r',encoding='utf-8')
write_file = open('../ChatGPT_test_result/CCKS2019_chatgpt_1000.txt','a',encoding='utf-8')
for nx,data in enumerate(read_file.readlines()):
    dict_ = {}
    dict_data = eval(data)
    text = dict_data['text']
    result = chatGPT_runse(text)
    print(nx)
    dict_['text'] = text
    dict_['entities'] = result
    write_file.write(str(dict_)+'\n')