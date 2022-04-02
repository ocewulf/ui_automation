#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/3/21 17:40 
"""
import os
import yaml

from config import BASE_PATH


def read_file(filename):
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename
    arr = []
    # 加载并读取文件流
    with open(filepath, "r", encoding="utf-8") as f:
        # 遍历调用yaml.safe_load(f).values()方法，取得values
        for data in yaml.safe_load(f).values():
            # 将获取的values添加到列表中,然后转换为符合条件格式的列表嵌套tuple格式
            arr.append(tuple(data.values()))
    return arr


if __name__ == '__main__':
    print(read_file("login.yaml"))
