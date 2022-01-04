# Functions that does not include
# 仅涉及内存数据处理的函数存在这里

def transpose_matrix(data):  # list[list[]] -> list[list[]] 转置列表中存储的矩阵
    new_data = []
    for col_index in range(len(data[0])):
        new_row = []
        for row in data:
            new_row.append(row[col_index])
        new_data.append(new_row)

    return new_data


def de_duplication(data):  # list -> list | 列表去重
    new_data = []
    for i in data:
        if i not in new_data:
            new_data.append(i)

    return new_data