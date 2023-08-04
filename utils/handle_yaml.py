"""
=========================
Time    : 2023/8/3 13:58
Author  : Rowrey
Email   : ll1106@163.com
File    : handle_yaml.py
=========================
"""
import yaml


def get_yaml_data(fileDir):
    with open(fileDir,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())
