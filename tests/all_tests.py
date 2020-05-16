import pytest
from pages.LoginPage import loginpage
from pages.home_page import homePageObj
from pages.recently_addList import recaddListObj
from pages.homepage_myLists import homePagemylistsObj
from pages.myList import myListObj
from resources.variables import *
import allure
import time


@allure.title('Verify user lands on login page')
@pytest.mark.usefixtures("browser")
def test_loginpage(browser):
    global user
    user = loginpage(browser)
    verify = user.load()
    assert verify == "Log in to MGM ROAR", "Unable to load login page"
    print(verify)


#
@allure.title('Verify carousel image set by admin is visible')
def test_verifycarousalimage(browser):
    verify = user.CarouselImage()
    assert verify == True


@allure.title('verify elements present in login model')
def test_elementloginmodel(browser):
    email = user.VerifyEmail()
    assert email == True, "Email textbox not found"
    next_button = user.VerifyNextButton()
    assert next_button == True, "Next button not found"
    request_account = user.VerifyRequestAnAccount()
    assert request_account == True, "Request an account button not found"


@allure.title('Verify user is able to enter Email in email field')
def test_enteremail(browser):
    user.EnterEmail(email)


@allure.title('Verify user with valid email id can proceed to next step')
def test_clicknext(browser):
    verify = user.ClickNext()
    assert verify == True, "user not proceed to next step with valid email id"


@allure.title('verify user is successfully logged in')
def test_login(browser):
    user.EnterPassword(password)
    user.ClickNext()
    time.sleep(10)
    verify = user.VerifyLogin()
    assert verify == True, "User is not able to login with valid credentials"


