class Test1:

    def test_button(self, setup_login_page):
        print('Clicar no botao search')
        setup_login_page.click_btn()