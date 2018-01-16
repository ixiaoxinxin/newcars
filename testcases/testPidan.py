# -*- coding: utf-8 -*-
import os,datetime
import unittest
from bok_choy.web_app_test import WebAppTest
from pages.toubaoPages import loginPage,toubaoPage

class TestToubao(WebAppTest,):
    def setUp(self):
        super(TestToubao, self).setUp()
        self.login_page = loginPage(self.browser)
        self.toubao_page = toubaoPage(self.browser)

    def test_page_existence(self):
        self.login_page.visit()

    def test_toubao(self):
        usrname = '13071001'
        passwd = '0000'
        maintenanceStaff = "test"
        plateNo = u"冀AB1234"
        vIN = "8765UHFEWU324328F"
        engine = "23432fewf"
        years = "2017"
        registerDate = "2010-08-26"
        ID = "110102199006242727"
        self.login_page.visit().login(usrname,passwd)
        self.toubao_page_input = loginPage(self.browser)
        toubao_info = self.toubao_page.visit().toubao(maintenanceStaff,plateNo,vIN,engine,years,registerDate,ID)
        #assert
        #save_screenshot(TestToubao.driver(self),datetime.datetime.now().strftime('%Y-%M-%D'))



if __name__ == '__main__':
    os.environ["SELENIUM_BROWSER"] = "Firefox"
    unittest.main()