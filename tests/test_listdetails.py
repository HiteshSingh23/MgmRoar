import pytest
from pages.LoginPage import loginpage
from pages.ListDetails import ListDetails
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
    # request_account = user.VerifyRequestAnAccount()
    # assert request_account == True, "Request an account button not found"


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


@allure.title('tc-35,Verify elements in mylist details page')
def test_mylistdetails(browser):
    global listdet
    listdet = ListDetails(browser)
    listdet.verify_addmovietolist()
    listdet.verify_mylist()
    assert listdet.verify_listheadername() == 'Demo', "title not found in list details page"
    assert listdet.verify_listgridbutton() == True, "grid button not found in list details page"
    assert listdet.verify_listbutton() == True, "list button not found in list details page"
    assert listdet.verify_sharebutton() == True, "share button not found in list details page"
    assert listdet.verify_deletebutton() == True, "delete button not found in list details page"
    assert listdet.verify_moviedetail() == True, "movie details not found in list details page"
    assert listdet.verify_moviecheckbox() == True, "movie checkbox not found in list details page"
    # assert listdet.verify_listcheckbox() == True, "checkbox button not found in list details page"


@allure.title('tc-36,Verify overlay present in movie card')
def test_mylistoverlaydetails(browser):
    global listdet
    listdet = ListDetails(browser)
    listdet.verify_overlaypanel()
    assert listdet.verify_addolist() == True, "add to list element not found"
    assert listdet.verify_watchmovie() == True, "watch movie element not found"
    assert listdet.verify_watchtrailer() == True, "watch trailer element not found"
    assert listdet.verify_viewdetails() == True, "view details element not found"


@allure.title('tc-38,Verify list view is displayed')
def test_listview(browser):
    global listdet
    listdet = ListDetails(browser)
    listdet.verify_listview()


@allure.title('tc-39,Verify elements list view is displayed')
def test_listelements(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_listelements() == 'TITLE', "title header in list not found"
    assert listdet.verify_directedelements() == 'DIRECTED BY', "DIRECTED BY header in list not found"
    assert listdet.verify_maincastelements() == 'MAIN CAST', "MAIN CAST header in list not found"
    assert listdet.verify_synopsiselements() == 'SYNOPSIS', "SYNOPSIS header in list not found"


@allure.title('tc-40,verify user is able to select title using checkbox')
def test_titleselect(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_titleselect() == True, "list title is not selected"


@allure.title('tc-41,To verify footer section when selected a title')
def test_footersection(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_footersection() == True, "footer section not found"


@allure.title('tc-42,To verify added title to the list')
def test_addtitletolist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_addtitletolist() == True, "Added title in list not found"


@allure.title('tc-43,To verify created list in add to list')
def test_createlist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_createlist() == True, "created list not found in add to list items"


@allure.title('tc-44,To verify title in created list')
def test_titleincreatedlist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_createdlist() == True, "created list not found"
    assert listdet.verify_titleincreatedlist() == True, "title not found in created list"


@allure.title('tc-45,To verify user is able to share title')
def test_sharelist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_sharewindow() == True, "share window not found"
    assert listdet.verify_shareemail() == False, "List not shared through mail"

#
# @allure.title('tc-47,To verify user is able to download csv')
# def test_downloadcsv(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_downloadcsv() == True, "downloaded csv not found"
#
#
# @allure.title('tc-48,To verify select all titile checkbox')
# def test_selectalltitle(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_selectalltitle() == True, "select all checkbox not selected"
#
#
# @allure.title('tc-50,To Verify User is able to share list by clicking on Share button in header')
# def test_sharelistheader(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_sharelistheader() == False, "List not shared through mail"
#
#
# @allure.title('tc-46,To verify delete title in the list')
# def test_deletetitle(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     listdet.verify_deletetitle()
#
#
# @allure.title('tc-49,To Verify user is able to Delete list')
# def test_deletelist(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_deletelist() == False, "list not removed from my list page"
#
#
# @allure.title('tc-37,To verify Watch Movie should not be shown in case of a TV entity')
# def test_watchmovieintv(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_watchmovieintv() == False, "Watch Movie should shown in case of a TV entity"