#
# @allure.title('TC: 49, Verify Recently Watched slider is displayed if user watches a movie')
# def test_recently_watched_slider(browser):
#     home_page = homePageObj(browser)
#     time.sleep(2)
#     assert home_page.verify_recentlywatched() == 'Recently Watched', "Recently watched slider option is not displaying "
#
#
# @allure.title('TC: 50, Verify elements for Recently Watched section')
# def test_recently_watched_options(browser):
#     home_page = homePageObj(browser)
#     time.sleep(3)
#     # assert home_page.verify_moviecards() == True, "Movie cards is not displaying in recently watched "
#     time.sleep(1)
#     assert home_page.verify_titleText() == True, "Title text for movie in recently wathced is not displaying"
#     assert home_page.verify_scroll() == True, "Horizontal scroll is not displaying in recently watched "
#     assert home_page.verify_rightarrow() == True, "Right Navigation bar is not showing "
#     time.sleep(2)
#     home_page.click_rightarrow()
#     time.sleep(3)
#     assert home_page.verify_leftarrow() == True, "Left navigation bar is not showing "
#     time.sleep(2)
#     home_page.click_prevarrow()
#     time.sleep(5)
#
#
#
# @allure.title('TC: 53, Verify movies are sorted in correct order')
# def test_correct_order(browser):
#     home_page = homePageObj(browser)
#     home_page.click_watchmovie()
#     time.sleep(4)
#     home_page.click_crossimg()
#     time.sleep(3)
#     global played_moviename, rec_addedmovie
#     played_moviename = home_page.play_moviename()
#     time.sleep(2)
#     rec_addedmovie = home_page.recent_moviename()
#     time.sleep(3)
#     assert played_moviename == rec_addedmovie, "The video played from action/adventure has not been added in recently " \
#                                                "watched playlist in correct ordered "
#
#
# @allure.title('TC: 55, Verify elements for each Movie card in recently watched')
# def test_elementMovieCard1(browser):
#     home_page = homePageObj(browser)
#     assert home_page.verifyMovieTitle() == played_moviename, "Movie title is not displaying in recently watched " \
#                                                              "section "
#     assert home_page.MovieGenre() == "ACTION / ADVENTURE,", "Movie generes not displayed in recently watched "
#
#
# @allure.title('TC: 56, Verify hover behavior on movie cards')
# def test_elementhover_card1(browser):
#     home_page = homePageObj(browser)
#     time.sleep(4)
#     assert home_page.addTolist() == "ADD TO LIST", 'Add to list is not showing on hover of movie card '
#     assert home_page.watchMoviesoption() == "WATCH MOVIE", "Watch movie is not showing on hover of movie card. "
#     assert home_page.watchTraileroption() == "WATCH TRAILER", "Watch movie is not showing on hover of movie card. "
#     assert home_page.viewDetailsoption() == "VIEW DETAILS", "Watch movie is not showing on hover of movie card. "
#
#
#
# @allure.title('TC: 57, Verify functionality of Add to List button')
# def test_addlist_functionality(browser):
#     home_page = homePageObj(browser)
#     home_page.click_addList()
#     assert home_page.verifyAlert() == "Select List(s)", "After clicking on add to list button Pop is not opening. "
#     time.sleep(3)
#
#
# @allure.title('TC: 58, Verify functionality of Watch Movie button')
# def test_watchmovie_functionality(browser):
#     home_page = homePageObj(browser)
#     time.sleep(3)
#     home_page.click_recwatch_movie()
#     time.sleep(12)
#     assert home_page.watch_movie_popup() == "width: 1140px; height: 640px;", "Pop up is not opening for watch trailer " \
#                                                                              "in recently watched movies "
#     home_page.choose_click()
#     time.sleep(2)
#     home_page.click_crossimg()
#
#
# @allure.title('TC: 60, Verify functionality of Watch Trailer button')
# def test_watchtrailer_functionality(browser):
#     home_page = homePageObj(browser)
#     time.sleep(5)
#     home_page.click_recwatch_trailer()
#     time.sleep(15)
#     assert home_page.watch_movie_popup() == "width: 1140px; height: 640px;", "Pop up is not opening for watch " \
#                                                                              "trailer in recently watched movies "
#     time.sleep(2)
#     home_page.click_crossimg()
#
#
# @allure.title('TC: 62, Verify functionality of View Details button')
# def test_viewdetails_functionality(browser):
#     home_page = homePageObj(browser)
#     home_page.click_viewdetails()
#     time.sleep(10)
#     assert home_page.verify_pagetitle() == rec_addedmovie + " | Movie - ROAR", "After clicking on view details button " \
#                                                                                "Movie details page is not opeing. "
#     home_page.click_mgmimg()
#
#
# @allure.title('TC : 64, Verify Right Navigation Arrow is visible only when we hover on the last card on the right')
# def test_right_navigation(browser):
#     home_page = homePageObj(browser)
#     time.sleep(3)
#     assert home_page.verify_rightarrow() == True, "Right navigation arrow should displayed when hover over last movie " \
#                                                   "cards. "
#
#
# @allure.title('TC: 65, Verify click behavior of Right Navigation arrow')
# def test_clickright_navigation(browser):
#     home_page = homePageObj(browser)
#     home_page.click_rightarrow()
#     time.sleep(1)
#     # assert home_page.verify_1card_slide() == False, "after clicking on right navigation 1 movie is displaying "
#
#
#
# @allure.title('TC: 66, Verify Right Navigation Arrow is disabled when we are on the last card in the list')
# def test_rightnav_disabled(browser):
#     home_page = homePageObj(browser)
#     time.sleep(2)
#     home_page.click_secnav_arrow()
#     time.sleep(2)
#     assert home_page.verify_right_disbaled() == False, "Right nav is not disabled when it is on last movie cards. "
#     time.sleep(5)
#
#
#
# @allure.title('TC : 67, Verify Left Navigation Arrow is visible only when we hover on the first card on the left')
# def test_left_navigation(browser):
#     home_page = homePageObj(browser)
#     time.sleep(3)
#     assert home_page.verify_leftarrow() == True, "Left navigation arrow is not displaying after hover on first movie " \
#                                                "cards "
#
#
# @allure.title('TC: 68, Verify click behavior of Left Navigation arrow')
# def test_clickleft_navigation(browser):
#     home_page = homePageObj(browser)
#     home_page.click_prevarrow()
#
#
# @allure.title('TC: 69, Verify Left Navigation Arrow is disabled when we are on the first card in the list')
# def test_leftnav_disabled(browser):
#     home_page = homePageObj(browser)
#     time.sleep(3)
#     assert home_page.verify_left_disbaled() == False, "Left nav is not disabled when it is on first movie cards. "
#
#
# @allure.title('TC: 93, Verify on click of Add to List button, Add List pop up is opened')
# def test_recentlyAddlist_opened(browser):
#     add = recaddListObj(browser)
#     assert add.verify_addToList() == "Select List(s)", "After clicking on add to list button on Movie cards Pop is " \
#                                                        "not opening. "
#
#
# @allure.title('TC: 94, Verify user is able to enter name and create new list from Carousel')
# def test_createList(browser):
#     add_list = recaddListObj(browser)
#     add_list.click_listName()
#     time.sleep(3)
#     add_list.enter_Listname(new_List_name)
#     time.sleep(1)
#     add_list.click_createList_text()
#     assert add_list.verify_LoaderText() == "Creating...", "After clicking on create list button Loader is not " \
#                                                           "displaying. "
#     # time.sleep(20)
#     time.sleep(2)
#     assert add_list.verify_success_msg() == True, "Success message is not showing after creating new List. "
#     time.sleep(2)
#     assert add_list.verify_newCreatedlist() == new_List_name, "After Creating new List . It is nit displayed in pop ."
#     time.sleep(3)
#     assert add_list.verify_checkBox() == True, "Newly created list is not auto selected. "
#
#
# @allure.title('TC: 95, Verify user is able to add the movie in the created list')
# def test_addMovie_list(browser):
#     home_page = homePageObj(browser)
#     add_list = recaddListObj(browser)
#     time.sleep(3)
#     add_list.click_Addlist_button()
#     time.sleep(18)
#     home_page.clickAutomationlist()
#     assert home_page.verifyMovie_list("Hercules (2014)") == "Hercules (2014)", "Added Movie is not showing in " \
#                                                                                "Automation List "
#     home_page.delete_movie("Hercules (2014)")
#     time.sleep(10)
#     home_page.click_verify_new_list()
#     assert home_page.verifyMovie_list("Hercules (2014)") == "Hercules (2014)", "Added Movie is not showing in " \
#                                                                                "Automation List "
#     home_page.delete_movie("Hercules (2014)")
#     time.sleep(50)
#     home_page.click_mgmimg()
#
#
# @allure.title('TC: 96, Verify user is able to select list(s)')
# def test_select_list(browser):
#     select = recaddListObj(browser)
#     select.click_addtoList2Card()
#     select.click_listName()
#     assert select.verify_selectList() == True, "Clicking in toggle button, list is not getting selected."
#
#
# @allure.title('TC: 97, Verify user is able to un-select any selected list(s)')
# def test_unselect_list(browser):
#     unselect = recaddListObj(browser)
#     unselect.click_listName()
#     assert unselect.verify_selectList() == False, "Clicking in toggle button twice, list is not getting unselected."
#     time.sleep(2)
#
#
# @allure.title('TC: 98, Verify user is able to add same movie in multiple lists')
# def test_addmovie_multiple(browser):
#     movie = recaddListObj(browser)
#     home_page = homePageObj(browser)
#     movie.click_listName()
#     movie.select_newlyList()
#     time.sleep(2)
#     movie.click_Addlist_button()
#     time.sleep(18)
#     home_page.clickAutomationlist()
#     assert home_page.verifyMovie_list("Detroit") == "Detroit", "Added Movie is not showing in Automation List "
#     home_page.delete_movie("Detroit")
#     time.sleep(10)
#     home_page.click_verify_new_list()
#     assert home_page.verifyMovie_list("Detroit") == "Detroit", "Added Movie is not showing in Automation List "
#     home_page.delete_movie("Detroit")
#     time.sleep(50)
#     home_page.click_mgmimg()
#
#
# @allure.title('TC: 99, Verify user is abe to search a list from the search bar')
# def test_searchList(browser):
#     add = recaddListObj(browser)
#     time.sleep(3)
#     assert add.verify_addToList() == "Select List(s)", "After clicking on add to list button on Movie cards Pop is " \
#                                                        "not opening. "
#     time.sleep(2)
#     add.enter_listname_search(new_List_name)
#     time.sleep(2)
#     assert add.verify_Listcount() == 1, "After entering list name in search bocx more than one items is showing in " \
#                                         "lists "
#     assert add.verify_searchElement() == new_List_name, "Searched element is not showing in list "
#
#
# @allure.title('TC: 100, Verify user is able to clear search on click of Clear button')
# def test_clearsearch(browser):
#     clear = recaddListObj(browser)
#     time.sleep(2)
#     assert clear.verify_Clearbutton() == "Search cleared", "After clicking on clear button search result is not clear."
#     time.sleep(4)
#
#
# @allure.title('TC: 101, Verify user is able to select list(s) from search result')
# def test_search_selectList(browser):
#     select = recaddListObj(browser)
#     select.enter_listname_search("Automation List")
#     select.click_listName()
#     assert select.verify_selectList() == True, "After searching List name , user is not able to select list ."
#

