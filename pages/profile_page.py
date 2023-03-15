from .base_page import BasePage
from .locators import ProfilePageLocators
from .input_data import AuthorizationInput


class ProfilePage(BasePage):
    def go_to_add_pet_btn(self):
        new_pet_btn = self.browser.find_element(*ProfilePageLocators.ADD_PET_BTN)
        new_pet_btn.click()

    def go_to_add_new_name(self):
        new_name = self.browser.find_element(*ProfilePageLocators.NAME_NEW_PET)
        new_name.send_keys(AuthorizationInput.name_valid)

    def go_to_add_new_age(self):
        new_age = self.browser.find_element(*ProfilePageLocators.AGE_NEW_PET)
        new_age.send_keys(AuthorizationInput.age_valid)

    def choose_new_pet_type(self):
        pet_type_list = self.browser.find_element(*ProfilePageLocators.TYPE_NEW_PET_LIST)
        pet_type_list.click()

    def choose_new_pet_type_dog(self):
        new_pet_type_dog = self.browser.find_element(*ProfilePageLocators.TYPE_DOG)
        new_pet_type_dog.click()

    def choose_new_pet_gender(self):
        new_pet_type_gender = self.browser.find_element(*ProfilePageLocators.GENDER_NEW_PET_LIST)
        new_pet_type_gender.click()

    def choose_new_pet_gender_male(self):
        new_pet_male = self.browser.find_element(*ProfilePageLocators.MALE_GENDER)
        new_pet_male.click()

    def go_to_submit_add_pet_btn(self):
        submit_add_pet_btn = self.browser.find_element(*ProfilePageLocators.SUBMIT_ADD_PET_BTN)
        submit_add_pet_btn.click()

    def go_to_edit_pet_profile(self):
        edit_pet_button = self.browser.find_element(*ProfilePageLocators.EDIT_PET_BTN)
        edit_pet_button.click()

    def go_to_quit_button(self):
        quit_button = self.browser.find_element(*ProfilePageLocators.QUIT_BTN)
        quit_button.click()
