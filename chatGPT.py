#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time：2023/3/3 19:27
# @Author：BaoTong
import openai

def create_chat(message):
    '''
    :param message: 传递给chatGPT的参数列表
    :return:
    '''
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=message,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response

def chatGPT_input(prompt,text):
    '''
    :param text: 输入测试提示，文本内容
    :return:ChatGPT输出结果
    '''
    openai.api_key = "your keys"
    messages = [
        {'role': 'user',
         'content': 'You are my Chat assistant!'}]
   # prompt_learning = "请给出句子中的人名、地名、机构名："
    content = prompt + text
    messages.append(
        {"role": "user", "content": content},
    )
    response = create_chat(messages)
    text = response['choices'][0]['message']['content'].strip('\n')
    return text

#
