# file = open('relation2id.txt','r',encoding='utf-8')
# result  = []
# for line in file.readlines():
#     relation  = line.split(' ')[0]
#     result.append(relation)
#
# print(result)


with open('test.txt', 'r',encoding='utf-8') as f:
    lines = f.readlines()

with open('test_main.txt', 'w',encoding='utf-8') as f:
    for line in lines:
        if line.strip():
            f.write(line)