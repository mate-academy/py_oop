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
    login_url = 'https://react-redux.realworld.io/#/login?_k=2vjfqt'

    def __init__(self, email, password):
        self.email = email
        self.password = password
        if '@' in email and len(email) < 25:
            print(f"{email} - valid email")
        else:
            print(f"{email} - invalid email")
        if len(password) > 8 and len(password) < 20:
            print(f"{password} - valid password")
        else:
            print(f"{password} - invalid password")


    def login_flow(self):
            print(f'- Open login page  {self.login_url}')
            print(f'- Fill Username field as {self.email}')
            print(f'- Fill Password field as {self.password}')
            print('- Click on [Sign in] button')




run1 = TestRunBuilder('alex@gmail.com', 'kasurasfyev')
run1.login_flow()
run2 = TestRunBuilder('alexdsadasdasdada@gmail.com', 'kasdasdadasdasdasdaurasfyev')
run2.login_flow()









# test_run_smoke = TestRunBuilder(username, user_email, user_password)
# test_run_sanity = TestRunBuilder(username, user_email, user_password)
# test_run_regression = TestRunBuilder(username, user_email, user_password)

