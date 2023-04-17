# with open("./test.char(1).bio", "r",encoding='utf-8') as f:
#     lines = f.readlines()
#
#     data = []
#     sentence = ""
#     labels = ""
#     for line in lines:
#         line = line.strip()
#         if not line:
#             if sentence and labels:
#                 data.append((sentence, labels))
#                 sentence = ""
#                 labels = ""
#         else:
#             word, label = line.split()
#             sentence += word + " "
#             labels += label + " "
#
#     if sentence and labels:
#         data.append((sentence.strip(), labels.strip()))
#
# with open("output.txt", "a",encoding='utf-8') as f:
#     for sentence, labels in data:
#         f.write( "".join(sentence.split()) + "\t" + labels+ "\n")


file =  open("./MSRA.json", "a",encoding='utf-8')

import json
with open("output.txt", "r",encoding='utf-8') as f:
    for sentence in f.readlines():

        data = {}
        words_labels = sentence.split("\t")
        words = words_labels[0].split(" ")
        labels = words_labels[1].split(" ")[:-1]

        data["text"]  = words[0]
        data["lable"]   = labels
        data = json.dumps(data,ensure_ascii=False)
        file.write(data+'\n')


