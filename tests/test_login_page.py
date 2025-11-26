
def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('jasndkasjnd@gmail.com', ';oiasbbi')
    login_page.check_error_alert(('Epic sadface: '
                                'Username and password '
                                'do not match any user in this service'))

def test_correct_login_with_incorrect_passw(login_page):
    login_page.open_page()
    login_page.fill_login_form('standard_user', 'asdasdasd')
    login_page.check_error_alert(('Epic sadface: '
                                  'Username and password '
                                  'do not match any user in this service'))
