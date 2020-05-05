import logging
import sys

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:日志记录
"""

# 加入日志
# 获取logger实例
logger = logging.getLogger("baseSpider")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("/autotesting/src/Server/Logs/operation_database.log",encoding="utf-8")  #log存放目录及文件名
file_handler.setFormatter(formatter)

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)