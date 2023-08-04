"""
=========================
Time    : 2023/8/4 14:48
Author  : Rowrey
Email   : ll1106@163.com
File    : handle_path.py
=========================
"""
import os

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#------data路径-------
data_path = os.path.join(project_path,'data')
#------log路径-------
log_path = os.path.join(project_path,'logs')
#------配置路径-------
config_path = os.path.join(project_path,'configs')
#------报告路径-------
report_path = os.path.join(project_path,'report\\tem')
