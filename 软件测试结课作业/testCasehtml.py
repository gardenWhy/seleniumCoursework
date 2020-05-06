import unittest

from MyPackage.FinTestCase import Test
# 帮助我们生成网页版报告
from MyPackage.HTMLTestRunner import HTMLTestRunner


class Test_runner(unittest.TestCase):
    def test_suit(self):
        # 创建一个测试套件
        mysuit = unittest.TestSuite()
        # 向测试套机中添加 测试用例的数组
        case_list = ['test_001', 'test_002', 'test_003', 'test_004', 'test_005']
        for case in case_list:
            mysuit.addTest(Test(case))
        # 生成 html格式的文档
        with open('report.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,  # 指定测试数据 写入到哪个文件
                title='后台进销平台测试',
                description='测试登陆、下单、查询、删除',  # 设定描述
                verbosity=2
            ).run(mysuit)


if __name__ == '__main__':
    unittest.main()
