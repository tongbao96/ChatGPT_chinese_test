from chatGPT import  chatGPT_runse

read_file  = open('1.txt','r',encoding='utf-8')
write_file = open('chatgpt_elements_500.txt','a',encoding='utf-8')
for nx,data in enumerate(read_file.readlines()):
    dict_ = {}
    dict_data = eval(data)
    text = dict_data['content']
    print(nx)
    dict_['content'] = text

    if '破产清算' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的公司名称、公告时间、公司行业、裁定时间、受理法院\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_tpe'] = '破产清算'

    if '安全事故' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的公司名称、公告时间、损失金额、伤亡人数、其他影响\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '安全事故'

    if '股东减持' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的减持金额、减持的股东、减持开始日期\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '股东减持'

    if '股权质押' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的质押方、接收方、质押金额、质押开始日期、质押结束日期\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '股权质押'

    if '股东增持' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的增持金额、增持的股东、增持开始日期\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '股东增持'

    if '股权冻结' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的冻结金额、被冻结股东、冻结开始日期、冻结结束日期、被冻结股东\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '股权冻结'

    if '高层死亡' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的公司名称、高层人员、高层职务、死亡/失联时间、死亡年龄\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '高层死亡'

    if '资产损失' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的公司名称、公告时间、损失金额、其他损失\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '资产损失'

    if '对外赔付' == dict_data['event_type']:
        prompt = '请按行给出以下文本中的公司名称、赔付对象、公告时间、赔付金额\n'
        result = chatGPT_runse(prompt, text)
        dict_['events'] = result
        dict_['event_type'] = '对外赔付'


    write_file.write(str(dict_)+'\n')


# {'破产清算': [{'公司名称', '公告时间', '公司行业', '裁定时间', '受理法院'}],
#  '安全事故': [{'公司名称',  '公告时间', '损失金额',  '伤亡人数', '其他影响'}],
#  '股东减持': [ {'减持金额', '减持的股东',  '减持开始日期'}],
#  '股权质押': [{ '质押开始日期', '质押方', '接收方', '质押金额', '质押结束日期', }],
#  '股东增持': [{'增持金额',  '增持的股东', '增持开始日期',}],
#  '股权冻结': [{'冻结开始日期',  '冻结结束日期', '冻结金额',  '被冻结股东'}],
#  '高层死亡': [{'公司名称',  '高层职务', '死亡/失联时间', '死亡年龄',  '高层人员'}],
#  '资产损失': [{'公司名称', '公告时间', '损失金额',  '其他损失'}],
#  '对外赔付': [{'赔付对象', '公司名称', '公告时间', '赔付金额',}]}
#
# read_file  = open('event_element_all_data.txt','r',encoding='utf-8')
# result = {}
# final_result={}
# for nx,data in enumerate(read_file.readlines()):
#
#     dict_data = eval(data)
#     text = dict_data['content']
#     #"events": [{"event_id": "4664588", "公司名称": "湖北银丰棉花股份有限公司", "公告时间": "2016年6月8日", "event_type": "重大资产损失"}]}
#     events = dict_data['events']
#     for i in events:
#
#         events_type = i['event_type']
#         if events_type not in result.keys():
#              result[events_type]=[*i]
#         else:
#             for x in [*i]:
#                 result[events_type].append(x)
# print(result)
# for key,value in result.items():
#     #print(value)
#     final_result[key] =[set(value)]
# print(final_result)

