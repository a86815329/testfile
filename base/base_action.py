from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def openFileManager(self):
        self.driver.start_activity('com.cyanogenmod.filemanager', '.com.cyanogenmod.filemanager.activities.NavigationActivity')

    def click(self, loc, time=10, poll=1):
        self.find_element(loc, time, poll).click()
    def clicks(self, loc, time=10, poll=1):
        self.find_elements(loc, time, poll)[1].click()
    def getText(self, loc, time=10, poll=1):
        return self.find_element(loc, time, poll)

    def input_text(self, loc, text, time=10, poll=1):
        self.find_element(loc,time,poll).clear()
        self.find_element(loc, time, poll).send_keys(text)
    def find_dir(self):
        while True:
            # 滑动屏幕
            self.driver.swipe(188, 659, 148, 248)

            # 定义函数find（）找出元素“关于手机”并返回
            def find():
                find_el = self.driver.find_elements_by_class_name("android.widget.TextView")
                for i in find_el:
                    if i.text == "zzz":
                        return i

            try:
                # 找到元素后点击
                find().click()
                # time.sleep(1)
                # 找到安卓版本并打印
                # print(driver.find_elements_by_id("android:id/summary")[2].text)
                # 完成后进行判断并抛出当前循环
                if find().text == "zzz":
                    break
            except AttributeError:
                pass

    def find_element(self, loc, time, poll):
        # By.XPATH,            ("text", "显示")
        loc_by, loc_value = loc
        if loc_by == By.XPATH:
            # //*[contains(@text,'显示')]

            # str = 456
            # "123%s789" % str <==> "123" + str + "789"
            # 结果 123456
            loc_value = "//*[contains(@" + loc_value[0] + ",'" + loc_value[1] + "')]"
        # return self.driver.find_element(loc_by, loc_value)
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(loc_by, loc_value))

    def find_elements(self, loc, time, poll):
        # By.XPATH,            ("text", "显示")
        loc_by, loc_value = loc
        if loc_by == By.XPATH:
            # //*[contains(@text,'显示')]

            # str = 456
            # "123%s789" % str <==> "123" + str + "789"
            # 结果 123456789
            loc_value = "//*[contains(@" + loc_value[0] + ",'" + loc_value[1] + "')]"
        # return self.driver.find_element(loc_by, loc_value)
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(loc_by, loc_value))
if __name__ == '__main__':
    BaseAction().openFileManager()
