import os,sys

"""
    @Author:alex-jiang
    @CreateTime: 2020/4/28
    @UpdateTime:
    @model:一键装包和建表
"""

os.system("python install -r requirement.txt - i https://pypi.douban.com/simple ")
os.system("python createSql.py")