@allure.title('TC: 102, Verify user is able to un-select list(s) from search result')
def test_search_unselectList(browser):
    unselect = recaddListObj(browser)
    time.sleep(2)
    unselect.click_listName()
    assert unselect.verify_selectList() == False, "After clear search user is not able to unselect list ."
    time.sleep(2)
    assert unselect.verify_Clearbutton() == "Search cleared", "After clicking on clear button search result is not " \
                                                              "clear. "


@allure.title('TC: 103, Verify user is able to add to multiple movies in same list')
def test_multimovie_1list(browser):
    multi = recaddListObj(browser)
    multi.click_listName()
    multi.click_Addlist_button()
    time.sleep(18)
    multi.click_2cardAdd()
    multi.click_listName()
    multi.click_Addlist_button()
    time.sleep(18)


@allure.title('TC: 104, Verify only 10 movie card is shown')
def test_totalmovie_cards(browser):
    total = recaddListObj(browser)
    time.sleep(3)
    assert total.verify_Totalmovie() <= 10, " Movie cards contains more than 10 movie in recently watched section "


@allure.title('TC: 105, Verify created lists are shown in the My Lists slider')
def test_createdLists(browser):
    lists = homePagemylistsObj(browser)
    time.sleep(40)
    assert lists.verify_autoList() == True, "Automation list is not displaying in My list slider"
    time.sleep(1)
    assert lists.verify_Mylists() <= 10, " My Lists contains more than 10 cards. it should be 10 or less than 10 "




