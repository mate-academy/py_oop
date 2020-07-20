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
    def __init__(self, first_name, last_name, user_email, user_password):

        self.username = first_name + last_name
        if "@" in user_email:
            self.user_email = user_email
        else:
            print('Email must include @')
        self.user_password = user_password

        if len(user_password) < 8 or len(user_password) > 20:
            print("Password must have at least 8 characters and max 20 characters")
        self.user_password = user_password

    def registration_test(self):
        print('------------------')
        print("Registration form")
        print('Click [Sign Up] button in navigation bar')
        print(f'Enter username as {self.username}')
        print(f' Enter user email as {self.user_email}')
        print(f'Enter password as {self.user_password}')
        print('Click [Sign in] button')
        print('check redirection to "/home" page')

    def login_flow(self):
        print('Click [Sign in] button')
        print(f'Enter user email as {self.user_email}')
        print(f'Enter user password as {self.user_password}')
        print('Click [Sign in] button')

    def login_test(self):
        print('------------------')
        print('Login form')
        self.login_flow()
        print('check redirect into "/home" page')

    def create_article(self):
        print('------------------')
        print('Create article')
        self.login_flow()
        print('Click [New post] button')
        print('fill out all fields as test data')
        print('Click [Publish] button')
        print('check out all fields on article preview screen')

    def test_run_smoke(self):
        self.login_test()

    def test_run_sanity(self):
        self.create_article()

    def test_run_regression(self):
        self.registration_test()
        self.login_flow()
        self.create_article()


test_run = TestRunBuilder('Yulia', 'Alloucha', 'pomelochka23@gmail.com', '44445785')
test_run.test_run_smoke()
# test_run_sanity = TestRunBuilder(username, user_email, user_password)
test_run.test_run_sanity()
# tes#t_run_regression = TestRunBuilder(username, user_email, user_password)
test_run.test_run_regression()
