import os

import allure, time
from os import path
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *
import random


class homepg():
    homeclick = (By.XPATH, "//a[@class='logo-img']//img")
    watchnowclick = (By.XPATH,
                     "//div[@class='carousel-item active']//div[@class='movie-content']//div[@class='btn-container']//div//button[@class='btn-view available-text d-none d-sm-block'][contains(text(),'Watch Now')]")
    closeplayer = (By.XPATH, "//div[@class='close tele-close']//img[@class='close-btn-image']")
    nextmovie = (By.XPATH, "//span[@class='carousel-control-next-icon']")
    mutebutton = (By.XPATH, "//span[contains(text(),'Volume/Mute')]/ancestor::button")
    resumebutton = (By.XPATH, "//button[contains(text(),'Resume watching')]")
    playbutton = (By.XPATH,
                  "//span[contains(text(),'Play/Pause')]/ancestor::div[@class='bmpui-ui-playbacktoggle-overlay']/div/button")
    addtolistcarousel = (By.XPATH,
                         "//div[@class='carousel-item active']//button[@class='cui-btn btn-movie'][contains(text(),'ADD TO LIST')]")
    createlist = (By.XPATH, "//div[@class='createNewList']")

    def __init__(self, browser):
        self.browser = browser

    """Home page-18"""

    @allure.step('To Verify Watch Now button is clikable and on click of it opens playout pop up')
    def verify_watchnow(self):
        time.sleep(10)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.homeclick))
        self.browser.find_element(*self.homeclick).click()
        self.browser.refresh()
        time.sleep(40)
        try:
            time.sleep(3)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.watchnowclick))
            data = self.browser.find_element(*self.watchnowclick)
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.watchnowclick))
            self.browser.find_element(*self.watchnowclick).click()
        else:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.nextmovie))
            self.browser.find_element(*self.nextmovie).click()
            time.sleep(5)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.watchnowclick))
            self.browser.find_element(*self.watchnowclick).click()
        time.sleep(30)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.watchnowclick))
        verify = self.browser.find_element(*self.closeplayer).is_displayed()
        # self.browser.find_element(*self.closeplayer).click()
        return verify

    """Home page-20"""

    @allure.step('To Verify mute control of the pop up works correctly')
    def verify_popupmutecontrols(self):
        time.sleep(4)
        try:
            time.sleep(3)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.resumebutton))
            data = self.browser.find_element(*self.resumebutton)
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.resumebutton))
            self.browser.find_element(*self.resumebutton).click()
        time.sleep(10)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.mutebutton))
        clas = self.browser.find_element(*self.mutebutton).get_attribute('class')
        print(clas)
        return clas

    @allure.step('To Verify all controls of the pop up works correctly')
    def verify_popupplaycontrols(self):
        time.sleep(10)
        try:
            time.sleep(3)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.resumebutton))
            data = self.browser.find_element(*self.resumebutton)
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.resumebutton))
            self.browser.find_element(*self.resumebutton).click()
        time.sleep(10)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.playbutton))
        clas = self.browser.find_element(*self.playbutton).get_attribute('class')
        time.sleep(4)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.closeplayer))
        print(clas)
        return clas

    def verify_closeplayer(self):
        self.browser.find_element(*self.closeplayer).click()

    """Home page-36"""

    @allure.step('Verify functionality of Add to List button')
    def verify_addtolistbutton(self):
        time.sleep(4)
        try:
            time.sleep(3)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.addtolistcarousel))
            data = self.browser.find_element(*self.addtolistcarousel)
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.addtolistcarousel))
            self.browser.find_element(*self.addtolistcarousel).click()
            time.sleep(10)
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.addtolistcarousel))
            verify = self.browser.find_element(*self.createlist).is_displayed()
            self.browser.refresh()
            time.sleep(30)
            return verify
