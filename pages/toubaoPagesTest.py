# -*- coding: utf-8 -*-
from bok_choy.page_object import PageObject
import confs.confs

class toubaoPage(PageObject):
    url = 'http://172.20.1.2/#/dashboard'
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div[3]/div/div/div/div[1]/img').is_present()

    def userName(self,usrname):
        return self.q(xpath='//*[@id="userName"]').fill(usrname)

    def passwrd(self,passwrd):
        return self.q(xpath='//*[@id="home"]/form/div[2]/input').fill(passwrd)

    def login_btn(self):
        return self.q(xpath='//*[@id="login"]').click()

    def che_toubao(self):
        return self.q(xpath='//*[@id="push-menu-container"]/div[2]/div/div[1]/nav/ul/li[1]/a/div[2]/span').click()

    def keche(self):
        return self.q(xpath='/html/body/div[3]/div/div/div/div/div/div[3]/div/div/span').click()

    # def che_toubao(self):
    #     return self.q(xpath='//*[@id="channel"]/div[1]').is_present

    def maintain(self,maintenanceStaff):
        return self.q(xpath='//*[@id="maintenanceStaff"]').fill(maintenanceStaff)

    def plateNo(self,plateNo):
        return self.q(xpath='//*[@id="plateNo"]').fill(plateNo)

    def che_matching(self):
        return self.q(xpath='//*[@id="ng-app"]/div[2]/div/div/button').click()

    def vIN(self,vIN):
        return self.q(xpath='//*[@id="vIN"]').fill(vIN)

    def engine(self,engine):
        return self.q(xpath='//*[@id="engine"]').fill(engine)

    def che_type(self):
        return self.q(xpath='//*[@id="car"]/div/ul/ng-form/li[2]/div/div/div[2]/div/div/button').click()

    def years(self,years):
        return self.q(xpath='/html/body/div[3]/div/div/form/div[3]/div[1]/div[3]/div[2]/div/input') .fill(years)

    def query_che(self):
        return self.q(xpath='/html/body/div[3]/div/div/form/div[3]/div[1]/div[4]/button[1]').click()

    def result_che(self):
        return self.q(xpath='/html/body/div[3]/div/div/form/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[1]/a')\
            .click()

    def registerDate(self,registerDate):
        return self.q(xpath='//*[@id="registerDate"]').fill(registerDate)

    def validate_che(self):
        return self.q(xpath='//*[@id="checked_label_3"]').click()

    def personID(self,ID):
        return self.q(xpath='//*[@id="personID"]').fill(ID)

    def damage_che(self):
        return self.q(xpath='//*[@id="kindNamechoosed0"]').click()

    def three_car(self):
        return self.q(xpath='//*[@id="kindNamechoosed1"]').click()

    def driver(self):
        return self.q(xpath='//*[@id="kindNamechoosed2"]').click()

    def passager(self):
        return self.q(xpath='//*[@id="kindNamechoosed3"]').click()

    # def baofeialter(self):
    #     return

    #需要核实以下步骤
    def calculate_che(self):
        return self.q(xpath='//*[@id="push-menu-container"]/div[2]/div[2]/div[2]/ul/li[1]/div/div/button').click()

    def save_che(self):
        return self.q(xpath='//*[@id="save"]').click()

    def save_che_confim(self):
        return self.q(xpath='//*[@id="push-menu-container"]/div[2]/div[2]/div[2]/ul/li[1]/div/div/button').click()

    def manwork(self):
        return self.q(xpath='/html/body/div[6]/div/div/div/div/div[3]/button[2]').click()

    #@property
    def toubao(self,usrname,passwd,maintenanceStaff,plateNo,vIN,engine,years,registerDate,ID):
        self.userName(usrname)
        self.passwrd(passwd)
        self.login_btn()
        self.che_toubao()
        self.keche()
        self.maintain(maintenanceStaff)
        print "maintenanceStaff ok"
        self.plateNo(plateNo)
        print "plateNo ok"
        self.che_matching()
        print "che_matching ok"
        self.vIN(vIN)
        print "vIN ok"
        self.engine(engine)
        print "engine ok"
        self.che_type()
        print "che_type ok"
        self.years(years)
        print "years ok"
        self.query_che()
        print "query_che ok"
        self.result_che()
        print "result_che ok"
        self.registerDate(registerDate)
        print "registerDate ok"
        self.validate_che()
        print "validate_che ok"
        self.personID(ID)
        print "ID ok"
        self.damage_che()
        print "damage_che"
        self.three_car()
        print "three_car"
        self.driver()
        print "driver ok"
        self.passager()
        print "passager ok"
        self.calculate_che()
        print "calculate_che ok"
        self.save_che()
        print "save_che ok"
        self.save_che_confim()
        print "save_che_ok"
        self.manwork()
        print "over"










