
TP = 0
FP = 0
FN = 0
chatgpt_count = 0
true_count = 0
with open('chatgpt_elements_500.txt', 'r',encoding='utf-8') as f1, open('event_element_label_500_main.txt', 'r',encoding='utf-8') as f2:
#with open('1.txt', 'r',encoding='utf-8') as f1, open('2.txt', 'r',encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    if len(lines1)!=len(lines2):
        print('文件行数不相等')
    else:
        for i in range(len(lines1)):
            text1 = eval(lines1[i])['content']
            text2 = eval(lines2[i])['content']

            chatgpt = eval(lines1[i])
            true = eval(lines2[i])['events']

            for t in range(min(len(text1), len(text2))):
                if text1[t] != text2[t]:
                    print(f"Line {t + 1} is different.")
                    continue
                    ## {'破产清算': [{'公司名称', '公告时间', '公司行业', '裁定时间', '受理法院'}],
                    ##  '重大安全事故': [{'公司名称',  '公告时间', '损失金额',  '伤亡人数', '其他影响'}],
                    ##  '股东减持': [ {'减持金额', '减持的股东',  '减持开始日期'}],
                    ##  '股权质押': [{ '质押开始日期', '质押方', '接收方', '质押金额', '质押结束日期', }],
                    #  '股东增持': [{'增持金额',  '增持的股东', '增持开始日期',}],
                    ##  '股权冻结': [{'冻结开始日期',  '冻结结束日期', '冻结金额',  '被冻结股东'}],
                    ##  '高层死亡': [{'公司名称',  '高层职务', '死亡/失联时间', '死亡年龄',  '高层人员'}],
                    ##  '重大资产损失': [{'公司名称', '公告时间', '损失金额',  '其他损失'}],
                    ##  '对外赔付': [{'赔付对象', '公司名称', '公告时间', '赔付金额',}]}
            #print()
# 'events': '公司名称：东华软件股份公司\n高层人员：黄杏国先生\n高层职务：副总经理\n死亡/失联时间：近日（公告发布时间为2015年3月3日）\n死亡年龄：101岁', 'event_type': '高层死亡'}
#'events': '公司名称：福安药业（集团）股份有限公司\n告时间：2014年7月17日\n损失金额：未提及\n伤亡人数：未提及\n其他影响：未提及', 'event_type': '安全事故'}

            #如果事件类型不一致 直接判错  根据true已有的标签判错
            if chatgpt['event_type']!=true[0]['event_type'].replace('重大',''):
                print(chatgpt_count)
                print('事件类型不一致')

                true[0]['事件类型'] = true[0].pop('event_type').replace('重大','')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                true = set(filter(lambda x: x[0] != '', true))
                true = set(true)
                Tp = 0
                Fp = len(true)
                Fn = len(true)

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn

                continue

            if  chatgpt['event_type']  == '高层死亡':

                company_name = chatgpt['events'].split('公司名称：')[1].split('\n')[0]
                renyuan = chatgpt['events'].split('高层人员：')[1].split('\n')[0]
                zhiwu = chatgpt['events'].split('高层职务：')[1].split('\n')[0]
                time = chatgpt['events'].split('死亡/失联时间：')[1].split('\n')[0]
                nianling = chatgpt['events'].split('死亡年龄：')[1].split('\n')[0]

                company_name = company_name.replace('。', '')
                renyuan = renyuan.replace('。', '')
                zhiwu = zhiwu.replace('。', '')
                time = time.replace('。', '')
                nianling = nianling.replace('。', '')

                company_name = company_name.split('、')
                renyuan = renyuan.split('、')
                zhiwu = zhiwu.split('、')
                time = time.split('、')
                nianling = nianling.split('、')

                event_type = [('高层死亡','事件类型')]
                predict_company_name = [(s, '公司名称') for s in company_name]
                predict_renyuan = [(s, '高层人员') for s in renyuan]
                predict_zhiwu = [(s, '高层职务') for s in zhiwu]
                predict_time = [(s, '死亡/失联时间') for s in time]
                predict_nianling = [(s, '死亡年龄') for s in nianling]
                final_label = set(predict_company_name + predict_renyuan + predict_zhiwu + predict_time + predict_nianling + event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))

                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                print(true)

                true = [(v, k) for k, v in true[0].items()]
                true = set(filter(lambda x: x[0] != '', true))
                true = set(true)

                Tp=0
                for p in final_label:
                        # 遍历真实实体
                        for t in true:
                            # 判断真实实体是否被预测为实体
                            if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                                Tp += 1
                                break

                Fp = len(final_label)-Tp
                Fn = len(true)- Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)
                TP += Tp
                FP += Fp
                FN += Fn


        #   # {'破产清算': [{'公司名称', '公告时间', '公司行业', '裁定时间', '受理法院'}],
