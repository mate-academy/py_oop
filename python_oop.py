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


class TestRunGeneral:
    registration_url = 'https://react-redux.realworld.io/#/register'
    login_url = 'https://react-redux.realworld.io/#/login'
    article_creation_url = 'https://react-redux.realworld.io/#/editor'
    article_test_data = 'Default'

    # Main constructor
    def __init__(self, first_name, last_name, user_email, user_password):
        self.username = ''.join([first_name, last_name])
        if len(user_email.split('@')) and ("@" in user_email):
            self.user_email = user_email
        else:
            print('Email field is not valid')
        self.user_password = user_password
        # comment line under this if you want to see the password in console
        self.user_password = '********'


class TestCases(TestRunGeneral):
    # Test suite for Registration page
    def registration_test_suite(self):
        print('-----------------------------')
        print('::: CHECKING REGISTRATION PAGE :::')
        print(f'- Open {self.registration_url} page')
        print(f'- Fill Username field as {self.username}')
        print(f'- Fill Email field as {self.user_email}')
        print(f'- Fill Password field as {self.user_password}')
        print('- Click on [Sign in] button')
        print('- Check the redirection to main page is working after successful registration')

    # Test suite for Login page
    def login_test_suite(self):
        print('-----------------------------')
        print('::: CHECKING LOGIN PAGE :::')
        self.login_flow()
        print('- Check the redirection to main page is working after successful login')

    # Test suite for Create Article page
    def publish_article_test_suite(self):
        print('-----------------------------')
        print('::: CHECKING CREATE ARTICLE PAGE :::')
        self.login_flow()
        print(f'- Open {self.article_creation_url} page')
        print(f'- Fill all fields with "{self.article_test_data}" text')
        print('- Click on [Publish Article] button')
        print('- Check if redirection to published page is working')


class TestRunBuilder(TestCases):
    # Login flow
    def login_flow(self):
        print(f'- Open {self.login_url} page')
        print(f'- Fill Username field as {self.user_email}')
        print(f'- Fill Password field as {self.user_password}')
        print('- Click on [Sign in] button')

    # Smoke Test Run
    def smoke_test_run(self):
        print('-----------------------------')
        print('You are running smoke flow')
        self.registration_test_suite()
        self.login_test_suite()

    # Sanity Test Run
    def sanity_test_run(self):
        print('-----------------------------')
        print('You are running sanity flow')
        self.publish_article_test_suite()

    # Regression Test Run
    def regression_test_run(self):
        print('-----------------------------')
        print('You are running regression flow')
        self.registration_test_suite()
        self.login_test_suite()
        self.publish_article_test_suite()


test_data = TestRunBuilder('Dmitriy', 'Lebed', 'up2dmas+12345@gmail.com', '12345678')

test_data.smoke_test_run()  # running smoke test run
test_data.sanity_test_run()  # running sanity test run
test_data.regression_test_run()  # running regression test run
