"""
Description: Create TestRail client for generating Test Suites

Features:
- TestSuite should be created with (username list(First Name/Last Name), user_email, user_password)
- Show in test cases all user data except password (password should be shown as '********')
- Create test suite for login/registration/article create flow
- Please use the same steps in common methods
- Validate valid user email and profile

Testing:
- Run all your testsuite using calling methods for suite_object
"""


class TestRunBuilder:
    pass
    url_test_site = 'https://react-redux.realworld.io/#/?_k=aq3qtv'

    def __init__(self, user_name, user_email, pswrd):
        self.user_name = user_name
        self.user_email = user_email
        self.pswrd = pswrd
        def check_user_name(user_name):
            min_chars = 'Name should be min 8 chars'
            if len(user_name) >= 8:
                return True
            else:
                return min_chars
        def check_user_email(user_email):
            index_mail_mark = 0
            mail_mark = '@'
            if mail_mark in user_email:
                index_mail_mark += user_email.find(mail_mark)

            if (len(user_email) > index_mail_mark) and (index_mail_mark > 0):
                return True
        def check_password(pswrd):
            if len(pswrd) >= 8:
                return True
            else:
                return False
        if check_user_name(self.user_name) is True and check_user_email(self.user_email) is True and check_password(self.pswrd) is True:
            self.pswrd = pswrd.replace(pswrd, '*' * len(pswrd))

    def login_flow(self):
        print('Click [Sign in] button')
        print(f'Enter user email as {self.user_email}')
        print(f'Enter user password as {self.pswrd}')
        print('Click [Sign in] button')


    def registration_test(self):
        print('------------------\n')
        print("Registration form")
        print('Click [Sign Up] button in navigation bar')
        print(f'Enter username as {self.user_name}')
        print(f' Enter user email as {self.user_email}')
        print(f'Enter password as {self.pswrd}')
        print('Click [Sign in] button')
        print('check redirection to "/home" page')

    def login_test(self):
        print('------------------\n')
        print('Login form')
        self.login_flow()
        print('check redirect into "/home" page')

    def create_article(self):
        print('------------------\n')
        print('Create article')
        self.login_flow()
        print('Click [New post] button')
        print('fill out all fields as test data')
        print('Click [Publish] button')

    def test_run_smoke(self):
        self.login_test()

    def test_run_sanity(self):
        self.create_article()

    def test_run_regression(self):
        self.registration_test()
        self.login_flow()
        self.create_article()




test_run_smoke = TestRunBuilder('Lincoln', 'avraam@lincoln.com', '12345678')
test_run_sanity = TestRunBuilder('Lincoln1', 'avraam1@lincoln.com', '12345678')
test_run_regression = TestRunBuilder('Lincoln2', 'avraam2@lincoln.com', '12345678')

test_run_smoke.test_run_smoke()
test_run_sanity.test_run_sanity()
test_run_regression.test_run_regression()