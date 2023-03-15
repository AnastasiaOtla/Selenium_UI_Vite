from selenium.webdriver.common.by import By


class MainPageLocators:
    MENU_BUTTON = (By.XPATH, '//*[@id="app"]/header/div/a/i')
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.ID, 'typesSelector')
    FILTER_BY_DOG = (By.ID, 'pv_id_2_0')
    FILTER_BY_PET_NAME = (By.ID, 'petName')
    NEXT_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[3]')
    PET_DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div/div/div[3]/div[1]/button')
    PROFILE_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    PETS = (By.CSS_SELECTOR, '.col-12')
    ADD_PET_BTN = (By.CLASS_NAME, "p-button p-component p-button-icon-only p-button-rounded p-button-primary p-button-outlined")
    EDIT_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')
    QUIT_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
    NAME_NEW_PET = (By.CLASS_NAME, "p-inputtext p-component w-full")
    AGE_NEW_PET = (By.CLASS_NAME, "p-inputtext p-component p-inputnumber-input")
    TYPE_NEW_PET_LIST = (By.ID, "typeSelector")
    TYPE_NEW_PET = (By.ID, "pv_id_2_list")
    TYPE_DOG = (By.ID, "pv_id_3_0")
    TYPE_CAT = (By.ID, "pv_id_3_1")
    TYPE_REPTILE = (By.ID, "pv_id_3_2")
    TYPE_HAMSTER = (By.ID, "pv_id_3_3")
    TYPE_PARROT = (By.ID, "pv_id_3_4")
    GENDER_NEW_PET_LIST = (By.ID, "genderSelector")
    GENDER_NEW_PET = (By.ID, "pv_id_3_list")
    MALE_GENDER = (By.ID, "pv_id_3_0")
    FEMAIL_GENDER = (By.ID, "pv_id_3_1")
    SUBMIT_ADD_PET_BTN = (By.CLASS_NAME, "p-button p-component p-button-success")

