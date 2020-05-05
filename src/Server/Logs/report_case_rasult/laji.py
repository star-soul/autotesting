# now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
# filename = "/autotesting/src/Server/Logs/report_case_rasult/" + now + "_result.html"
# fp = open(filename, 'wb')
#
# runner = HTMLTestRunner.HTMLTestRunner(
#     stream=fp,
#     title=u'搜索功能测试报告',
#     description=u'用例执行情况：')
#
# runner.run(testFile().test_Execute_Request())
#
# # 关闭文件流，不关的话生成的报告是空的
# fp.close()