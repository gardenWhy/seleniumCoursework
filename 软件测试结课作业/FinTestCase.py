import unittest

from MyPackage.finTest import Fin


class Test(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("byte")

    # 正确登录的 测试用例
    def test_001(self):
        lg = Fin()
        lg.login("wewopa", "123456")
        # 获取登录后  上边的显示的用户名
        data = lg.get_text("class", "right_header")
        # 断言 判断登录之后的用户名 是否和预期的用户名相同
        self.assertEqual('Welcome 曹文杰 | Logout', data, msg="登录未成功")
        lg.driver.close()

    def test_002(self):
        od = Fin()
        od.login("wewopa", "123456")
        od.order()
        od.driver.switch_to.frame("mainiFrame")
        data1 = od.get_text("xpath", "/html/body/div")
        self.assertEqual('添加订单成功', data1, msg="订单未成功下单")
        od.driver.close()

    def test_003(self):
        search = Fin()
        search.login("wewopa", "123456")
        search.search()
        search.driver.switch_to.frame("mainiFrame")
        data2 = search.get_text("xpath", "/html/body/form/table/tbody/tr[3]/td/strong")
        self.assertEqual('银月城', data2, msg="查询库存未成功")
        search.driver.close()

    def test_004(self):
        delete = Fin()
        delete.login("wewopa", "123456")
        data1 = delete.delete()
        delete.driver.switch_to.frame('mainiFrame')
        data2 = delete.get_text('xpath', '/html/body/table/tbody/tr[4]/td[1]')
        self.assertNotEqual(data1, data2, msg='删除操作出现了意想不到的事情')
        delete.driver.close()

    def test_005(self):
        add = Fin()
        add.login("wewopa", "123456")
        add.add('张三', '1234568', '北京', '1500')
        add.driver.switch_to.frame('mainiFrame')
        data = add.get_text('css', 'body')
        self.assertEqual('成功', data, msg='添加失败')
        add.driver.close()


if __name__ == '__main__':
    unittest.main()
