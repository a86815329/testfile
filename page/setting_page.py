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
    father_dir = By.XPATH, ("text", "父目录")
    select_aaa = By.XPATH, ("text", "aaa")
    move_file = By.XPATH, ("text", "移动选择项")
    refresh = By.XPATH, ("text", "刷新")
    OK = By.ID, "android:id/button1"
    dir_num = By.ID, "com.cyanogenmod.filemanager:id/navigation_status_selection_label"

    # 文本框
    text_view = By.ID, "com.cyanogenmod.filemanager:id/input_name_dialog_edit"

    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_search(self):
        self.click(self.search_button)
    def click_option(self):
        self.click(self.option_button)
    def click_new_file(self):
        self.click(self.new_file)
    def click_select_all(self):
        self.click(self.select_all)
    def click_father_dir(self):
        self.click(self.father_dir)
    def click_aaa(self):
        self.click(self.select_aaa)
    def click_move_file(self):
        self.click(self.move_file)
    def click_refresh(self):
        self.click(self.refresh)
    def get_text(self):
        return self.getText(self.dir_num).text
        pass

    def click_OK(self):
        self.click(self.OK)
    def findDir(self):
        self.find_dir()
    def make_txt(self):
        for i in range(1,21):
            self.txt = str(i) + ".txt"
            self.click(self.option_button)
            self.clicks(self.new_txt)
            self.input_text(self.text_view,self.txt )
            self.click_OK()


    def input_text_view(self, text):
        self.input_text(self.text_view, text)

    def click_back(self):
        self.click(self.back_button)