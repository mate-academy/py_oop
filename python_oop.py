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
import re

class TestRunBuilder:
    url = 'https:/react-redux.realworld.io'
    # EMAIL_REGEX = re.compile(r'[a-z0-9+]+@[a-z0-9]+.com')
    EMAIL_REGEX = re.compile(r'[\w+]+@[\w]+.com')

    def __init__(self, username, user_email, user_password):
        self.valid_data = True
        if len(username) >= 8:
            self.username = username
        else:
            print('Username too short. Minimum length 8 symbols')
            self.valid_data = False

        if self.EMAIL_REGEX.fullmatch(user_email):
            self.user_email = user_email
        else:
            print('Invalid email address')
            self.valid_data = False

        if len(user_password) >= 8:
            self.user_password = user_password
        else:
            print('Password too short. Minimum length 8 symbols')
            self.valid_data = False

    def show_user_data(self):
        if self.valid_data:
            print(f'Username: {self.username} \nUser email: {self.user_email} \nPassword: {len(self.user_password) * "*"} '
                  f'\nValid: {self.valid_data}')

    def login_common_flow(self):
        if self.valid_data:
            print('-' * 100)
            print(f'Open page, use: {self.url}')
            print('Click on "Sign In" link')
            print(f'Type "{self.username}" into "Username" field')
            print(f'Type "{len(self.user_password) * "*"}" into "Password" field')
            print('Click on [Sign in] button')

    def registration_common_flow(self):
        if self.valid_data:
            print('-' * 100)
            print(f'Open page, use: {self.url}')
            print('Click on "Sign Up" link')
            print(f'Type "{self.username}" into "Username" field')
            print(f'Type "{self.user_email}" into "Email" field')
            print(f'Type "{len(self.user_password) * "*"}" into "Password" field')
            print('Click on [Sign in] button')

    def registration_test_case(self):
        self.registration_common_flow()
        print('Redirect to Home page')
        print('-' * 100)

    def registration_with_existed_credentials_test_case(self):
        self.registration_common_flow()
        print(f'Validation error: {self.username} already exists')
        print('-' * 100)

    def login_test_case(self):
        self.login_common_flow()
        print('Redirect to main page')
        print('Check username in top-right on the page')
        print('Exit from account')
        print('-' * 100)

    def create_article_test_case(self):
        self.login_common_flow()
        print('Click on "New Post" link')
        print('Fill all fields in Article form')
        print('Click on [Publish Article] button')
        print('Check response')
        print('Exit from account')
        print('-' * 100)

    def registration_sanity_run(self):
        if self.valid_data:
            print('*'*20, 'Sanity Run', '*'*20)
            self.registration_test_case()
            self.login_test_case()
            self.registration_with_existed_credentials_test_case()

    def site_smoke_run(self):
        if self.valid_data:
            print('*' * 20, 'Smoke Run', '*' * 20)
            self.registration_test_case()
            self.login_test_case()
            self.create_article_test_case()

    def site_regression_run(self):
        if self.valid_data:
            print('*' * 20, 'Regression Run', '*' * 20)
            self.registration_test_case()
            self.login_test_case()
            self.create_article_test_case()
            self.registration_with_existed_credentials_test_case()


if __name__ == '__main__':
    test_run_smoke = TestRunBuilder('AndriiTest1', 'anrdiit est@gmail1.com', '123456789')
    test_run_sanity = TestRunBuilder('AndriiTest2', 'anrdiitest@gmail2.com', '123456789')
    test_run_regression = TestRunBuilder('AndriiTest3', 'anrdiitest@gmail3.com', '123456789')

    test_run_smoke.show_user_data()
    test_run_smoke.site_smoke_run()
    test_run_sanity.registration_sanity_run()
    test_run_regression.site_regression_run()


