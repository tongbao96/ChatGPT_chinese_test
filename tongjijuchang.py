
count = 0
with open('./ChatGPT_test_result/resume_chatgpt_1000.txt', 'r',encoding='utf-8') as f1:
#with open('../1.txt', 'r',encoding='utf-8') as f1, open('../2.txt', 'r',encoding='utf-8') as f2:
    lines1 = f1.readlines()
    for i in range(len(lines1)):
        num = len(eval(lines1[i])['text'])
        count+=num
    print(count)

    print(count / len(lines1))

