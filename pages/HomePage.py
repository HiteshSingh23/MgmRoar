from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.webdriver import WebDriver
import allure
from pathlib import Path
import csv
import time
from selenium.webdriver import ActionChains

class homepage:

    header_logo = (By.XPATH, "//div[@class='header']//img[@alt='logo-img']")
    header_movie = (By.XPATH, "//ul[@class='menu-items']//a[@id='Movies']")
    header_television = (By.XPATH, "//ul[@class='menu-items']//a[@id='Television']")
    header_mylist = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    header_logout_button = (By.XPATH, "//button[@class='user-logout-btn']")
    all_movies_television = (By.XPATH, "//div[@class='banner-text']")
    lists = (By.XPATH, "//div[@class='col']")
    email_textbox = (By.XPATH, "//input[@name='username']")
    header = (By.XPATH, "//div[@class='header']")
    carousel = (By.XPATH, "//div[@class='carousel']")
    movie_list_bestpicturewinner = (By.XPATH, "//h2[text()='Best Picture Winners']")
    movie_list_jamesbond = (By.XPATH, "//h2[text()='James Bond']")
    movie_list_newreleases = (By.XPATH, "//h2[text()='New Releases']")
    movie_list_actionadventure = (By.XPATH, "//h2[text()='Action / Adventure']")
    movie_list_oscarwinning = (By.XPATH, "//h2[text()='Oscar-winning Films']")
    movie_list_actionhits = (By.XPATH, "//h2[text()='Action Packed Hits']")
    movie_list_robocop = (By.XPATH, "//h2[text()='Robocop']")
    movie_list_rockey = (By.XPATH,"//h2[text()='Rocky']")
    movie_list_Pinkpanther = (By.XPATH, "//h2[text()='Pink Panther']")
    movie_list_legallyblonde = (By.XPATH, "//h2[text()='Legally Blonde']")
    see_all_tv_shows = (By.XPATH, "//div//button[text()=' SEE ALL TV SHOWS ']")
    see_all_movies = (By.XPATH, "//div//button[text()=' SEE ALL MOVIES ']")
    footer_logo = (By.XPATH,"//section//img[@alt='footer-logo']")
    privacy_policy = (By.XPATH, "//li//a[text()='privacy policy']")
    terms_of_use = (By.XPATH, "//li//a[text()='terms of use']")
    support = (By.XPATH, "//div//a[text()='Support']")
    movie_image_slider = (By.XPATH, "//div[@class='carousel-inner']")
    next_navigation = (By.XPATH, "//span[@class='carousel-control-next-icon']")
    previous_navigtion = (By.XPATH, "//span[@class='carousel-control-prev-icon']")
    carousel_progress_bar = (By.XPATH, "//ul[@class='carousel-menu-list']")
    progress_bar_spectre = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Spectre']")
    progress_bar_armyofdarkness = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Army Of Darkness']")
    progress_bar_magnificent = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='The Magnificent Seven (2016)']")
    progress_bar_rocky = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Rocky II']")
    progress_bar_amigos = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Three Amigos!']")
    progress_bar_legally_blonde = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Legally Blonde']")
    progress_bar_witch_hunter = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Hansel & Gretel Witch Hunters']")
    slider_background_images = (By.XPATH, "//div[@class='carousel-inner']//img[@class='slider-image']")
    movie_logo = (By.XPATH, "//img[@alt='logo-image']")
    watchnow_button = (By.XPATH, "//div[@class='btn-container']/button[text()=' Watch Now ']")
    add_to_list_button = (By.XPATH, "//div[@class='btn-container']//button[text()='ADD TO LIST']")
    view_details = (By.XPATH, "//div[@class='btn-container']//button[text()='View details']")
    synopsis_title = (By.XPATH, "//div[@class='row']//p[@class='synopsis-title']")
    see_all_button = (By.XPATH, "//div[@class='row']//a[@class='see-all-text']")
    movie_poster = (By.XPATH, "//div[@class='ng-scroll-content']//div[@class='movie-poster']")
    movie_list_next_button = (By.XPATH, "(//div//a[@role='button']/i[@class='next-icon icon'])[2]")
    movie_list_prev_button = (By.XPATH, "//div//a[@role='button']/i[@class='previous-icon icon']")
    poster_image = By.XPATH, ("//div//img[@class='image-loaded']")
    movie_title_Detroit = (By.XPATH, "//p[@class='movie-title light-color'][contains(text(),'Detroit')]")
    movie_genres = (By.XPATH, "//div[@class='movies-block-container light_background']//ul[@class='movies-list d-flex "
                              "active']//li[1]//mgm-movie-poster[1]//div[1]//div[3]//span[1]")
    movie_card_list = (By.XPATH, "//div[@class='button-hover ']//button[text()='ADD TO LIST']")
    movie_card_watch_now = (By.XPATH, "//h2[contains(text(),'Best Picture "
                                      "Winners')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                                      "@class='movies-list d-flex active']/li[1]//button[contains(text(),"
                                      "'Watch movie')]")
    movie_card_watch_trailer = (By.XPATH, "//div[@class='button-hover ']//button[text()='Watch trailer']")
    #movie_card_view_details = (By.XPATH, "//div[@class = 'button-hover']//button[text()='View details']")
    explore_element = (By.XPATH, "//div[@class='gold-footer']/h2")
    television_show = (By.XPATH, "//div/h2[text()='Our Television Shows']")
    movies = (By.XPATH, "//div/h2[text()='Our Movies']")
    movie_title_Flyboys = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Flyboys ']")
    movie_title_Capote = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Capote ']")
    movie_title_Hotel_Rwanda = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Hotel Rwanda ']")
    movie_title_ben_huh = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Ben-hur (2016) ']")
    movie_title_Valkyrie = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Valkyrie ']")
    movie_card_view_details = (By.XPATH, "//div[@class='button-hover ']//button[text()='View details']")
    player_popup = (By.XPATH, "//div[@class='modal-body']")
    movie_close_btn = (By.XPATH, "//img[@class='close-btn-image']")
    titles_underligned = (By.XPATH, "//ul[@class='carousel-menu-list']/li[@class='carousel-menu active']")
    recently_watched = (By.XPATH, "//div//h2[text()='Recently Watched']")
    Recently_watched_next_button = (By.XPATH, "(//div//a[@role='button']/i[@class='next-icon icon'])[1]")
    movie_name = (By.XPATH, "//div[@class='movie-poster']//p")
    add_to_list_search = (By.XPATH, "//div[@class='search-content']/input")
    add_to_list_clear = (By.XPATH, "//div[@class='atl-searchclear']//span")
    add_to_list_list_name = (By.XPATH, "//div[@class='toggle-btn-item']")
    add_to_list_toggel_button = (By.XPATH, "(//div[@class='toggle-btn-item']//label/span[@class='slider round'])[1]")
    add_to_list_toggel_button1 = (By.XPATH, "//div[@class='single-toggle']//span[text()=' test ']")
    add_to_list = (By.XPATH, "//div[@class='atl-add-btn']//span")
    add_to_list_enter_name = (By.XPATH, "//div[@class='atl-add-form']//input")
    add_to_list_create_list = (By.XPATH, "//div[@class='atl-newlistadd']//span")
    new_list = By.XPATH, ("(//div[@class='toggle-btn-item'])[1]")
    selected_list = (By.XPATH, "//div[@class='single-toggle']//input[@class='ng-valid ng-dirty ng-touched']")
    add_to_list_verify = (By.XPATH, "//div[@class='movie-detail']/p")
    created_list = (By.XPATH, "//div//a[text()='Demo']")
    created_list_test = (By.XPATH, "//div//a[text()='test']")
    abc = (By.XPATH, "//div[@class='toggle-btn-item']//input")
    add_to_list_creating = (By.XPATH, "//div[text()='Creating...']")
    add_to_list_created = (By.XPATH, "//div[@class='createdListItem']//span[text()=' Created! ']")
    new_list1 = (By.XPATH, "//div[@class='toggle-btn-item']")
    list_auto_select = (By.XPATH, "//div//input[@class='ng-valid ng-dirty ng-touched']")
    next_arrow = (By.XPATH, "//div[div[div[h2[text()='Best Picture Winners']]]]/following-sibling::div[1]//i["
                            "@class='next-icon icon']")
    best_pictures = (By.XPATH, "//h2[text()='Best Picture Winners']")
    play_begining = (By.XPATH, "//button[@class='watch-again-btn btn-view']")
    watch_popup = (By.XPATH, "//div[@id='bitmovin-player']")
    close_button = (By.XPATH, "//img[@class='close-btn-image']")
    add_list = (By.XPATH, "//h2[contains(text(),'Best Picture "
                          "Winners')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                          "@class='movies-list d-flex active']/li[1]//button[contains(text(),'ADD TO LIST')]")

    cardhover_option1 = (By.XPATH, "//h2[contains(text(),'Best Picture "
                                   "Winners')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                                   "@class='movies-list d-flex active']/li[1]//div[@class='button-hover']/ul[1]/li[1]")
    cardhover_option2 = (By.XPATH, "//h2[contains(text(),'Best Picture "
                                   "Winners')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                                   "@class='movies-list d-flex active']/li[1]//div[@class='button-hover']/ul[1]/li[2]")
    cardhover_option3 = (By.XPATH, "//h2[contains(text(),'Best Picture "
                                   "Winners')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                                   "@class='movies-list d-flex active']/li[1]//div[@class='button-hover']/ul[1]/li[3]")
    cardhover_option4 = (By.XPATH, "//h2[contains(text(),'Best Picture "
                                   "Winners')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                                   "@class='movies-list d-flex active']/li[1]//div[@class='button-hover']/ul[1]/li[4]")


    def __init__(self, browser):
        self.browser = browser
        #self.browser = WebDriver

    @allure.step('Verify logo is visible on header')
    def HomePageLogo(self):
        return self.browser.find_element(*self.header_logo).is_displayed()

    @allure.step('Verify Movies link is visible in header')
    def HeaderMovies(self):
        return self.browser.find_element(*self.header_movie).is_displayed()
    
    @allure.step('Verify Television shows link is visible in header')
    def HeaderTelevision(self):
        return self.browser.find_element(*self.header_television).is_displayed()

    @allure.step('Verify MyList link is visible in header')
    def HeaderMylist(self):
        return self.browser.find_element(*self.header_mylist).is_displayed()

    @allure.step('Verify Logout button is present in header')
    def HeaderLogoutButton(self):
        return self.browser.find_element(*self.header_logout_button).is_displayed()

    @allure.step('Click Movies link')
    def ClickMovies(self):
        self.browser.find_element(*self.header_movie).click()
        return  self.browser.find_element(*self.all_movies_television).is_displayed()
    
    @allure.step('Click Television link')
    def ClickTelevision(self):
        self.browser.find_element(*self.header_television).click()
        return self.browser.find_element(*self.all_movies_television).is_displayed()
    
    @allure.step('Click Lists link')
    def ClickLists(self):
        self.browser.find_element(*self.header_mylist).click()
        return self.browser.find_element(*self.lists).is_displayed()
    
    @allure.step('Go back to homepage')
    def ClickLogo(self):
        self.browser.find_element(*self.header_logo).click()
        time.sleep(5)
        self.browser.refresh()
        return self.browser.find_element(*self.header_movie).is_displayed()

    @allure.step('Click logout button')
    def ClickLogoutButton(self):
        time.sleep(5)
        self.browser.find_element(*self.header_logout_button).click()
        time.sleep(5)
        return self.browser.find_element(*self.email_textbox).is_displayed()

    @allure.step('Homepage header')
    def HomepageElementHeader(self):
        time.sleep(5)
        return self.browser.find_element(*self.header).is_displayed()

    @allure.step('Homepage Carousel slider')
    def HomepageMainCarousel(self):
        return self.browser.find_element(*self.carousel).is_displayed()

    @allure.step('Movie List Best Picture Winner')
    def HomepageMovieList1(self):
        return self.browser.find_element(*self.movie_list_bestpicturewinner).is_displayed()

    @allure.step('Movie List James Bond')
    def HomepageMovieList2(self):
        return self.browser.find_element(*self.movie_list_jamesbond).is_displayed()

    @allure.step('Movie List New Release')
    def HomepageMovieList3(self):
        return self.browser.find_element(*self.movie_list_newreleases).is_displayed()

    @allure.step('Movie List Action/Adventure')
    def HomepageMovieList4(self):
        return self.browser.find_element(*self.movie_list_actionadventure).is_displayed()

    @allure.step('Movie List Oscar Winning Films')
    def HomepageMovieList5(self):
        return self.browser.find_element(*self.movie_list_oscarwinning).is_displayed()

    @allure.step('Movie List Action Packed Hits')
    def HomepageMovieList6(self):
        return self.browser.find_element(*self.movie_list_actionhits).is_displayed()

    @allure.step('Movie List Robocop')
    def HomepageMovieList7(self):
        return self.browser.find_element(*self.movie_list_robocop).is_displayed()

    @allure.step('Movie List Rocky')
    def HomepageMovieList8(self):
        return self.browser.find_element(*self.movie_list_rockey).is_displayed()

    @allure.step('Movie List Pink Panther')
    def HomepageMovieList9(self):
        return self.browser.find_element(*self.movie_list_Pinkpanther).is_displayed()

    @allure.step('Movie List Legally Blonde')
    def HomepageMovieList10(self):
        return self.browser.find_element(*self.movie_list_legallyblonde).is_displayed()
    
    @allure.step('Explore all tv shows')
    def HomepageExploreAllTvShows(self):
        return self.browser.find_element(*self.see_all_tv_shows).is_displayed()

    @allure.step('Explore all Movies')
    def HomepageExploreAllMovies(self):
        return self.browser.find_element(*self.see_all_movies).is_displayed()

    @allure.step('Global Footer logo')
    def HomepageFooterLogo(self):
        return self.browser.find_element(*self.footer_logo).is_displayed()

    @allure.step('Global Footer Privacy Policy')
    def HomepageFooterPrivacy(self):
        return self.browser.find_element(*self.privacy_policy).is_displayed()

    @allure.step('Global Footer Use of terms')
    def HomepageFooterTerms(self):
        return self.browser.find_element(*self.terms_of_use).is_displayed()

    @allure.step('Global Footer Support')
    def HomepageFooterSupport(self):
        return self.browser.find_element(*self.support).is_displayed()

    @allure.step('Carousel image slider')
    def MovieImageSlider(self):
        return self.browser.find_element(*self.movie_image_slider).is_displayed()

    @allure.step('Carousel Progress bar')
    def ProgressBar(self):
        return self.browser.find_element(*self.carousel_progress_bar).is_displayed()

    @allure.step('Progress bar movie Spectre')
    def ProgressBarSpectre(self):
        self.browser.refresh()
        time.sleep(5)
        return self.browser.find_element(*self.progress_bar_spectre).is_displayed()

    @allure.step('Progress bar movie Army of Darkness')
    def ProgressBarArmyOfDarkness(self):
        #self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_armyofdarkness).is_displayed()

    @allure.step('Progress bar movie The Magnificient Seven')
    def ProgressBarMagnificent(self):
        #self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_magnificent).is_displayed()

    @allure.step('Progress bar movie Rocky')
    def ProgressBarRockey(self):
        #self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_rocky).is_displayed()

    @allure.step('Progress bar movie Three Amigosi')
    def ProgressBarAmigos(self):
        #self.browser.find_element(*self.next_navigation).click()
        #return self.browser.find_element(*self.progress_bar_amigos).is_displayed()
        #time.sleep(10)
        try:
            movie = self.browser.find_element(*self.progress_bar_amigos).is_displayed()

            if movie == True:
                return True
        except:
            return False

    @allure.step('Progress bar movie Legally Blonde')
    def ProgressBarLegallyBlonde(self):
        #self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_legally_blonde).is_displayed()

    @allure.step('Progress bar movie Hansel and Gretel witch hunter')
    def ProgressBarWitchHunter(self):
        #self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_witch_hunter).is_displayed()
    
    @allure.step('Previous navigation button in progress bar')
    def ProgressBarPreviousArrow(self):
        return self.browser.find_element(*self.previous_navigtion).is_displayed()
    
    @allure.step('Next navigation button in progress bar')
    def ProgressBarNextArrow(self):
        return self.browser.find_element(*self.next_navigation).is_displayed()

    @allure.step('Slider Background Image')
    def SliderBackgroundImage(self):
        time.sleep(10)
        self.browser.find_element(*self.next_navigation).click()
        slider_images = self.browser.find_element(*self.slider_background_images).is_displayed()
        print("aabb")
        return slider_images

    @allure.step('Movie logo')
    def MovieLogo(self):
        return self.browser.find_element(*self.movie_logo).is_displayed()

    @allure.step('Watch now button')
    def WatchNowButton(self):
        return self.browser.find_element(*self.watchnow_button).is_displayed()

    @allure.step('Add to list button')
    def AddToListButton(self):
        return self.browser.find_element(*self.add_to_list_button).is_displayed()

    @allure.step('Add to list button')
    def ViewDetailsButton(self):
        return self.browser.find_element(*self.view_details).is_displayed()

    @allure.step('Click View Detail Button')
    def ClickViewDetailsButton(self):
        self.browser.find_element(*self.view_details).click()
        time.sleep(5)
        self.browser.refresh()
        time.sleep(5)
        title = self.browser.find_element(*self.synopsis_title)
        title.location_once_scrolled_into_view
        time.sleep(3)
        name = title.text
        return name
    
    @allure.step('Click Spectre Movie')
    def ClickSpectreMovie(self):
        self.browser.find_element(*self.progress_bar_spectre).click()
        
    @allure.step('See All Button')
    def SeeAllButton(self):
        see = []
        see = self.browser.find_elements(*self.see_all_button)
        button = see[1].is_displayed()
        print(len(see))
        return button
    
    @allure.step('Movie Poter')
    def MoviePoster(self):
        time.sleep(4)
        poster = []
        poster =  self.browser.find_element(*self.movie_poster)
        poster.location_once_scrolled_into_view
        time.sleep(4)
        poster1 = poster.is_displayed()
        return poster1
    
    @allure.step('Movie List Next Button')
    def MovieListNextButton(self):
        nextbtn = self.browser.find_element(*self.movie_list_next_button)
        nextbtn.location_once_scrolled_into_view
        global actionchains
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(nextbtn).perform()
        nextbtn.click()
        btn = nextbtn.is_displayed()
        #time.sleep(10)
        #nextbtn.click()
        return btn
    
    @allure.step('Movie List previous Button')
    def MovieListPrevButton(self):
        pic = self.browser.find_element(*self.best_pictures)
        self.browser.execute_script("arguments[0].scrollIntoView();", pic)
        time.sleep(1)
        prevbtn = self.browser.find_element(*self.movie_list_prev_button)
        ActionChains(self.browser).move_to_element(prevbtn).perform()
        #prevbtn.click()
        return self.browser.find_element(*self.movie_list_prev_button).is_displayed()
        
    @allure.step('Movie List Poster Image')    
    def PosterImage(self):
        return self.browser.find_element(*self.poster_image).is_displayed()
    
    @allure.step('Movie Title Element')
    def MovieTitle(self):
        return self.browser.find_element(*self.movie_title_Detroit).is_displayed()
    
    @allure.step('Movie Genre Element')
    def MovieGenre(self):
        return self.browser.find_element(*self.movie_genres).is_displayed()

    @allure.step('Movie Card Add To List Button')
    def MovieCardAddToList(self):
        return self.browser.find_element(*self.movie_card_list).is_displayed()

    @allure.step('Movie card Watch Now Button')
    def MovieCardWatchNow(self):
        return self.browser.find_element(*self.movie_card_watch_now).is_displayed()
    
    
    @allure.step('Movie Card Watch Trailer Button')
    def MovieCardWatchTrailer(self):
        return self.browser.find_element(*self.movie_card_watch_trailer).is_displayed()


    @allure.step('Movie Card View Detail Button')
    def MovieCardViewDetails(self):
        movie = self.browser.find_element(*self.movie_list_jamesbond)
        movie.location_once_scrolled_into_view
        time.sleep(10)
        title = self.browser.find_element(*self.movie_card_view_details)
        title.location_once_scrolled_into_view
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(title).perform()
        time.sleep(10)
        abc = title.is_displayed()
        #title.click()
        #time.sleep(10)
        return abc


    @allure.step('Explore Element')
    def ExploreElement(self):
        return self.browser.find_element(*self.explore_element).is_displayed()

    @allure.step('Click Explore All Tv Shows')
    def ClickExploreAllTvShows(self):
        self.browser.find_element(*self.see_all_tv_shows).click()
        return self.browser.find_element(*self.television_show).is_displayed()

    @allure.step('Click Explore All Movie')
    def ClickExploreAllMovies(self):
        self.browser.find_element(*self.see_all_movies).click()
        return self.browser.find_element(*self.movies).is_displayed()
    
    @allure.step('Movie List Previous Button')
    def MovieListPrevButton1(self):
        try:
            prevbtn = self.browser.find_element(*self.movie_list_prev_button).is_displayed()
            #actionchains.move_to_element(prevbtn).perform()
            #prevbtn.click()
            if prevbtn == True:
                return True
        except:
            return False

    @allure.step('Movie List Next Button')
    def MovieListNextButton1(self):
        pic = self.browser.find_element(*self.best_pictures)
        self.browser.execute_script("arguments[0].scrollIntoView();", pic)
        time.sleep(1)
        right_nav = self.browser.find_element(*self.next_arrow)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(right_nav).perform()
        return right_nav.is_displayed()

    @allure.step('click on Right navigation arrow in best pictures ')
    def click_rightarrow(self):
        time.sleep(1)
        right_nav = self.browser.find_element(*self.next_arrow)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(right_nav).perform()
        right_nav.click()

    @allure.step('Right Navigation Behaviour')
    def RightNavigationBehaviour(self):
        return self.browser.find_element(*self.movie_title_Flyboys).is_displayed()
    
    @allure.step('Right Navigation Behaviour')
    def RightNavigationBehaviour1(self):
        return self.browser.find_element(*self.movie_title_Capote).is_displayed()

    @allure.step('Right Navigation Behaviour')
    def RightNavigationBehaviour2(self):
        return self.browser.find_element(*self.movie_title_Hotel_Rwanda).is_displayed()

    @allure.step('Click Movie list prev Navigation button')
    def ClickPrevNavigationButton(self):
        prevbtn = self.browser.find_element(*self.movie_list_prev_button)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(prevbtn).perform()
        prevbtn.click()

    @allure.step('Movie Title Benhuh')
    def MovieTitleBenHuh(self):
        return self.browser.find_element(*self.movie_title_ben_huh).is_displayed()

    @allure.step('Movie Title Valkrie')
    def MovieTitleValkyrie(self):
        return self.browser.find_element(*self.movie_title_Valkyrie).is_displayed()

    @allure.step('Movie List Next Navigation Disable')
    def NextNavigationDisable(self):
        try:
            nextbtn = self.browser.find_element(*self.movie_list_next_button)
            nextbtn.location_once_scrolled_into_view
            global actionchains
            #actionchains = ActionChains(self.browser)
            actionchains.move_to_element(nextbtn).perform()
            nextbtn.click()
            nextbtn1 = self.browser.find_element(*self.movie_list_next_button).is_displayed()
            # time.sleep(10)
            # nextbtn.click()
            if nextbtn1 == True:
                return True
        except:
            return False

    @allure.step('Movie List View Detail button')
    def MovieListViewDetailButton(self):
        movie = self.browser.find_element(*self.movie_list_jamesbond)
        movie.location_once_scrolled_into_view
        time.sleep(10)
        title = self.browser.find_element(*self.movie_card_view_details)
        title.location_once_scrolled_into_view
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(title).perform()
        time.sleep(10)
        abc = title.is_displayed()
        title.click()
        time.sleep(10)
        return abc

    @allure.step('verify Synopsis title')
    def VerifySynopsisTitle(self):

        synopsis = self.browser.find_element(*self.synopsis_title)
        synopsis.location_once_scrolled_into_view
        time.sleep(5)
        name = synopsis.is_displayed()
        print(name)
        return name

    @allure.step('Click Movie Card Watch Movie Button')
    def ClickWatchMovieButton(self):
        watch_movie = self.browser.find_element(*self.movie_card_watch_now)
        ActionChains(self.browser).move_to_element(watch_movie).perform()
        time.sleep(3)
        watch_movie.click()
        time.sleep(10)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(65)

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(65)

    @allure.step('Verify pop up for watch trailer is opening ')
    def watch_movie_popup(self):
        styl = self.browser.find_element(*self.watch_popup).get_attribute('style')
        print(styl)
        return styl

    @allure.step('CLick on close image to close movie')
    def click_crossimg(self):
        self.browser.find_element(*self.close_button).click()

    @allure.step('Click Main Carousel Next Navigation button')
    def MainCareusalClickNextNavigationArrow(self):
        self.browser.find_element(*self.next_navigation).click()

    @allure.step('Click Main carousel previous navigation button')
    def MainCareusalClickPrevNavigationArrow(self):
        self.browser.find_element(*self.previous_navigtion).click()

    @allure.step('verify slider reset after last movie')
    def SliderBarReset(self):
        for x in range(0,7):
            self.browser.find_element(*self.next_navigation).click()
    
    @allure.step('Verify titles of movie are underligned')
    def SliderTitleHighlighted(self):
        movie = self.browser.find_element(*self.titles_underligned)
        return movie.text

    @allure.step('user is abl to scroll properly')
    def VerifyScroll(self):
        verify = self.browser.find_element(*self.see_all_movies)
        verify.location_once_scrolled_into_view
        return verify.is_displayed()

    @allure.step('Check carousel is auto progress')
    def CarouselAutoProgress(self):
        self.browser.refresh()
        a = self.browser.find_element(*self.progress_bar_spectre)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(a).perform()
        time.sleep(20)
        b = self.browser.find_element(*self.progress_bar_amigos).is_displayed()
        print(b)
        return b
    @allure.step('slider movie Army of Darkness')
    def SliderMovie(self):
        s = self.browser.find_element(*self.next_navigation)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(s).perform()
        try:
            a = self.browser.find_element(*self.progress_bar_armyofdarkness)
            z = a.is_displayed()
            print(a)
            print(z)
            if z == True:
                return True
        except:
            return False

    def RecentlyWatched(self):
        return self.browser.find_element(*self.recently_watched).is_displayed()

    def Refresh(self):
        self.browser.refresh()
        time.sleep(5)

    def RecentlyWatchedNextButton(self):
        nextbtn = self.browser.find_element(*self.movie_list_next_button)
        nextbtn.location_once_scrolled_into_view
        global actionchains
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(nextbtn).perform()
        btn = nextbtn.is_displayed()
        nextbtn.click()
        return btn

    def RecentlyWatchedPrevButton(self):
        prevbtn = self.browser.find_element(*self.movie_list_prev_button)
        prevbtn.location_once_scrolled_into_view
        time.sleep(5)
        actionchains.move_to_element(prevbtn).perform()
        # prevbtn.click()
        return self.browser.find_element(*self.movie_list_prev_button).is_displayed()

    def RecentlyWatchedPosterImage(self):
        image = self.browser.find_element(*self.poster_image)
        image.location_once_scrolled_into_view
        a = image.is_displayed()
        return a

    def MovieSortedCorrectOrder(self):
        movie = []
        movie = self.browser.find_elements(*self.movie_name)
        name = movie[0].text
        print(name)
        return name

    def ClickMainCarouselAddToList(self):
        self.browser.find_element(*self.add_to_list_button).click()

    def AddToListSearchBox(self):
        return self.browser.find_element(*self.add_to_list_search).is_displayed()

    def AddToListCreatedList(self):
        return self.browser.find_element(*self.add_to_list_list_name).is_displayed()

    def AddToListToggelButton(self):
        return self.browser.find_element(*self.add_to_list_toggel_button).is_displayed()

    def AddToListCreateList(self):
        return self.browser.find_element(*self.add_to_list_create_list).is_displayed()

    def AddToListListName(self):
        return self.browser.find_element(*self.add_to_list_enter_name).is_displayed()

    def AddToListCreateListButton(self):
        return self.browser.find_element(*self.add_to_list_create_list).is_displayed()

    def ListName(self, name):
        self.browser.find_element(*self.add_to_list_enter_name).send_keys(name)

    def ClickCreateList(self):
        self.browser.find_element(*self.add_to_list_create_list).click()
        time.sleep(5)
        return self.browser.find_element(*self.add_to_list_creating).is_displayed()

    def NewList(self):
        time.sleep(10)
        list = self.browser.find_element(*self.new_list).text
        return list

    def ListAutoSelect(self):
        time.sleep(3)
        return self.browser.find_element(*self.selected_list).is_displayed()
