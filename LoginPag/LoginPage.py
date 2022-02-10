from selenium.webdriver.common.by import By

from LoginPag.PageObject import PageObject


class LoginPage(PageObject):

    url = 'https://rmauro-failure.herokuapp.com/'
    class_search_button = 'btn'
    class_error_message = 'error-message-container'
    comando_sql = 'SearchString'

    def __init__(self, browser=None):
        super(LoginPage, self).__init__(browser=browser)
        self.open_login_page()

    def open_login_page(self):
        self.driver.get(self.url)

    def click_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_search_button).submit()

    def testar_comando_SQL(self, comando='mmer%'):
        self.driver.find_element(By.ID, self.comando_SQL).send_keys(comando)
        self.click_btn()
