import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.variables import *


class homePagemylistsObj:
    total_lists = (By.XPATH, "//h2[contains(text(),'My Lists')]/ancestor::div[3]/following-sibling::div[1]//ul[1]//li")
    auto_list = (By.XPATH, "//p[contains(text(),'Automation List')]")
    myList = (By.XPATH, "//div[h2[contains(text(),'My Lists')]]")
    myList_rightNav = (By.XPATH, "//div[@class='movies-block-container']//i[@class='next-icon icon']")
    # myList_rightNav = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//i["
    #                              "@class='next-icon icon']")
    myList_prevNav = (By.XPATH, "//i[@class='previous-icon icon']")
    myList_seeall = (By.XPATH, "//a[contains(text(),'SEE LISTS')]")
    title_text = (By.XPATH, "//h2[contains(text(),'My Lists')]")
    lists_cards = (By.XPATH, "//div[p[contains(text(),'Automation List')]]")
    list_page_tile = (By.XPATH, "//p[@class='yourList']")
    detail_title = (By.XPATH, "//span[@class='view-title']")
    card_titles = (By.XPATH, "//p[contains(text(),'Automation List')]/parent::div[1]/p[2]/span[1]")
    curated_title = (By.XPATH, "//p[@class='title'][contains(text(),'Family')]")
    curated_made = (By.XPATH, "//p[@class='title'][contains(text(),'Family')]/ancestor::a[1]/p[1]")
    curated_numTitle = (By.XPATH, "//p[@class='title'][contains(text(),'Family')]/parent::div[1]/p[2]/span[1]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify number of lists in My Lists section')
    def verify_Mylists(self):
        count = self.browser.find_elements(*self.total_lists)
        print(len(count))
        return len(count)

    @allure.step('Verify in My list Automation List is displayed')
    def verify_autoList(self):
        time.sleep(2)
        lst = self.browser.find_element(*self.myList)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        time.sleep(2)
        return self.browser.find_element(*self.auto_list).is_displayed()

    @allure.step('Click on List card ')
    def click_listCard(self):
        time.sleep(2)
        self.browser.find_element(*self.auto_list).click()

    @allure.step('Verify Detail Page for list is opened ')
    def verify_detailedPage(self):
        return self.browser.find_element(*self.detail_title).text

    @allure.step('Verify number of titles on list cards ')
    def verify_Numbtitles(self):
        return self.browser.find_element(*self.card_titles).is_displayed()

    @allure.step('Click on see all Button ')
    def click_seeALL(self):
        self.browser.find_element(*self.myList_seeall).click()

    @allure.step('Verify My lists Right navigation arrow')
    def verify_rightNav(self):
        time.sleep(5)
        right_nav = self.browser.find_element(*self.myList_rightNav)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(right_nav).perform()
        return right_nav.is_displayed()

    @allure.step('Verify My Lists Left Navigation arrow')
    def verify_LeftNav(self):
        time.sleep(3)
        ledt_nav = self.browser.find_element(*self.myList_prevNav)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(ledt_nav).perform()
        return ledt_nav.is_displayed()

    @allure.step('Click on Right navigation arrow in My Lists Section')
    def click_rightNav(self):
        time.sleep(2)
        self.browser.find_element(*self.myList_rightNav).click()

    @allure.step('Click on Left Navigation arrow in My lists section ')
    def click_leftNav(self):
        time.sleep(3)
        self.browser.find_element(*self.myList_prevNav).click()

    @allure.step('Verify Title text in My lists section ')
    def verify_Mylists_title(self):
        return self.browser.find_element(*self.title_text).is_displayed()

    @allure.step('Verify See all button in my Lists section ')
    def verify_seeAll(self):
        time.sleep(1)
        return self.browser.find_element(*self.myList_seeall).is_displayed()

    @allure.step('Verify List cards in myList section ')
    def verify_listCards(self):
        time.sleep(1)
        return self.browser.find_element(*self.lists_cards).is_displayed()

    @allure.step('Verify List page heading i.e opening after click on see all button')
    def verify_list_Heading(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.list_page_tile))
        return self.browser.find_element(*self.list_page_tile).text

    @allure.step('Verify Text List made for you on curated list cards ')
    def verify_curatedText(self):
        time.sleep(1)
        return self.browser.find_element(*self.curated_made).text

    @allure.step('Verify List title on curated list cards')
    def verify_curateList_title(self):
        return self.browser.find_element(*self.curated_title).text

    @allure.step('Verify number of titles on curated list ')
    def verify_curatedNumtitles(self):
        return self.browser.find_element(*self.curated_numTitle).is_displayed()

