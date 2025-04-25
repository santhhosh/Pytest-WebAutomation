import thread

from hrmpages.base_page import BasePage
from conftest import *
from configtestdata import *

@pytest.mark.usefixtures("setup")
@pytest.mark.Regression
class Test_Login:
    def setup_class(self):
        self.login_page = BasePage(self.driver)

    def test_valid_login(self):

        self.login_page.register(firstname,lastname,address,email,phone,password,confirm_password)



    def test_switch_to_alerts(self):

        self.login_page.switchto_alerts()


    def test_switch_to_windows(self):

        self.login_page.switchto_windows()
