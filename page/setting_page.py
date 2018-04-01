import os, sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SettingPage(BaseAction):

    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"

    option_button = By.ID, "com.cyanogenmod.filemanager:id/ab_actions"

    new_file = By.XPATH, ("text", "新建文件夹")
    new_txt = By.XPATH, ("text", "新建文件")
    select_all = By.XPATH, ("text", "全部选择")
    cancel_select_all = By.XPATH, ("text", "取消全选")
    bookmark = By.XPATH, ("text", "添加到书签")
    add_quick_icon = By.XPATH, ("text", "添加快捷方式")
    set_as_home = By.XPATH, ("text", "Set as home")
    bookmark_text = By.ID, "com.cyanogenmod.filemanager:id/bookmarks_item_name"
    father_dir = By.XPATH, ("text", "父目录")
    select_aaa = By.XPATH, ("text", "aaa")
    move_file = By.XPATH, ("text", "移动选择项")
    refresh = By.XPATH, ("text", "刷新")
    attr = By.XPATH, ("text", "属性")
    OK = By.ID, "android:id/button1"
    cancel = By.ID, "android:id/button2"
    dir_num = By.ID, "com.cyanogenmod.filemanager:id/navigation_status_selection_label"
    dir_attr = By.ID, "com.cyanogenmod.filemanager:id/breadcrumb_item"
    dir_attr_name = By.ID, "com.cyanogenmod.filemanager:id/fso_properties_name"

    message = By.ID, "com.cyanogenmod.filemanager:id/input_name_dialog_message"
    # 文本框
    text_view = By.ID, "com.cyanogenmod.filemanager:id/input_name_dialog_edit"

    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"
    home_button = By.ID, "android:id/home"
    class_text_view = By.CLASS_NAME, "android.widget.TextView"

    def click_search(self):
        self.click(self.search_button)
    def click_option(self):
        self.click(self.option_button)
    def click_new_file(self):
        self.click(self.new_file)
    def click_new_txt(self):
        self.clicks(self.new_txt)
    def click_select_all(self):
        self.click(self.select_all)
    def click_cancel_select_all(self):
        self.click(self.cancel_select_all)
        pass
    def click_add_bookmark(self):
        self.click(self.bookmark)
    def click_setashome(self):
        self.click(self.set_as_home)
    def click_home_botton(self):
        self.click(self.home_button)
    def click_father_dir(self):
        self.click(self.father_dir)
    def click_aaa(self):
        self.click(self.select_aaa)
    def click_move_file(self):
        self.click(self.move_file)
    def click_refresh(self):
        self.click(self.refresh)
    def click_attr(self):
        self.click(self.attr)
    def get_text(self):
        return self.getText(self.dir_num).text
        pass
    def get_text_attr(self):
        return self.getTexts(self.dir_attr).text
    def get_attr_name(self):
        return self.getTexts(self.dir_attr_name).text
    def get_boomark_name(self):
        return self.getTexts(self.bookmark_text).text
    def get_all_text(self):
        return self.getTextArray(self.class_text_view)
        pass
    def click_add_quick_icon(self):
        return self.click(self.add_quick_icon)
    def fina_aaa_not_in(self):
        self.find_aaa_not_in_screen()
    def sendkeycode(self,keynum):
        self.click_key(keynum)

    def click_OK_or_cancel(self):
        try:
            if self.getText(self.message).text == "此名称已存在.":
                self.click(self.cancel)
                self.click(self.cancel)
        except BaseException:
            self.click(self.OK)
    def click_findDir(self,dir):
        self.click_find_dir(dir)
    def assert_findDir(self,dir):
        if self.find_dir(dir):
            return True
        else:
            return 0
    def make_txt(self):
        for i in range(1,21):
            self.txt = str(i) + ".txt"
            self.click(self.option_button)
            self.clicks(self.new_txt)
            self.input_text(self.text_view,self.txt )
            self.click_OK_or_cancel()


    def input_text_view(self, text):
        self.input_text(self.text_view, text)

    def click_back(self):
        self.click(self.back_button)