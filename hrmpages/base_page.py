from hrmhelper.helper import Selenium_Helper
from locators.locators_all import *
from selenium.webdriver.support.ui import Select

class BasePage(Selenium_Helper):
    def __init__(self, driver):
        super().__init__(driver)



    def register(self,firstname,lastname,address,email,phone,password,confirm_password):
        self.webelement_enter(First_Name, firstname)
        self.webelement_enter(Last_Name, lastname)
        self.webelement_enter(Address, address)
        self.webelement_enter(Email, email)
        self.webelement_enter(Phone, phone)
        self.webelement_click(Gender)
        self.webelement_click(Hobbies)
        #self.select_dropdown_by_index(Languages, language)
        self.webelement_click(Skills)

        #self.webelement_click(Country)
        self.webelement_click(Dateofbirth_year)
        self.webelement_click(Dateofbirth_month)
        self.webelement_click(Dateofbirth_day)
        self.webelement_enter(Password, password)
        self.webelement_enter(Confirm_Password, confirm_password)
        self.webelement_click(Submit_button)

    def switchto_alerts(self):
        self.webelement_click(Switch_To)
        self.webelement_click(Alerts)
        self.webelement_click(click_button_1)

    def switchto_windows(self):
        self.webelement_click(Switch_To)
        self.webelement_click(Windows)
        self.webelement_click(click_button)
        #testing purpose

    def switchto_frames(self):
        self.webelement_click(Switch_To)