import random

# 定义要读取的文件名和写入的文件名
filename = 'test.txt'
output_filename = 'SanWen.txt'

# 打开输入文件和输出文件
with open(filename, 'r',encoding='utf-8') as file, open(output_filename, 'w',encoding='utf-8') as output_file:
    # 读取输入文件的每一行
    lines = file.readlines()
    # 打乱每一行的顺序
    random.shuffle(lines)
    # 将打乱顺序后的每一行写入输出文件
    for line in lines:
        output_file.write(line)