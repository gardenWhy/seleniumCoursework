import time

from selenium.webdriver.support.select import Select

from MyPackage.MyCommonLib import CommonShare


# 使用老师现有平台进行测试，今日完成
class Fin(CommonShare):
    # 登陆
    def login(self, user, pwd):
        self.open_url("http://wewopa.natapp4.cc/jinxiaocun/")
        self.ActionChain("xpath", "/html/body/div/div[2]/form/table/tbody/tr[2]/td[2]/input", user)
        self.ActionChain("xpath", "/html/body/div/div[2]/form/table/tbody/tr[3]/td[2]/input", pwd)
        self.click("xpath", "/html/body/div/div[2]/form/table/tbody/tr[4]/td/input")
        time.sleep(3)
        data = self.get_text("class", "right_header")
        print(data)
        self.driver.switch_to.default_content()

    # 下单
    def order(self):
        self.driver.switch_to.frame("mainiFrame")
        self.ActionChain("id", 'textfield21', "2020-04-28")
        # self.click("xpath", '//*[@id="dpOkInput"]')
        self.ActionChain("css", "#textfield23", "testtesttest")
        self.ActionChain("xpath", "/html/body/form/table/tbody/tr[4]/td[4]/input", "123")
        self.ActionChain("xpath", "/html/body/form/table/tbody/tr[5]/td[4]/input", "456")
        self.ActionChain("xpath", "/html/body/form/table/tbody/tr[6]/td[4]/input", "789")
        self.click("id", 'button')
        print(self.get_text("css", "body > div:nth-child(1)"))
        self.driver.switch_to.default_content()

    # 库存查询
    def search(self):
        self.click("xpath", '/html/body/div[1]/div[2]/div[1]/ul/li[3]/a')
        self.driver.switch_to.frame("mainiFrame")
        s1 = Select(self.locateElement("xpath", '//*[@id="sName"]'))
        s1.select_by_visible_text("银月城")
        self.click('xpath', '/html/body/form/table/tbody/tr[2]/td[3]/input')
        print(self.get_text("xpath", "/html/body/form/table/tbody/tr[3]/td/strong"))
        self.driver.switch_to.default_content()

    # 删除客户
    def delete(self):
        self.click('xpath', '/html/body/div[1]/div[2]/div[1]/ul/li[6]/a')
        self.driver.switch_to.frame('mainiFrame')
        data = self.get_text('xpath', '/html/body/table/tbody/tr[4]/td[1]')
        self.click('xpath', '/html/body/table/tbody/tr[4]/td[6]/a/img')
        self.click('xpath', '/html/body/table/tbody/tr[4]/td[6]/div/span[1]')
        self.driver.switch_to.default_content()
        return data

    def add(self, name, phone, address, price):
        self.click('css', 'a.menuitem:nth-child(9)')
        self.click('xpath', '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[5]/ul/li[2]/a')
        self.driver.switch_to.frame('mainiFrame')
        self.ActionChain('css', '#name', name)
        self.ActionChain('css', '#phone', phone)
        self.ActionChain('css', '#address', address)
        self.ActionChain('css', '#birthday', '2020-04-28')
        self.click('css', '#sex0')
        self.ActionChain('css', '#price', price)
        self.click('css', '#button')
        self.driver.switch_to.default_content()

if __name__ == '__main__':
    F = Fin()
    F.login("wewopa", "123456")
    # F.order()
    # F.search()
    # F.delete()
    # F.add('张三', '1234568', '北京', '1500')
