import os, sys, pytest

sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.setting_page import SettingPage


class TestFlie():
    def setup(self):
        self.driver = init_driver()
        self.driver.start_activity('com.cyanogenmod.filemanager',
                                   '.activities.NavigationActivity')
        self.setting_page = SettingPage(self.driver)

        pass

    def teardown(self):
        pass

    def testFile001(self):
        self.setting_page.click_option()
        self.setting_page.click_new_file()
        self.setting_page.input_text_view("aaa")
        self.setting_page.click_OK()
        self.setting_page.click_option()
        self.setting_page.click_new_file()
        self.setting_page.input_text_view("zzz")
        self.setting_page.click_OK()
        self.setting_page.findDir()
        self.setting_page.make_txt()
        self.setting_page.click_option()
        self.setting_page.click_select_all()
        self.setting_page.click_option()
        self.setting_page.click_refresh()
        self.setting_page.click_father_dir()
        self.setting_page.click_aaa()
        self.setting_page.click_option()
        self.setting_page.click_move_file()
        self.setting_page.click_option()
        self.setting_page.click_select_all()
        assert self.setting_page.get_text() == "已选择 20 个文件。"

        pass
    def testFile002(self):
        pass