#
    def ClickAddToListToggelButton(self):
        self.browser.find_element(*self.add_to_list_toggel_button).click()

    def ClickAddToListToggleButton1(self):
        self.browser.find_element(*self.add_to_list_toggel_button1).click()

    def AddMovieToList(self):
        time.sleep(10)

        time.sleep(5)
        self.browser.find_element(*self.add_to_list).click()
        time.sleep(20)

    def VerifyAddedMovie(self):
        self.browser.find_element(*self.header_mylist).click()
        scroll = self.browser.find_element(*self.created_list)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        scroll.click()
        verify = self.browser.find_element(*self.add_to_list_verify)
        movie = verify.text
        return movie

    def VerifySecondAddedMovie(self):
        self.browser.find_element(*self.header_mylist).click()
        scroll = self.browser.find_element(*self.created_list)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        scroll.click()
        verify = self.browser.find_element(*self.add_to_list_verify)
        movie = verify.text
        return movie

    def SearchList(self, name):
        self.browser.find_element(*self.add_to_list_search).send_keys(name)

    def VerifySearchedList(self):
        self.browser.find_element(*self.add_to_list_toggel_button1).is_displayed()

    def AddToListClearButton(self):
        return self.browser.find_element(*self.add_to_list_clear).is_displayed()

    def ClickAddToListClearButton(self):
        self.browser.find_element(*self.add_to_list_clear).click()

    def ClickMovieCardAddToList(self):
        list = []
        list = self.browser.find_elements(*self.movie_card_list)
        print(len(list))
        list[10].location_once_scrolled_into_view
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(list[10]).perform()
        list[10].click()
        time.sleep(10)
        return self.browser.find_element(*self.add_to_list_search).is_displayed()

    def VerifyListCreated(self):
        time.sleep(10)
        lists = []
        lists = self.browser.find_elements(*self.new_list1)
        name = lists[2].text
        return name
    
    def CreatedList(self):
        a = WebDriverWait(self.browser,15).until(EC.presence_of_element_located(*self.add_to_list_created))
        #self.browser.find_element(*self.add_to_list_created).is_displayed()
        return a.is_displayed()
    
    def q(self):
        a=[]
        a = self.browser.find_elements(*self.abc)
        print(len(a) + "element")
        b= a[2].get_attribute("class")
        print(b)

    @allure.step('Verify Add to List option in recently watched movie card')
    def addTolist_bestpicture(self):
        time.sleep(1)
        card1 = self.browser.find_element(*self.cardhover_option1)
        ActionChains(self.browser).move_to_element(card1).perform()
        return self.browser.find_element(*self.cardhover_option1).text

    @allure.step('Verify Watch movie option in recently watched movie card')
    def watchMoviesoption(self):
        time.sleep(1)
        return self.browser.find_element(*self.cardhover_option2).text

    @allure.step('Verify Watch Trailer option in recently watched movie card')
    def watchTraileroption(self):
        time.sleep(1)
        return self.browser.find_element(*self.cardhover_option3).text

    @allure.step('Verify View Details option in recently watched movie card')
    def viewDetailsoption(self):
        time.sleep(1)
        return self.browser.find_element(*self.cardhover_option4).text