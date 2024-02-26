import allure
from allure_commons.types import Severity

from qa_guru_python_10_12.data.users import student
from qa_guru_python_10_12.pages.registartion_page import RegistrationPage


@allure.tag('DemoQa')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', '1gonte')
@allure.feature('User registration')
@allure.story('Register new user')
@allure.link('https://demoqa.com', name='Testing')
@allure.title('Successfull registration')
def test_fill_registration_form():

    with allure.step('Open registration form'):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step('Fill form'):
        registration_page.register(student)

    with allure.step('Check filled info'):
        registration_page.should_have_registered(student)