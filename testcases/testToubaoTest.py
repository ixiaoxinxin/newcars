# -*- coding: utf-8 -*-
import os
import unittest
from bok_choy.web_app_test import WebAppTest
from pages.toubaoPagesTest import toubaoPage

class TestToubao(WebAppTest):
    def setUp(self):
        super(TestToubao, self).setUp()
        self.toubao_page = toubaoPage(self.browser)

    def test_toubao(self):
        test_usrname = '13071001'
        test_passwd = '0000'
        maintenanceStaff = "test"
        plateNo = u"冀AB1234"
        vIN = "8765UHFEWU324328F"
        engine = "23432fewf"
        years = "2017"
        registerDate = "2010-08-26"
        ID = "110102199006242727"
        self.toubao_page.visit().toubao(test_usrname,test_passwd,maintenanceStaff,plateNo,vIN,engine,years,registerDate,ID)



if __name__ == '__main__':
    os.environ["SELENIUM_BROWSER"] = "firefox"
    unittest.main()