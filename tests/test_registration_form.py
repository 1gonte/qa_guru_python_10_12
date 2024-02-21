import allure

from qa_guru_python_10_12.data.users import student
from qa_guru_python_10_12.pages.registartion_page import RegistrationPage


@allure.title('Successfull registration')
def test_fill_registration_form():

    with allure.step('Open registration form'):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step('Fill form'):
        registration_page.register(student)

    with allure.step('Check filled info'):
        registration_page.should_have_registered(student)