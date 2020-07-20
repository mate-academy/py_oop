class TestRunBuilder:
    url = 'qamay18.testrail.io'

    def __init__(self, first_name, last_name, email, password):
        self.username = first_name + ' ' + last_name

        if '@' in email:
            self.useremail = email
        else:
            print('invalid email')

        if len(password) >= 10:
            self.password = password
        else:
            print('invalid password')

    def testrail_greatings(self):
        print(f'Hello {self.username}, u are in {self.url}')

    def registration_test_flow(self):
        print('----------------------')
        print('Push [SignUp] button')
        print(f'Fill in "Username" field like {self.username}')
        print(f'Fill in "Email" field like {self.useremail}')
        print(f'Fill in "Password" field like {self.password}')
        print('Push [Sumbit] button')
        print('Check redirection to "/Home" page')

    def login_test_flow(self):
        print('----------------------')
        print('Press [SignIn] button')
        print(f'Fill in "Email" field as {self.useremail}')
        print(f'Fill in "Password" field as {self.password}')
        print('Press [Login] button')

    def create_article_flow(self):
        print('----------------------')
        self.login_test_flow()
        print('Press [New Article] button')
        print('Fill in Article fields')
        print('Press [Publish] button')
        print('Check that article is displaying on the article list')

    def test_run_smoke(self):
        print('----------------------')
        self.registration_test_flow()

    def test_run_sanity(self):
        print('----------------------')
        self.login_test_flow()
        self.create_article_flow()

    def test_run_regression(self):
        print('----------------------')
        self.registration_test_flow()
        self.create_article_flow()


greating = TestRunBuilder('Oleksii', 'Samoilenko', 'shithedead@gmail.com', '1234qwer897987')
greating.testrail_greatings()

test_run = TestRunBuilder('Oleksii', 'Samoilenko', 'shithedead@gmail.com', '1234qwer897987')
test_run.test_run_smoke()

test_run2 = TestRunBuilder('Oleksii', 'Samoilenko', 'shithedead@gmail.com', '12346876qwer')
test_run2.test_run_sanity()

test_run3 = TestRunBuilder('Oleksii', 'Samoilenko', 'shithedead@gmail.com', '1234qwer875765')
test_run3.test_run_regression()
