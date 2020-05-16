import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.variables import *


class myListObj:
    list_name = (By.XPATH, "//span[@class='view-title']")
    share_button = (By.XPATH, "//span[@class='share-icon']")
    delete_button = (By.XPATH, "//span[contains(text(), 'Delete')]")
    list_check = (By.XPATH, "//input[@id='select-all']")
    list_selected = (By.XPATH, "//div[@class='item-action']/span[1]")
    download = (By.XPATH, "//button[contains(text(),'DOWNLOAD.CSV')]")
    share_popup = (By.XPATH, "//button[contains(text(),'SHARE LIST')]")
    add_list = (By.XPATH, "//button[@id='dropdownForm1']")
    delete_popup = (By.XPATH, "//button[contains(text(),'DELETE')]")
    close_popup = (By.XPATH, "//div[@class='modal-header-popup desk-close']//img[@class='close-btn-image']")
    static_topText = (By.XPATH, "//div[@class='share-header']")
    pop_list = (By.XPATH, "//div[@class='share-body ng-star-inserted']")
    static_2Text = (By.XPATH, "//div[@class='share-list']")
    email_textbox = (By.XPATH, "//input[@id='email']")
    share_btn = (By.XPATH, "//button[@class='share-btn']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify List name in list table ')
    def verify_listName(self):
        time.sleep(1)
        return self.browser.find_element(*self.list_name).text

    @allure.step('Verify share button is displayed in list detailed page')
    def verify_shareButton(self):
        time.sleep(1)
        return self.browser.find_element(*self.share_button).is_displayed()

    @allure.step('Click share button in right top ')
    def click_shareButton(self):
        time.sleep(1)
        self.browser.find_element(*self.share_button).click()

    @allure.step('Verify Delete button is displayed in list detailed page ')
    def verify_deleteButton(self):
        return self.browser.find_element(*self.delete_button).is_displayed()

    @allure.step('Verify Check box is displayed in list detailed page ')
    def verify_checkBox(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.list_check))
        return self.browser.find_element(*self.list_check).is_displayed()

    @allure.step('Clicking on check box in list page')
    def click_list_checkBox(self):
        time.sleep(2)
        self.browser.find_element(*self.list_check).click()

    @allure.step('Verify Check box gets selected after clicking on check box')
    def verify_checkselected(self):
        time.sleep(1)
        return self.browser.find_element(*self.list_check).is_selected()

    @allure.step('Verify Download.csv file  in footer popup')
    def verify_downloadCsv(self):
        time.sleep(1)
        return self.browser.find_element(*self.download).is_displayed()

    @allure.step('Verify share list  in footer popup')
    def verify_shareList(self):
        time.sleep(1)
        return self.browser.find_element(*self.share_popup).is_displayed()

    @allure.step('Verify Add to List tab in footer popup')
    def verify_addList(self):
        time.sleep(1)
        return self.browser.find_element(*self.add_list).is_displayed()

    @allure.step('Verify Delete tab in footer popup ')
    def verify_DeleteFooterpopup(self):
        time.sleep(1)
        return self.browser.find_element(*self.delete_popup).is_displayed()

    @allure.step('Verify List selected Text in opened footer popup')
    def verify_Listtext(self):
        time.sleep(1)
        return self.browser.find_element(*self.list_selected).text

    @allure.step('Verify Close button in opened Pop after clicking on share button ')
    def verify_closeBtn(self):
        time.sleep(3)
        return self.browser.find_element(*self.close_popup).is_displayed()

    @allure.step('Verify Static top Text in in share in share popup ')
    def verify_staticToptext(self):
        time.sleep(1)
        return self.browser.find_element(*self.static_topText).is_displayed()

    @allure.step('Verify List name and numbers of title in it ')
    def verify_lisTitle(self):
        time.sleep(1)
        return self.browser.find_element(*self.pop_list).is_displayed()

    @allure.step('Verify Static text in middle in share popup ')
    def verify_staticTextmiddle(self):
        time.sleep(1)
        return self.browser.find_element(*self.static_2Text).is_displayed()

    @allure.step('Verify Email textbox in share popup ')
    def verify_emailTextbox(self):
        time.sleep(1)
        return self.browser.find_element(*self.email_textbox).is_displayed()

    @allure.step('Verify Share button in share popup ')
    def verify_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.share_btn).is_displayed()
