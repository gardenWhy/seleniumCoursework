import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class CommonShare(object):
    # 构造函数初始化
    def __init__(self):
        self.driver = webdriver.Firefox()
        # 将浏览器最大化
        self.driver.maximize_window()
        pass

    # 打开网页
    def open_url(self, url):
        self.driver.get(url)
        # 设置隐式等待
        self.driver.implicitly_wait(10)
        pass

    # 封装一个定位元素的方法
    def locateElement(self, locate_type, value):
        # 判断定位方式
        # el定位到的元素
        el = None
        if locate_type == "id":
            el = self.driver.find_element_by_id(value)
        elif locate_type == "name":
            el = self.driver.find_element_by_name(value)
        elif locate_type == "class":
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == "text":
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == "xpath":
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == "css":
            el = self.driver.find_element_by_css_selector(value)

        if el is not None:
            return el

    # 封装点击函数
    # 可以吧locateElement 封装点击或输入函数里
    def click(self, locate_type, value):
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()
        time.sleep(4)

    # 封装输入函数
    def input_data(self, locate_type, value, data):
        el = self.locateElement(locate_type, value)
        el.send_keys(data)
        time.sleep(2)

    # 先点击后输入的函数
    def ActionChain(self, locate_type, value, data):
        el = self.locateElement(locate_type, value)
        # 有的浏览器有自动输入，使用double_click就可以覆盖
        ActionChains(self.driver).double_click(el).send_keys(data).perform()
        time.sleep(3)

    # 获取连接文本的函数
    def get_text(self, locate_type, value):
        el = self.locateElement(locate_type, value)
        return el.text

    # 获得属性的函数
    def get_attr(self, locate_type, value, data):
        el = self.locateElement(locate_type, value)
        return el.get_attribute(data)


if __name__ == '__main__':
    comm = CommonShare()
    comm.open_url("http://www.baidu.com")
    comm.locateElement("id", "kw").send_keys("桂林天气")
    comm.click("id", "su")
