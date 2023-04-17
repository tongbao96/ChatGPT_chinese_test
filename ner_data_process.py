
#text = "在过去的五年中，致公党在邓小平理论指引下，遵循社会主义初级阶段的基本路线，努力实践致公党十大提出的发挥参政党职能、加强自身建设的基本任务。"
#labels = ["O", "O", "O", "O", "O", "O", "O", "O", "B-ORG", "I-ORG", "I-ORG", "O", "B-PER", "I-PER", "I-PER", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORG", "I-ORG", "I-ORG", "I-ORG", "I-ORG", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
import json

read_file = open('./WeiboNER.json','r',encoding='utf-8')
write_file = open('./output.txt','a',encoding='utf-8')
for json_str in read_file.readlines():
    result = {}
    data = json.loads(json_str)
    text = data['text']
    labels = data['lable']
    entities = []
    current_entity = ""
    current_label = ""
    for i in range(len(text)):
        if labels[i].startswith("B-"):
            # 新的实体开始
            current_entity = text[i]
            current_label = labels[i][2:]
        elif labels[i].startswith("I-"):
            # 实体继续
            current_entity += text[i]
        elif labels[i] == "O" and current_entity:
            # 实体结束
            entities.append((current_entity, current_label))
            current_entity = ""
            current_label = ""

    if current_entity:
        # 如果最后一个字符是实体，需要将其加入列表
        entities.append((current_entity, current_label))
    if len(entities)>0:
        result['text'] = text
        result['entities']=entities
        write_file.write(str(result)+'\n')

#[('致公党', 'ORG'), ('邓小平', 'PER'), ('致公党十大', 'ORG')]
