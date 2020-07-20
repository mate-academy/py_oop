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
    url = 'https://qamay208.testrail.com'


    def __init__(self, first_name, last_name, user_email, user_password):

        self.username = first_name + last_name
        if "@" in user_email:
            self.useremail = user_email
        else:
            print('invalid email. please retry')
        self.user_password = user_password
        #self.user_password = "********"

   

    def testrail_greetings(self):
        print(f'Hello, tester. You are on {self.url}')

    def registration_test_suit(self):
        print('------------------')
        print('open "/registration" page')
        print(f'fill out username fields as {self.username}')
        print(f'fill out user email field as {self.useremail}')
        print(f'fill out password field as {self.user_password}')
        print('push [Registration] button')
        print('check redirection to "/home" page')

    def login_flow(self):
        print('open "/login" page')
        print(f'fill out username email field as {self.useremail}')
        print(f'fill out password field as {self.user_password}')
        print('push [Login] button')

    def login_test_suit(self):
        print('------------------')
        self.login_flow()
        print(f'fill out username email field as {self.useremail}')
        print(f'fill out password field as {self.user_password}')
        print('push [Login] button')
        print('check redirection to "/home" page')

    def create_article(self):
        print('------------------')
        self.login_flow()
        print('push [new article] button')
        print('fill out all fields as test data')
        print('push [Publish] button')
        print('check out all fields on article preview screen')

    def test_run_smoke(self):
        self.login_flow()

    def test_run_sanity(self):
        self.create_article()

    def test_run_regression(self):
        self.registration_test_suit()
        self.login_flow()
        self.create_article()


test_run = TestRunBuilder('Pamella', 'Anderson', 'pamella120@yahoo.com', '5051qwerty')
test_run.test_run_smoke()
# test_run_sanity = TestRunBuilder(username, user_email, user_password)
test_run.test_run_sanity()
# test_run_regression = TestRunBuilder(username, user_email, user_password)
test_run.test_run_regression()