# 'events': '公司名称：长岭（集团）股份有限公司\n公告时间：2009年1月19日\n公司行业：未提及\n裁定时间：[2007]宝市中法破字第14-14号\n受理法院：宝鸡市中级人民法院', 'event_tpe': '破产清算'}
# "events": [{"event_id": "4328485", "受理法院": "宝鸡市中级人民法院", "公司名称": "长岭（集团）股份有限公司", "公告时间": "二〇〇九年一月十九日","event_type": "破产清算"}]}
            if  chatgpt['event_type']  == '破产清算':

                company_name = chatgpt['events'].split('公司名称：')[1].split('\n')[0]
                gonggaotime = chatgpt['events'].split('公告时间：')[1].split('\n')[0]
                hanggye = chatgpt['events'].split('公司行业：')[1].split('\n')[0]
                caidingtime = chatgpt['events'].split('裁定时间：')[1].split('\n')[0]
                fayuan = chatgpt['events'].split('受理法院：')[1].split('\n')[0]

                company_name = company_name.replace('。', '')
                gonggaotime = gonggaotime.replace('。', '')
                hanggye = hanggye.replace('。', '')
                caidingtime = caidingtime.replace('。', '')
                fayuan = fayuan.replace('。', '')

                company_name = company_name.split('、')
                gonggaotime = gonggaotime.split('、')
                hanggye = hanggye.split('、')
                caidingtime = caidingtime.split('、')
                fayuan = fayuan.split('、')

                event_type = [('破产清算','事件类型')]
                predict_company_name = [(s, '公司名称') for s in company_name]
                predict_gonggaotime = [(s, '公告时间') for s in gonggaotime]
                predict_hanggye = [(s, '公司行业') for s in hanggye]
                predict_caidingtime = [(s, '裁定时间') for s in caidingtime]
                predict_fayuan = [(s, '受理法院') for s in fayuan]

                final_label = set(predict_company_name + predict_gonggaotime + predict_hanggye + predict_caidingtime + predict_fayuan +event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))


                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                #true = set(filter(lambda x: x[0] != '', true))
                true = set(true)
                print(true)

                Tp=0
                for p in final_label:
                    # 遍历真实实体
                    for t in true:
                        # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                            Tp += 1
                            break

                Fp = len(final_label)-Tp
                Fn = len(true)- Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn


            ##  '安全事故': [{'公司名称',  '公告时间', '损失金额',  '伤亡人数', '其他影响'}],
          # { 'events': '公司名称：云南博闻科技实业股份有限公司\n公告时间：2008年9月1日\n损失金额：未造成公司资产损失\n伤亡人数：未提及\n其他影响：未对公司生产经营产生不良影响','event_type': '安全事故'}

            if  chatgpt['event_type']  == '安全事故':
                print(chatgpt)
                print('qqqqqqqqqqqqqqqqqqq')
                company_name = chatgpt['events'].split('公司名称：')[1].split('\n')[0]
                gonggaotime = chatgpt['events'].split('公告时间：')[1].split('\n')[0]
                money = chatgpt['events'].split('损失金额：')[1].split('\n')[0]
                die = chatgpt['events'].split('伤亡人数：')[1].split('\n')[0]
                other = chatgpt['events'].split('其他影响：')[1].split('\n')[0]

                company_name = company_name.replace('。', '')
                gonggaotime = gonggaotime.replace('。', '')
                money = money.replace('。', '')
                die = die.replace('。', '')
                other = other.replace('。', '')

                company_name = company_name.split('、')
                gonggaotime = gonggaotime.split('、')
                money = money.split('、')
                die = die.split('、')
                other = other.split('、')

                event_type = [('重大安全事故','事件类型')]
                predict_company_name = [(s, '公司名称') for s in company_name]
                predict_gonggaotime = [(s, '公告时间') for s in gonggaotime]
                predict_money = [(s, '损失金额') for s in money]
                predict_die = [(s, '伤亡人数') for s in die]
                predict_other = [(s, '其他影响') for s in other]

                final_label = set(predict_company_name + predict_gonggaotime + predict_money + predict_die + predict_other + event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))


                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                #true = set(filter(lambda x: x[0] != '', true))
                true = set(true)

                Tp = 0
                for p in final_label:
                    # 遍历真实实体
                    for t in true:
                        # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                            Tp += 1
                            break

                Fp = len(final_label) - Tp
                Tp = len(final_label & true)
                Fp = len(final_label)-Tp
                Fn = len(true)- Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn


            ##  '重大资产损失': [{'公司名称', '公告时间', '损失金额',  '其他损失'}],
            #'events': '公司名称：湖南郴电国际发展股份有限公司\n公告时间：2006年7月18日\n损失金额：具体损失正在核实当中，未给出具体数字\n其他损失：部分供电设施遭到破坏，对公司的生产经营有较大影响。', 'event_type': '资产损失'}
            if chatgpt['event_type'] == '资产损失':
                company_name = chatgpt['events'].split('公司名称：')[1].split('\n')[0]
                gonggaotime = chatgpt['events'].split('公告时间：')[1].split('\n')[0]
                money = chatgpt['events'].split('损失金额：')[1].split('\n')[0]
                other = chatgpt['events'].split('其他损失：')[1].split('\n')[0]

                company_name = company_name.replace('。', '')
                gonggaotime = gonggaotime.replace('。', '')
                money = money.replace('。', '')
                other = other.replace('。', '')

                company_name = company_name.split('、')
                gonggaotime = gonggaotime.split('、')
                money = money.split('、')
                other = other.split('、')

                event_type = [('重大资产损失', '事件类型')]
                predict_company_name = [(s, '公司名称') for s in company_name]
                predict_gonggaotime = [(s, '公告时间') for s in gonggaotime]
                predict_money = [(s, '损失金额') for s in money]
                predict_other = [(s, '其他损失') for s in other]

                final_label = set(
                    predict_company_name + predict_gonggaotime + predict_money + predict_other + event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))


                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                #true = set(filter(lambda x: x[0] != '', true))
                true = set(true)

                Tp = 0
                for p in final_label:
                    # 遍历真实实体
                    for t in true:
                        # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                            Tp += 1
                            break

                Fp = len(final_label) - Tp

                Tp = len(final_label & true)
                Fp = len(final_label) - Tp
                Fn = len(true) - Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn


                ## '股权冻结': [{'冻结开始日期',  '冻结结束日期', '冻结金额',  '被冻结股东'}],
                # 'events': '冻结金额：全部股份\n被冻结股东：湖北江湖生态农业股份有限公司\n冻结开始日期：截止2012年2月16日\n冻结结束日期：2013年2月16日\n被冻结股东：湖北江湖生态农业股份有限公司',

            if chatgpt['event_type'] == '股权冻结':
                dongjienum = chatgpt['events'].split('冻结金额：')[1].split('\n')[0]
                gudong = chatgpt['events'].split('被冻结股东：')[1].split('\n')[0]
                start_time = chatgpt['events'].split('冻结开始日期：')[1].split('\n')[0]
                end_time = chatgpt['events'].split('冻结开始日期：')[1].split('\n')[0]

                dongjienum = dongjienum.replace('。', '')
                gudong = gudong.replace('。', '')
                start_time = start_time.replace('。', '')
                end_time = end_time.replace('。', '')

                dongjienum = dongjienum.split('、')
                gudong = gudong.split('、')
                start_time = start_time.split('、')
                end_time = end_time.split('、')

                event_type = [('股权冻结', '事件类型')]
                predict_dongjienum = [(s, '冻结金额') for s in dongjienum]
                predict_gudong = [(s, '被冻结股东') for s in gudong]
                predict_start_time = [(s, '冻结开始日期') for s in start_time]
                predict_end_time = [(s, '冻结结束日期') for s in end_time]

                final_label = set(predict_dongjienum + predict_gudong + predict_start_time + predict_end_time + event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))


                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                #true = set(filter(lambda x: x[0] != '', true))
                true = set(true)

                Tp = 0
                for p in final_label:
                    # 遍历真实实体
                    for t in true:
                        # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                            Tp += 1
                            break

                Fp = len(final_label) - Tp

                Tp = len(final_label & true)
                Fp = len(final_label) - Tp
                Fn = len(true) - Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn


        ## '股权质押': [{ '质押开始日期', '质押方', '接收方', '质押金额', '质押结束日期', }],
        # 'events': '质押方：王小明先生\n接收方：中信建投证券份有限公司\n质押金额：8310000股\n质押开始日期：未给出\n质押结束日期：36个月后', 'event_type': '股权质押'}
            if chatgpt['event_type'] == '股权质押':
                zhiyafang = chatgpt['events'].split('质押方：')[1].split('\n')[0]
                jieshoufang = chatgpt['events'].split('接收方：')[1].split('\n')[0]
                money = chatgpt['events'].split('质押金额：')[1].split('\n')[0]
                start_time = chatgpt['events'].split('质押开始日期：')[1].split('\n')[0]
                end_time = chatgpt['events'].split('质押结束日期：')[1].split('\n')[0]

                zhiyafang = zhiyafang.replace('。', '')
                jieshoufang = jieshoufang.replace('。', '')
                money = money.replace('。', '')
                start_time = start_time.replace('。', '')
                end_time = end_time.replace('。', '')

                zhiyafang = zhiyafang.split('、')
                jieshoufang = jieshoufang.split('、')
                money = money.split('、')
                start_time = start_time.split('、')
                end_time = end_time.split('、')

                event_type = [('股权质押', '事件类型')]
                predict_zhiyafang = [(s, '质押方') for s in zhiyafang]
                predict_jieshoufang = [(s, '接收方') for s in jieshoufang]
                predict_money = [(s, '质押金额') for s in money]
                predict_start_time = [(s, '质押开始日期') for s in start_time]
                predict_end_time = [(s, '质押结束日期') for s in end_time]

                final_label = set(predict_zhiyafang + predict_jieshoufang + predict_money + predict_start_time + predict_end_time+event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))

                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                #如果lable里没有，应该在chatgpt里也不要有
                #true = set(filter(lambda x: x[0] != '', true))
                true = set(true)

                Tp = 0
                for p in final_label:
                    # 遍历真实实体
                    for t in true:
                        # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                            Tp += 1
                            break

                Fp = len(final_label) - Tp

                Tp = len(final_label & true)
                Fp = len(final_label) - Tp
                Fn = len(true) - Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn


        ##   '对外赔付': [{'赔付对象', '公司名称', '公告时间', '赔付金额',}]}
        # 'events': '公司名称：九芝堂股份有限公司\n赔付对象：公司控股股东的房屋搬迁损失补偿费\n公告时间：2008年12月30日\n赔付金额：未提及具体金额', 'event_type': '对外赔付'}
            if chatgpt['event_type'] == '对外赔付':
                gongsi = chatgpt['events'].split('公司名称：')[1].split('\n')[0]
                duixiang = chatgpt['events'].split('赔付对象：')[1].split('\n')[0]
                shijian = chatgpt['events'].split('公告时间：')[1].split('\n')[0]
                money = chatgpt['events'].split('赔付金额：')[1].split('\n')[0]


                gongsi = gongsi.replace('。', '')
                duixiang = duixiang.replace('。', '')
                money = money.replace('。', '')
                shijian = shijian.replace('。', '')

                gongsi = gongsi.split('、')
                duixiang = duixiang.split('、')
                money = money.split('、')
                shijian = shijian.split('、')

                event_type = [('对外赔付', '事件类型')]
                predict_gongsi = [(s, '公司名称') for s in gongsi]
                predict_duixiang = [(s, '赔付对象') for s in duixiang]
                predict_money = [(s, '赔付金额') for s in money]
                predict_shijian = [(s, '公告时间') for s in shijian]

                final_label = set(predict_gongsi + predict_duixiang + predict_money + predict_shijian+event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))

                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                #如果lable里没有，应该在chatgpt里也不要有
                #true = set(filter(lambda x: x[0] != '', true))
                true = set(true)

                Tp = 0
                for p in final_label:
                    # 遍历真实实体
                    for t in true:
                        # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                            Tp += 1
                            break

                Fp = len(final_label) - Tp

                Tp = len(final_label & true)
                Fp = len(final_label) - Tp
                Fn = len(true) - Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn

            #股东增持 股东减持
            #'events': '减持金额：300万股 * 4.52元/股 = 1356万元\n减持的股东：北京申安联合有限公司\n减持开始日期：2019年3月28日', 'event_type': '股东减持'}
            ##  '股东减持': [ {'减持金额', '减持的股东',  '减持开始日期'}],
            if chatgpt['event_type'] == '股东减持':
                money = chatgpt['events'].split('减持金额：')[1].split('\n')[0]
                duixiang = chatgpt['events'].split('减持的股东：')[1].split('\n')[0]
                shijian = chatgpt['events'].split('减持开始日期：')[1].split('\n')[0]


                duixiang = duixiang.replace('。', '')
                money = money.replace('。', '')
                shijian = shijian.replace('。', '')

                duixiang = duixiang.split('、')
                money = money.split('、')
                shijian = shijian.split('、')

                event_type = [('股东减持', '事件类型')]
                predict_money = [(s, '减持金额') for s in money]
                predict_duixiang = [(s, '减持开始日期') for s in duixiang]
                predict_shijian = [(s, '公告时间') for s in shijian]

                final_label = set(predict_money +predict_duixiang +  predict_shijian + event_type)
                final_label = set(filter(lambda x: x[0] != '无', final_label))
                final_label = set(filter(lambda x: '提及' not in x[0], final_label))
                final_label = set(filter(lambda x: '未知' not in x[0], final_label))

                true[0]['事件类型'] = true[0].pop('event_type')
                del true[0]['event_id']
                true = [(v, k) for k, v in true[0].items()]
                # 如果lable里没有，应该在chatgpt里也不要有
                # true = set(filter(lambda x: x[0] != '', true))
                true = set(true)

                Tp = 0
                for p in final_label:
                    # 遍历真实实体
                    for t in true:
                        # 判断真实实体是否被预测为实体
                        if (t[0] in p[0] or p[0] in t[0]) and t[1] == p[1]:  # 模糊匹配
                            Tp += 1
                            break

                Fp = len(final_label) - Tp

                Tp = len(final_label & true)
                Fp = len(final_label) - Tp
                Fn = len(true) - Tp

                chatgpt_count += list(chatgpt['events']).count('：')
                true_count += len(true)

                TP += Tp
                FP += Fp
                FN += Fn
#

# fp应该减去18  18为标注数据中日期为空的值
# fn也应该减去18
#1011 1463 1039
#0.40864995957962813 0.49317073170731707 0.4469496021220159
FP-=18
FN-=18
print(TP,FP,FN)
pre = TP/(TP+FP)
rec = TP/(TP+FN)
f1 = (2*pre*rec)/(pre+rec)
print(pre,rec,f1)


print(chatgpt_count)
print(true_count)
# 1944 5126 4989
# 0.27496463932107496 0.2803980960623107 0.2776547882596586
# chatgpt 7070
# true 6933