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
        self.setting_page.click_OK_or_cancel()
        self.setting_page.click_option()
        self.setting_page.click_new_file()
        self.setting_page.input_text_view("zzz")
        self.setting_page.click_OK_or_cancel()
        self.setting_page.click_findDir("zzz")
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
        self.setting_page.click_aaa()
        self.current_position_name = self.setting_page.get_text_attr()
        self.setting_page.click_option()
        self.setting_page.click_attr()
        self.attr_name = self.setting_page.get_attr_name()
        assert self.current_position_name == self.attr_name
    def testFile003(self):
        pass
        self.setting_page.fina_aaa_not_in()
        self.setting_page.click_option()
        self.setting_page.click_refresh()
        assert self.setting_page.find_dir_aaa()
    def testFile004(self):
        self.setting_page.click_option()
        self.setting_page.click_new_file()
        self.setting_page.input_text_view("testfile004")
        self.setting_page.click_OK_or_cancel()
        assert self.setting_page.assert_findDir("testfile004")
    def testFile005(self):
        pass
        self.setting_page.click_option()
        self.setting_page.click_new_txt()
        self.setting_page.input_text_view("test005.txt")
        self.setting_page.click_OK_or_cancel()
        self.setting_page.assert_findDir("test005.txt")
    def testFile006(self):
        self.setting_page.click_option()
        self.setting_page.click_select_all()
        assert self.setting_page.get_text() == "已选择 15 个文件夹和 3 个文件。"
    def testFile007(self):
        self.setting_page.click_option()
        self.setting_page.click_select_all()
        self.setting_page.click_option()
        self.setting_page.click_cancel_select_all()
        try:
            if self.setting_page.get_text():
                self.result = 0


        except BaseException:
            self.result =1
        assert self.result
    def testFile008(self):
        self.setting_page.click_option()
        self.setting_page.click_add_bookmark()
        self.current_position_name = self.setting_page.get_text_attr()
        self.setting_page.click_home_botton()
        self.bookmark_name = self.setting_page.get_boomark_name()
        assert self.current_position_name == self.bookmark_name
    def testFile009(self):
        self.current_position_name = self.setting_page.get_text_attr()
        self.setting_page.click_option()
        self.setting_page.click_add_quick_icon()
        self.setting_page.sendkeycode(3)
        self.textlist = self.setting_page.get_all_text()
        if self.current_position_name in self.textlist:
            assert 1
        else:
            assert 0
    def testFile010(self):
        self.setting_page.click_option()
        self.setting_page.click_setashome()
        self.position_name_1 = self.setting_page.get_text_attr()
        # pass
        self.setting_page.click_aaa()
        self.driver.start_activity('com.cyanogenmod.filemanager',
                                   '.activities.NavigationActivity')
        self.position_name_2 = self.setting_page.get_text_attr()
        assert self.position_name_1 == self.position_name_2
    def testFile011(self):
        assert 0




