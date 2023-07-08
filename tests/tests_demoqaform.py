import datetime
import os
from selene import browser, have

from models.users import User
from pages.registration_page import RegistrationPage


def test_filling_form_demoqa():
    registration_page = RegistrationPage()

    ivan = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='Ivan@example.com',
        gender='Male',
        phone_number='9881234567',
        date_of_birth=datetime.date(2000, 10, 2),
        subjects='Chemistry',
        hobbies='Sports',
        image='Ivan.jpg',
        current_address='Mira str., 5',
        state='NCR',
        city='Delhi'

    )
    registration_page.open_practice_form_page()
    registration_page.register(ivan)
    registration_page.should_have_registered(ivan)
