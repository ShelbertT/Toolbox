# All functions that include manipulating the files are stored here
# 所有涉及到对文件进行操作的功能都在这

import os
import re
import csv
import json

g_path = 'E:\\database\\BaiduIndex\\2011\\word1\\[北京空气质量],(2011-01-01至2011-12-31),0.csv'  # 文件夹总路径


def one_line_tools(path):
    file_list = os.listdir(path)  # path -> list[str] | 返回当前目录下所有文件与文件夹名，包括后缀。不会进入下级目录
    info_list = re.split(r'[\[\],().]', path)  # 用中括号里面的内容去做切分字符串
    return file_list, info_list


def create_path(path):  # path -> action | 使用绝对路径进行路径创建
    path = path.strip()
    path = path.rstrip("\\")
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    else:
        return


# CSV------------------------------------------------------------------------------------------------------------------
def read_csv(input_path):  # path -> list[list[str]] | 输入文件路径，返回存储csv的二维列表，索引顺序：index[row][col]
    data = []
    with open(input_path, 'r') as f:
        csv_reader = csv.reader(f)  # 用reader是为了防止空行的出现
        for row in csv_reader:
            data.append(row)

    return data


def write_csv(data, output_path='test.csv'):  # list[list[]] -> .csv | 输入一个二维列表，生成其csv文件在output_path
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


# JSON------------------------------------------------------------------------------------------------------------------
def write_json(data, output_path='test.json'):  # dict -> json | 把字典写入本地json文件
    with open(output_path, "w", encoding='utf-8') as f:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(data, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行




# if __name__ == '__main__':
#     g_data = read_csv(g_path)
#     transpose_matrix(g_data)
#     # write_csv('E:\\test.csv', g_data)