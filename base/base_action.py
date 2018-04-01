from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def openFileManager(self):
        self.driver.start_activity('com.cyanogenmod.filemanager', '.com.cyanogenmod.filemanager.activities.NavigationActivity')
    def click_key(self,keynum):
        self.driver.keyevent(keynum)

    def click(self, loc, time=10, poll=1):
        self.find_element(loc, time, poll).click()
    def clicks(self, loc, time=10, poll=1):
        self.find_elements(loc, time, poll)[1].click()
    def getText(self, loc, time=10, poll=1):
        return self.find_element(loc, time, poll)
    def getTexts(self, loc, time=10, poll=1):
        return self.find_elements(loc, time, poll)[len(self.find_elements(loc, time, poll)) - 1]
    def getTextArray(self, loc, time=10, poll=1):
        self.textlist = []
        for i in self.find_elements(loc, time, poll):
            self.textlist.append(i.text)
        return self.textlist

    def input_text(self, loc, text, time=10, poll=1):
        self.find_element(loc,time,poll).clear()
        self.find_element(loc, time, poll).send_keys(text)
    def click_find_dir(self,dir):
        self.find_dir(dir).click()
    def find_dir(self,dir):
        while True:
            # 滑动屏幕
            self.driver.swipe(188, 659, 148, 248)

            def find():
                find_el = self.driver.find_elements_by_class_name("android.widget.TextView")
                for i in find_el:
                    if i.text == dir:
                        return i
                    elif i.text == "allpairs.rar":
                        return i

            try:
                find()

                # time.sleep(1)
                # 找到安卓版本并打印
                # print(driver.find_elements_by_id("android:id/summary")[2].text)
                # 完成后进行判断并抛出当前循环
                if find().text == dir:
                    return find()
                elif find().text == "allpairs.rar":
                    return None
            except AttributeError:
                pass
    def find_dir_aaa(self):
        find_el = self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in find_el:
            if i.text == "aaa":
                return True

    def find_aaa_not_in_screen(self):
        while True:
            # 滑动屏幕
            self.driver.swipe(188, 659, 148, 248)

            array = []
            find_el = self.driver.find_elements_by_class_name("android.widget.TextView")
            for i in find_el:
                array.append(i.text)
            if "aaa" not in array:
                break
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
