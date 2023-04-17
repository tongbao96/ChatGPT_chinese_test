# count = 0
# s1=[]
# s2=[]
# with open('chatgpt_class_500.txt','r',encoding='utf-8') as f1:
#     lines1 = f1.readlines()
#     for line in lines1:
#         t = eval(line)
#         event1 = t['event_type']
#         s1.append(event1)
#
#
# with open('event_element_label_500_main.txt', 'r', encoding='utf-8') as f2:
#     lines2 = f2.readlines()
#     for line in lines2:
#         m = eval(line)
#         event2 = m['events'][0]['event_type'].replace('重大','')
#         s2.append(event2)
#
# for i in range(len(s1)):
#     if s1[i] == s2[i]:
#         count += 1
#
# print(count)
# print(s1)
# print(s2)
#

count = 0
with open('chatgpt_class_500.txt','r',encoding='utf-8') as f1:
    lines1 = f1.readlines()
    for line in lines1:
        t = eval(line)
        text = t['content']
        count+=len(text)
print(count/500)
